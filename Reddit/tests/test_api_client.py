"""Tests for Reddit API client."""
from unittest.mock import Mock, patch

import pytest
from reddit_scraper.api_client import RedditAPIClient


def test_client_initialization():
    """Test client initialization with credentials."""
    with patch.dict('os.environ', {
        'REDDIT_CLIENT_ID': 'test_id',
        'REDDIT_CLIENT_SECRET': 'test_secret'
    }):
        client = RedditAPIClient()
        assert client.client_id == 'test_id'
        assert client.client_secret == 'test_secret'
        assert client.user_agent is not None


def test_client_missing_credentials():
    """Test client raises error when credentials are missing."""
    with patch.dict('os.environ', {}, clear=True):
        with pytest.raises(ValueError):
            RedditAPIClient()


def test_rate_limiter_initialization():
    """Test rate limiter is initialized properly."""
    with patch.dict('os.environ', {
        'REDDIT_CLIENT_ID': 'test_id',
        'REDDIT_CLIENT_SECRET': 'test_secret'
    }):
        client = RedditAPIClient()
        assert client.rate_limiter is not None
        assert client.rate_limiter.max_requests == 100
        assert client.rate_limiter.time_window == 60


def test_get_remaining_requests():
    """Test getting remaining API requests."""
    with patch.dict('os.environ', {
        'REDDIT_CLIENT_ID': 'test_id',
        'REDDIT_CLIENT_SECRET': 'test_secret'
    }):
        client = RedditAPIClient()
        remaining = client.get_remaining_requests()
        assert remaining == 100  # Should be max initially
        assert remaining == 100  # Should be max initially
