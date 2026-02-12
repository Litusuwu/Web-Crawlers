"""Tests for Reddit scrapers."""
from datetime import datetime
from unittest.mock import MagicMock, Mock, patch

import pytest
from reddit_scraper.api_client import RedditAPIClient
from reddit_scraper.models import RedditPost
from reddit_scraper.scrapers.search import SearchScraper


@pytest.fixture
def mock_client():
    """Create a mock Reddit API client."""
    with patch.dict('os.environ', {
        'REDDIT_CLIENT_ID': 'test_id',
        'REDDIT_CLIENT_SECRET': 'test_secret'
    }):
        client = RedditAPIClient()
        client.rate_limiter.wait_if_needed = Mock(return_value=None)
        return client


@pytest.fixture
def mock_submission():
    """Create a mock Reddit submission."""
    submission = Mock()
    submission.id = 'abc123'
    submission.title = 'Test Post'
    submission.selftext = 'Test body'
    submission.is_self = True
    submission.author.name = 'test_user'
    submission.created_utc = 1234567890
    submission.subreddit.display_name = 'test'
    submission.url = 'https://reddit.com/r/test/comments/abc123/'
    submission.score = 100
    submission.num_comments = 10
    submission.permalink = '/r/test/comments/abc123/'
    submission.link_flair_text = None
    submission.media = None
    submission.is_gallery = False
    submission.preview = {}  # Fix for mock preview attribute
    return submission


def test_search_scraper_initialization(mock_client):
    """Test search scraper initialization."""
    scraper = SearchScraper(mock_client)
    assert scraper.client == mock_client


def test_submission_to_post(mock_client, mock_submission):
    """Test conversion of PRAW submission to RedditPost."""
    scraper = SearchScraper(mock_client)
    post = scraper._submission_to_post(mock_submission)
    
    assert isinstance(post, RedditPost)
    assert post.id == 'abc123'
    assert post.title == 'Test Post'
    assert post.author == 'test_user'
    assert post.subreddit == 'test'
    assert post.score == 100
    assert post.num_comments == 10


def test_search_all(mock_client, mock_submission):
    """Test searching all of Reddit."""
    scraper = SearchScraper(mock_client)
    
    # Mock the reddit.subreddit().search() method
    mock_search = Mock(return_value=[mock_submission])
    mock_client._reddit = Mock()
    mock_client._reddit.subreddit.return_value.search = mock_search
    
    results = scraper.search_all(query="test", limit=1)
    
    assert len(results) == 1
    assert isinstance(results[0], RedditPost)
    assert results[0].title == 'Test Post'
    assert results[0].title == 'Test Post'
