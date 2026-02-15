"""Tests to verify stealth evasion effectiveness.

These tests run against local browser instances to validate that
our custom JS overrides and stealth args properly mask automation
indicators. The stealth plugin itself (which monkey-patches at the
class level) is tested via scripts/check_detection.py instead.
"""

from __future__ import annotations

import pytest_asyncio
from playwright.async_api import async_playwright

from tiktok_scraper.stealth_config import STEALTH_ARGS, STEALTH_JS_OVERRIDES, VIEWPORT


@pytest_asyncio.fixture
async def stealth_page():
    """Create a Playwright page with our custom stealth overrides."""
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(
            headless=True,
            args=STEALTH_ARGS,
        )
        context = await browser.new_context(viewport=VIEWPORT)
        page = await context.new_page()
        await page.add_init_script(STEALTH_JS_OVERRIDES)
        await page.goto("about:blank")
        yield page
        await browser.close()


async def test_webdriver_is_hidden(stealth_page):
    """navigator.webdriver should be undefined, not true."""
    webdriver = await stealth_page.evaluate("navigator.webdriver")
    assert webdriver is not True, "navigator.webdriver is exposed as True"


async def test_plugins_are_present(stealth_page):
    """navigator.plugins should report at least 1 plugin."""
    plugin_count = await stealth_page.evaluate("navigator.plugins.length")
    assert plugin_count > 0, "No plugins reported — headless detection risk"


async def test_languages_are_set(stealth_page):
    """navigator.languages should return a realistic array."""
    languages = await stealth_page.evaluate("navigator.languages")
    assert len(languages) > 0, "Empty languages array — detection risk"
    assert "en-US" in languages, "en-US not in languages"


async def test_chrome_object_exists(stealth_page):
    """window.chrome should exist in Chromium."""
    has_chrome = await stealth_page.evaluate("!!window.chrome")
    assert has_chrome, "window.chrome object missing"


async def test_viewport_dimensions(stealth_page):
    """Viewport should match configured dimensions."""
    width = await stealth_page.evaluate("window.innerWidth")
    height = await stealth_page.evaluate("window.innerHeight")
    assert width == VIEWPORT["width"], f"Width mismatch: {width}"
    assert height == VIEWPORT["height"], f"Height mismatch: {height}"
