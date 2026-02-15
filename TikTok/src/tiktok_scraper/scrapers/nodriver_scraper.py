"""nodriver-based scraper for TikTok evaluation.

nodriver uses a custom CDP implementation (no WebDriver protocol),
giving it a structural advantage over Selenium/Playwright for
evading automation detection.
"""

from __future__ import annotations

import json
import logging
from dataclasses import dataclass, field

import nodriver as uc

from tiktok_scraper.config import AppConfig, get_config
from tiktok_scraper.stealth_config import DEFAULT_USER_AGENT

logger = logging.getLogger(__name__)


@dataclass
class NodriverResult:
    """Result of a nodriver-based TikTok scrape."""

    url: str
    success: bool
    blocked: bool = False
    captcha: bool = False
    login_wall: bool = False
    hydration_data: dict | None = None
    page_title: str = ""
    error: str = ""
    detection_signals: list[str] = field(default_factory=list)


async def scrape_with_nodriver(
    url: str = "https://www.tiktok.com/en",
    config: AppConfig | None = None,
) -> NodriverResult:
    """Scrape TikTok using nodriver (CDP-based, no WebDriver footprint).

    Args:
        url: TikTok URL to access.
        config: Application configuration.

    Returns:
        NodriverResult with scraping outcome.
    """
    if config is None:
        config = get_config()

    result = NodriverResult(url=url, success=False)

    browser_args = [
        f"--user-agent={DEFAULT_USER_AGENT}",
        "--disable-blink-features=AutomationControlled",
        "--no-first-run",
        "--no-default-browser-check",
    ]

    if config.proxy.is_configured:
        proxy_server = config.proxy.url or f"http://{config.proxy.host}:{config.proxy.port}"
        browser_args.append(f"--proxy-server={proxy_server}")
        logger.info("nodriver using proxy: %s", config.proxy.host or "configured")
    else:
        logger.warning("No proxy configured — detection risk is very high")

    try:
        browser = await uc.start(
            headless=config.browser.headless,
            browser_args=browser_args,
        )

        page = await browser.get(url)

        await page.sleep(3)

        result.page_title = await page.evaluate("document.title")

        # Check page content for blocks
        page_source = await page.evaluate("document.documentElement.outerHTML")

        block_indicators = ["Access Denied", "blocked", "unusual traffic", "verify you are human"]
        for indicator in block_indicators:
            if indicator.lower() in page_source.lower():
                result.blocked = True
                result.detection_signals.append(f"Block detected: '{indicator}'")

        captcha_check = await page.evaluate(
            """
            !!document.querySelector('iframe[src*="captcha"]')
            || !!document.querySelector('div[class*="captcha"]')
            || !!document.querySelector('#captcha-verify-image')
            """
        )
        if captcha_check:
            result.captcha = True
            result.detection_signals.append("CAPTCHA element found")

        login_check = await page.evaluate(
            """
            !!document.querySelector('[data-e2e="modal-close-inner-button"]')
            || !!document.querySelector('div[class*="LoginModal"]')
            """
        )
        if login_check:
            result.login_wall = True
            result.detection_signals.append("Login modal detected")

        # Extract hydration data
        hydration_raw = await page.evaluate(
            """
            (() => {
                const el = document.querySelector(
                    'script#__UNIVERSAL_DATA_FOR_REHYDRATION__'
                );
                return el ? el.textContent : null;
            })()
            """
        )
        if hydration_raw:
            try:
                result.hydration_data = json.loads(hydration_raw)
                logger.info("nodriver extracted hydration JSON")
            except json.JSONDecodeError:
                result.detection_signals.append("Hydration JSON parse failed")

        result.success = not result.blocked and not result.captcha

        browser.stop()

    except Exception as e:
        result.error = str(e)
        logger.exception("nodriver scrape failed")

    return result
