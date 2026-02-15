"""Hydration JSON scraper for TikTok.

Attempts to extract data from TikTok's __UNIVERSAL_DATA_FOR_REHYDRATION__
script tag using httpx (no browser). This is the lightest approach but
has the highest detection risk due to Python's TLS fingerprint mismatch.
"""

from __future__ import annotations

import json
import logging
from dataclasses import dataclass, field

import httpx
from selectolax.parser import HTMLParser

from tiktok_scraper.config import AppConfig, get_config

logger = logging.getLogger(__name__)

TIKTOK_HEADERS = {
    "Accept": (
        "text/html,application/xhtml+xml,application/xml;q=0.9,"
        "image/avif,image/webp,image/apng,*/*;q=0.8"
    ),
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Cache-Control": "no-cache",
    "Pragma": "no-cache",
    "Sec-Ch-Ua": '"Chromium";v="131", "Not_A Brand";v="24"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"macOS"',
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/131.0.0.0 Safari/537.36"
    ),
}


@dataclass
class HydrationResult:
    """Result of hydration JSON extraction."""

    url: str
    success: bool
    status_code: int = 0
    hydration_data: dict | None = None
    user_data: dict | None = None
    video_data: list[dict] = field(default_factory=list)
    error: str = ""
    tls_fingerprint_risk: str = "HIGH"


async def extract_hydration_data(
    url: str = "https://www.tiktok.com/@tiktok",
    config: AppConfig | None = None,
) -> HydrationResult:
    """Extract TikTok page data via hydration JSON without a browser.

    WARNING: This approach uses Python's TLS stack (httpx/httpcore),
    which has a different TLS fingerprint than Chrome. TikTok may
    detect this mismatch and block the request.

    Args:
        url: TikTok page URL (profile pages work best).
        config: Application configuration.

    Returns:
        HydrationResult with extracted data or error details.
    """
    if config is None:
        config = get_config()

    result = HydrationResult(
        url=url,
        success=False,
        tls_fingerprint_risk="HIGH — Python httpx TLS != Chrome TLS",
    )

    proxy_url = None
    if config.proxy.is_configured:
        proxy_url = config.proxy.url or f"http://{config.proxy.host}:{config.proxy.port}"

    try:
        async with httpx.AsyncClient(
            proxy=proxy_url,
            headers=TIKTOK_HEADERS,
            follow_redirects=True,
            timeout=30.0,
        ) as client:
            response = await client.get(url)
            result.status_code = response.status_code

            if response.status_code != 200:
                result.error = f"HTTP {response.status_code}"
                return result

            tree = HTMLParser(response.text)
            script_tag = tree.css_first("script#__UNIVERSAL_DATA_FOR_REHYDRATION__")

            if not script_tag:
                result.error = "Hydration script tag not found — page may be blocked or empty"
                return result

            raw_json = script_tag.text()
            if not raw_json:
                result.error = "Hydration script tag is empty"
                return result

            hydration = json.loads(raw_json)
            result.hydration_data = hydration

            # Navigate the hydration JSON to extract useful data
            default_scope = hydration.get("__DEFAULT_SCOPE__", {})

            # User data (for profile pages)
            user_detail = default_scope.get("webapp.user-detail", {})
            if user_detail:
                result.user_data = user_detail.get("userInfo", {})

            # Video list data
            video_detail = default_scope.get("webapp.video-detail", {})
            if video_detail:
                item_info = video_detail.get("itemInfo", {})
                if item_info:
                    result.video_data = [item_info.get("itemStruct", {})]

            result.success = True
            logger.info("Hydration data extracted successfully from %s", url)

    except httpx.HTTPError as e:
        result.error = f"HTTP error: {e}"
        logger.exception("httpx request failed")
    except json.JSONDecodeError as e:
        result.error = f"JSON parse error: {e}"
        logger.exception("Failed to parse hydration JSON")
    except Exception as e:
        result.error = f"Unexpected error: {e}"
        logger.exception("Hydration extraction failed")

    return result
