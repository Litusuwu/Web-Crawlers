"""Configuration management for TikTok scraper evaluation."""

import os
from pathlib import Path

from dotenv import load_dotenv
from pydantic import BaseModel, Field

load_dotenv(Path(__file__).resolve().parent.parent.parent / ".env")


class ProxyConfig(BaseModel):
    """Residential proxy configuration."""

    url: str = Field(default_factory=lambda: os.getenv("PROXY_URL", ""))
    username: str = Field(default_factory=lambda: os.getenv("PROXY_USERNAME", ""))
    password: str = Field(default_factory=lambda: os.getenv("PROXY_PASSWORD", ""))
    host: str = Field(default_factory=lambda: os.getenv("PROXY_HOST", ""))
    port: str = Field(default_factory=lambda: os.getenv("PROXY_PORT", ""))
    socks5_url: str = Field(default_factory=lambda: os.getenv("SOCKS5_PROXY_URL", ""))

    @property
    def is_configured(self) -> bool:
        return bool(self.url or (self.host and self.port))

    @property
    def playwright_proxy(self) -> dict | None:
        """Return proxy dict in Playwright's expected format."""
        if not self.is_configured:
            return None
        proxy = (
            {"server": self.url} if self.url else {"server": f"http://{self.host}:{self.port}"}
        )
        if self.username:
            proxy["username"] = self.username
        if self.password:
            proxy["password"] = self.password
        return proxy


class BrowserConfig(BaseModel):
    """Browser automation settings."""

    headless: bool = Field(
        default_factory=lambda: os.getenv("HEADLESS", "true").lower() == "true"
    )
    viewport_width: int = Field(
        default_factory=lambda: int(os.getenv("VIEWPORT_WIDTH", "1920"))
    )
    viewport_height: int = Field(
        default_factory=lambda: int(os.getenv("VIEWPORT_HEIGHT", "1080"))
    )
    user_agent: str = Field(default_factory=lambda: os.getenv("USER_AGENT", ""))


class ScrapingConfig(BaseModel):
    """Scraping behavior settings."""

    min_request_delay: float = Field(
        default_factory=lambda: float(os.getenv("MIN_REQUEST_DELAY", "3"))
    )
    max_request_delay: float = Field(
        default_factory=lambda: float(os.getenv("MAX_REQUEST_DELAY", "10"))
    )
    max_pages_per_session: int = Field(
        default_factory=lambda: int(os.getenv("MAX_PAGES_PER_SESSION", "5"))
    )


class AppConfig(BaseModel):
    """Root application configuration."""

    proxy: ProxyConfig = Field(default_factory=ProxyConfig)
    browser: BrowserConfig = Field(default_factory=BrowserConfig)
    scraping: ScrapingConfig = Field(default_factory=ScrapingConfig)
    log_level: str = Field(default_factory=lambda: os.getenv("LOG_LEVEL", "INFO"))


def get_config() -> AppConfig:
    """Load and return application configuration."""
    return AppConfig()
