"""Tests to validate proxy configuration and connectivity.

Run these tests BEFORE attempting TikTok scraping to ensure
the proxy is working correctly.
"""

from __future__ import annotations

import pytest

from tiktok_scraper.config import get_config


def test_proxy_config_loads():
    """Proxy configuration should load from environment."""
    config = get_config()
    assert config.proxy is not None


def test_proxy_playwright_format():
    """Playwright proxy dict should have correct structure when configured."""
    config = get_config()
    if not config.proxy.is_configured:
        pytest.skip("No proxy configured — set PROXY_URL in .env")

    proxy = config.proxy.playwright_proxy
    assert proxy is not None
    assert "server" in proxy
    assert proxy["server"].startswith(("http://", "https://", "socks5://"))


def test_scraping_config_defaults():
    """Scraping config should have sensible defaults."""
    config = get_config()
    assert config.scraping.min_request_delay >= 1
    assert config.scraping.max_request_delay > config.scraping.min_request_delay
    assert config.scraping.max_pages_per_session >= 1


def test_browser_config_defaults():
    """Browser config should have reasonable defaults."""
    config = get_config()
    assert config.browser.viewport_width >= 1024
    assert config.browser.viewport_height >= 768
