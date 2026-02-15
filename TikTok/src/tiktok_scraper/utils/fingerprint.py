"""Browser fingerprint generation utilities.

Generates coherent fingerprint profiles where all signals
(UA, platform, viewport, timezone, locale, WebGL) are internally
consistent — a key requirement for evading TikTok detection.
"""

from __future__ import annotations

import random
from dataclasses import dataclass


@dataclass
class FingerprintProfile:
    """A coherent browser fingerprint profile."""

    user_agent: str
    platform: str
    viewport_width: int
    viewport_height: int
    timezone: str
    locale: str
    language: str
    languages: list[str]
    webgl_vendor: str
    webgl_renderer: str
    hardware_concurrency: int
    device_memory: int
    color_depth: int


PROFILES = [
    FingerprintProfile(
        user_agent=(
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/131.0.0.0 Safari/537.36"
        ),
        platform="MacIntel",
        viewport_width=1920,
        viewport_height=1080,
        timezone="America/New_York",
        locale="en-US",
        language="en-US",
        languages=["en-US", "en"],
        webgl_vendor="Google Inc. (Apple)",
        webgl_renderer="ANGLE (Apple, ANGLE Metal Renderer: Apple M1, Unspecified Version)",
        hardware_concurrency=8,
        device_memory=8,
        color_depth=30,
    ),
    FingerprintProfile(
        user_agent=(
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/131.0.0.0 Safari/537.36"
        ),
        platform="Win32",
        viewport_width=1920,
        viewport_height=1080,
        timezone="America/Chicago",
        locale="en-US",
        language="en-US",
        languages=["en-US", "en"],
        webgl_vendor="Google Inc. (NVIDIA)",
        webgl_renderer="ANGLE (NVIDIA, NVIDIA GeForce RTX 3060 Direct3D11 vs_5_0 ps_5_0)",
        hardware_concurrency=12,
        device_memory=16,
        color_depth=24,
    ),
    FingerprintProfile(
        user_agent=(
            "Mozilla/5.0 (X11; Linux x86_64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/131.0.0.0 Safari/537.36"
        ),
        platform="Linux x86_64",
        viewport_width=1920,
        viewport_height=1080,
        timezone="Europe/London",
        locale="en-GB",
        language="en-GB",
        languages=["en-GB", "en"],
        webgl_vendor="Google Inc. (Intel)",
        webgl_renderer="ANGLE (Intel, Mesa Intel(R) UHD Graphics 630, OpenGL 4.6)",
        hardware_concurrency=8,
        device_memory=16,
        color_depth=24,
    ),
]


def get_random_profile() -> FingerprintProfile:
    """Return a random coherent fingerprint profile."""
    return random.choice(PROFILES)


def get_profile_for_platform(platform: str) -> FingerprintProfile:
    """Return a profile matching the specified platform.

    Args:
        platform: One of 'macos', 'windows', 'linux'.
    """
    platform_map = {
        "macos": "MacIntel",
        "windows": "Win32",
        "linux": "Linux x86_64",
    }
    target = platform_map.get(platform.lower(), "MacIntel")

    for profile in PROFILES:
        if profile.platform == target:
            return profile

    return PROFILES[0]
