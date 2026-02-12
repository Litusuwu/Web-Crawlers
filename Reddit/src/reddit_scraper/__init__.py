"""
Reddit Scraper - A Python package for scraping Reddit data.

This package provides tools to search and extract data from Reddit using
the official Reddit API (PRAW) with proper rate limiting and data modeling.
"""

from .api_client import RedditAPIClient
from .models import RedditComment, RedditPost, RedditUser
from .rate_limiter import RateLimiter
from .scrapers.comments import CommentScraper
from .scrapers.search import SearchScraper
from .scrapers.user import UserScraper

__version__ = "0.1.0"
__all__ = [
    "RedditAPIClient",
    "RedditPost",
    "RedditComment",
    "RedditUser",
    "SearchScraper",
    "UserScraper",
    "CommentScraper",
    "RateLimiter",
]


def main():
    """Entry point for the reddit-scraper CLI."""
    print("Reddit Scraper v0.1.0")
    print("Use the examples/ directory for usage examples.")
    print("\nQuick start:")
    print("1. Copy .env.example to .env and add your Reddit API credentials")
    print("2. Run: uv run python examples/search_by_name.py")
