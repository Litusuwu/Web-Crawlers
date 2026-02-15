"""End-to-end scraping tests for TikTok evaluation.

These tests make real network requests and are marked as integration tests.
Run with: uv run pytest tests/test_scraping.py -v -m integration

NOTE: These tests require:
  - Playwright browsers installed (uv run playwright install chromium)
  - Proxy configuration in .env (recommended)
  - Network access
"""

from __future__ import annotations

import pytest

from tiktok_scraper.config import get_config
from tiktok_scraper.scrapers.hydration_scraper import extract_hydration_data
from tiktok_scraper.scrapers.playwright_scraper import scrape_with_playwright


@pytest.mark.asyncio
@pytest.mark.integration
async def test_playwright_tiktok_home():
    """Playwright should be able to load TikTok home page."""
    config = get_config()
    result = await scrape_with_playwright(
        url="https://www.tiktok.com/en",
        config=config,
    )
    assert result.response_status in (200, 403), f"Unexpected status: {result.response_status}"

    if result.success:
        assert result.page_title, "Page title should not be empty on success"


@pytest.mark.asyncio
@pytest.mark.integration
async def test_hydration_extraction():
    """httpx should be able to fetch a TikTok profile page."""
    config = get_config()
    result = await extract_hydration_data(
        url="https://www.tiktok.com/@tiktok",
        config=config,
    )
    assert result.status_code in (200, 403), f"Unexpected status: {result.status_code}"

    if result.success:
        assert result.hydration_data is not None, "Should have hydration data on success"


@pytest.mark.asyncio
@pytest.mark.integration
async def test_explore_page_access():
    """Playwright should attempt TikTok explore page."""
    config = get_config()
    result = await scrape_with_playwright(
        url="https://www.tiktok.com/explore",
        config=config,
    )
    # Record detection signals regardless of outcome
    if result.detection_signals:
        for signal in result.detection_signals:
            print(f"  Detection signal: {signal}")

    if result.blocked:
        print("  BLOCKED — TikTok detected automation")
    if result.captcha:
        print("  CAPTCHA — TikTok requires verification")
    if result.login_wall:
        print("  LOGIN WALL — TikTok requires authentication")
