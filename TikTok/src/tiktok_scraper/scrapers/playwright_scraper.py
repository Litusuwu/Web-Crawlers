"""Playwright + stealth-plugin scraper for TikTok evaluation.

Tests whether Playwright with anti-detection plugins can access
TikTok's public pages without triggering bot detection.
"""

from __future__ import annotations

import json
import logging
from dataclasses import dataclass, field

from playwright.async_api import async_playwright
from playwright_stealth_plugin import async_apply

from tiktok_scraper.config import AppConfig, get_config
from tiktok_scraper.stealth_config import STEALTH_ARGS, STEALTH_JS_OVERRIDES, VIEWPORT
from tiktok_scraper.utils.behavioral import human_delay, simulate_scroll

logger = logging.getLogger(__name__)


@dataclass
class ScrapeResult:
    """Result of a TikTok scraping attempt."""

    url: str
    success: bool
    blocked: bool = False
    captcha: bool = False
    login_wall: bool = False
    hydration_data: dict | None = None
    page_title: str = ""
    error: str = ""
    response_status: int = 0
    detection_signals: list[str] = field(default_factory=list)


async def scrape_with_playwright(
    url: str = "https://www.tiktok.com/en",
    config: AppConfig | None = None,
) -> ScrapeResult:
    """Attempt to scrape a TikTok page using Playwright + stealth plugin.

    Args:
        url: TikTok URL to scrape.
        config: Application configuration. Uses defaults if None.

    Returns:
        ScrapeResult with details about the attempt.
    """
    if config is None:
        config = get_config()

    result = ScrapeResult(url=url, success=False)

    async with async_playwright() as pw:
        # Apply stealth plugin — monkey-patches chromium.launch to inject
        # anti-detection scripts automatically into all pages/contexts.
        await async_apply(pw)

        launch_args = {
            "headless": config.browser.headless,
            "args": STEALTH_ARGS,
        }

        if config.proxy.is_configured:
            launch_args["proxy"] = config.proxy.playwright_proxy
            logger.info("Using proxy: %s", config.proxy.host or "configured")
        else:
            logger.warning("No proxy configured — TikTok will likely block this request")

        browser = await pw.chromium.launch(**launch_args)

        context = await browser.new_context(
            viewport=VIEWPORT,
            user_agent=config.browser.user_agent or None,
            locale="en-US",
            timezone_id="America/New_York",
        )

        page = await context.new_page()

        # Additional custom JS overrides on top of stealth plugin
        await page.add_init_script(STEALTH_JS_OVERRIDES)

        try:
            response = await page.goto(url, wait_until="domcontentloaded", timeout=30000)
            result.response_status = response.status if response else 0

            await human_delay(2.0, 4.0)

            result.page_title = await page.title()

            # Check for login wall
            login_selectors = [
                '[data-e2e="modal-close-inner-button"]',
                'div[class*="LoginModal"]',
                'div[class*="login-modal"]',
            ]
            for sel in login_selectors:
                if await page.query_selector(sel):
                    result.login_wall = True
                    result.detection_signals.append(f"Login wall detected: {sel}")
                    import contextlib

                    with contextlib.suppress(Exception):
                        await page.click(sel, timeout=3000)
                    break

            # Check for CAPTCHA
            captcha_selectors = [
                'iframe[src*="captcha"]',
                'div[class*="captcha"]',
                '#captcha-verify-image',
                'div[class*="Captcha"]',
            ]
            for sel in captcha_selectors:
                if await page.query_selector(sel):
                    result.captcha = True
                    result.detection_signals.append(f"CAPTCHA detected: {sel}")
                    break

            # Check for block page
            page_content = await page.content()
            block_indicators = [
                "Access Denied",
                "blocked",
                "unusual traffic",
                "verify you are human",
            ]
            for indicator in block_indicators:
                if indicator.lower() in page_content.lower():
                    result.blocked = True
                    result.detection_signals.append(f"Block indicator: '{indicator}'")

            # Try to extract hydration data
            hydration_el = await page.query_selector(
                'script#__UNIVERSAL_DATA_FOR_REHYDRATION__'
            )
            if hydration_el:
                raw_json = await hydration_el.text_content()
                if raw_json:
                    try:
                        result.hydration_data = json.loads(raw_json)
                        logger.info("Successfully extracted hydration JSON")
                    except json.JSONDecodeError:
                        result.detection_signals.append("Hydration JSON parse failed")

            # Test infinite scroll
            if not result.blocked and not result.captcha:
                await simulate_scroll(page, scrolls=2)
                await human_delay(1.0, 2.0)

            result.success = (
                not result.blocked
                and not result.captcha
                and result.response_status == 200
            )

        except Exception as e:
            result.error = str(e)
            logger.exception("Playwright scrape failed")
        finally:
            await browser.close()

    return result
