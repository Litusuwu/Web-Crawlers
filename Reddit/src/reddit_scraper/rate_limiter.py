"""Rate limiter for Reddit API requests."""
import time
from collections import deque
from typing import Optional


class RateLimiter:
    """
    Rate limiter to respect Reddit's API limits.
    Default: 100 requests per minute per OAuth client.
    """

    def __init__(self, max_requests: int = 100, time_window: int = 60):
        """
        Initialize rate limiter.

        Args:
            max_requests: Maximum number of requests allowed in time window
            time_window: Time window in seconds (default 60 seconds)
        """
        self.max_requests = max_requests
        self.time_window = time_window
        self.requests: deque[float] = deque()

    def wait_if_needed(self) -> Optional[float]:
        """
        Wait if rate limit would be exceeded.

        Returns:
            Time waited in seconds, or None if no wait was needed
        """
        now = time.time()

        # Remove requests outside the time window
        while self.requests and self.requests[0] < now - self.time_window:
            self.requests.popleft()

        # Check if we need to wait
        if len(self.requests) >= self.max_requests:
            oldest_request = self.requests[0]
            wait_time = (oldest_request + self.time_window) - now
            if wait_time > 0:
                time.sleep(wait_time)
                return wait_time

        # Record this request
        self.requests.append(time.time())
        return None

    def get_remaining_requests(self) -> int:
        """Get number of requests remaining in current window."""
        now = time.time()

        # Remove requests outside the time window
        while self.requests and self.requests[0] < now - self.time_window:
            self.requests.popleft()

        return self.max_requests - len(self.requests)

    def reset(self):
        """Clear all tracked requests."""
        self.requests.clear()
