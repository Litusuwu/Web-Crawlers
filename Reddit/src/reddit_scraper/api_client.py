"""Reddit API client with OAuth2 authentication."""

import os

import praw
from dotenv import load_dotenv

from .rate_limiter import RateLimiter


class RedditAPIClient:
    """
    Reddit API client wrapper using PRAW with OAuth2.
    Handles authentication and rate limiting.
    """

    def __init__(
        self,
        client_id: str | None = None,
        client_secret: str | None = None,
        user_agent: str | None = None,
        username: str | None = None,
        password: str | None = None,
    ):
        """
        Initialize Reddit API client.

        Args:
            client_id: Reddit app client ID (env: REDDIT_CLIENT_ID)
            client_secret: Reddit app secret (env: REDDIT_CLIENT_SECRET)
            user_agent: User agent string (env: REDDIT_USER_AGENT)
            username: Reddit username (optional, for user auth)
            password: Reddit password (optional, for user auth)
        """
        # Load environment variables
        load_dotenv()

        # Get credentials from parameters or environment
        self.client_id = client_id or os.getenv("REDDIT_CLIENT_ID")
        self.client_secret = client_secret or os.getenv("REDDIT_CLIENT_SECRET")
        self.user_agent = user_agent or os.getenv(
            "REDDIT_USER_AGENT", "reddit-scraper/0.1.0"
        )
        self.username = username or os.getenv("REDDIT_USERNAME")
        self.password = password or os.getenv("REDDIT_PASSWORD")

        if not self.client_id or not self.client_secret:
            raise ValueError(
                "Reddit API credentials required. Set REDDIT_CLIENT_ID and "
                "REDDIT_CLIENT_SECRET environment variables or pass them as parameters."
            )

        # Initialize rate limiter (100 requests per minute)
        self.rate_limiter = RateLimiter(max_requests=100, time_window=60)

        # Initialize PRAW Reddit instance
        self._reddit: praw.Reddit | None = None

    @property
    def reddit(self) -> praw.Reddit:
        """Get or create authenticated Reddit instance."""
        if self._reddit is None:
            if self.username and self.password:
                # User-authenticated (script) mode
                self._reddit = praw.Reddit(
                    client_id=self.client_id,
                    client_secret=self.client_secret,
                    user_agent=self.user_agent,
                    username=self.username,
                    password=self.password,
                )
            else:
                # Read-only mode
                self._reddit = praw.Reddit(
                    client_id=self.client_id,
                    client_secret=self.client_secret,
                    user_agent=self.user_agent,
                )

        return self._reddit

    def wait_for_rate_limit(self) -> float | None:
        """
        Wait if necessary to respect rate limits.

        Returns:
            Time waited in seconds, or None if no wait was needed
        """
        return self.rate_limiter.wait_if_needed()

    def get_remaining_requests(self) -> int:
        """Get number of API requests remaining in current window."""
        return self.rate_limiter.get_remaining_requests()

    def test_connection(self) -> bool:
        """
        Test the API connection.

        Returns:
            True if connection successful, False otherwise
        """
        try:
            # Try to fetch user info (read-only request)
            if self.username:
                user = self.reddit.user.me()
                return user is not None
            else:
                # For read-only mode, just verify we can access Reddit
                subreddit = self.reddit.subreddit("python")
                return subreddit.display_name is not None
        except Exception as e:
            print(f"Connection test failed: {e}")
            return False
            print(f"Connection test failed: {e}")
            return False
