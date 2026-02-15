"""Proxy rotation and management utilities.

Manages residential proxy connections for TikTok scraping.
TikTok blocks datacenter IPs aggressively — residential proxies
are mandatory for any sustained scraping.
"""

from __future__ import annotations

import logging
import random
from dataclasses import dataclass

import httpx

from tiktok_scraper.config import ProxyConfig

logger = logging.getLogger(__name__)

IP_CHECK_URLS = [
    "https://api.ipify.org?format=json",
    "https://httpbin.org/ip",
    "https://ifconfig.me/ip",
]


@dataclass
class ProxyStatus:
    """Result of proxy connectivity check."""

    is_working: bool
    external_ip: str = ""
    response_time_ms: float = 0
    error: str = ""


async def check_proxy(proxy_config: ProxyConfig) -> ProxyStatus:
    """Verify proxy connectivity and get external IP.

    Args:
        proxy_config: Proxy configuration to test.

    Returns:
        ProxyStatus with connectivity details.
    """
    if not proxy_config.is_configured:
        return ProxyStatus(is_working=False, error="No proxy configured")

    proxy_url = proxy_config.url or f"http://{proxy_config.host}:{proxy_config.port}"
    check_url = random.choice(IP_CHECK_URLS)

    try:
        async with httpx.AsyncClient(proxy=proxy_url, timeout=15.0) as client:
            import time

            start = time.monotonic()
            response = await client.get(check_url)
            elapsed_ms = (time.monotonic() - start) * 1000

            if response.status_code == 200:
                ip = response.text.strip()
                if "{" in ip:
                    import json

                    ip = json.loads(ip).get("ip", ip).get("origin", ip)

                return ProxyStatus(
                    is_working=True,
                    external_ip=ip,
                    response_time_ms=round(elapsed_ms, 1),
                )
            else:
                return ProxyStatus(
                    is_working=False,
                    error=f"HTTP {response.status_code}",
                    response_time_ms=round(elapsed_ms, 1),
                )

    except httpx.ProxyError as e:
        return ProxyStatus(is_working=False, error=f"Proxy error: {e}")
    except httpx.ConnectError as e:
        return ProxyStatus(is_working=False, error=f"Connection error: {e}")
    except Exception as e:
        return ProxyStatus(is_working=False, error=f"Unexpected error: {e}")


async def get_direct_ip() -> str:
    """Get the machine's direct (non-proxied) external IP for comparison."""
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get("https://api.ipify.org?format=json")
            if response.status_code == 200:
                return response.json().get("ip", "unknown")
    except Exception:
        pass
    return "unknown"
