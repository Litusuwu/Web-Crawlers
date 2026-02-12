"""User scraper for Reddit."""


from ..api_client import RedditAPIClient
from ..models import RedditPost, RedditUser
from ..utils import timestamp_from_utc
from .search import SearchScraper


class UserScraper:
    """
    Scraper for Reddit user data.
    Handles user profiles, submissions, and comments.
    """
    
    def __init__(self, client: RedditAPIClient):
        """
        Initialize user scraper.
        
        Args:
            client: Authenticated Reddit API client
        """
        self.client = client
        self.search_scraper = SearchScraper(client)
    
    def get_user_profile(self, username: str) -> RedditUser:
        """
        Get user profile information.
        
        Args:
            username: Reddit username
            
        Returns:
            RedditUser object
        """
        self.client.wait_for_rate_limit()
        
        redditor = self.client.reddit.redditor(username)
        
        return RedditUser(
            username=redditor.name,
            created_utc=timestamp_from_utc(redditor.created_utc),
            comment_karma=redditor.comment_karma,
            link_karma=redditor.link_karma,
            is_gold=redditor.is_gold,
            is_mod=redditor.is_mod,
            verified=redditor.verified if hasattr(redditor, 'verified') else False
        )
    
    def get_user_submissions(
        self,
        username: str,
        limit: int = 100,
        sort: str = 'new'
    ) -> list[RedditPost]:
        """
        Get user's submissions (posts).
        
        Args:
            username: Reddit username
            limit: Maximum number of submissions
            sort: Sort method ('new', 'hot', 'top', 'controversial')
            
        Returns:
            List of RedditPost objects
        """
        return self.search_scraper.search_by_author(username, limit)
    
    def user_exists(self, username: str) -> bool:
        """
        Check if a user exists.
        
        Args:
            username: Reddit username
            
        Returns:
            True if user exists, False otherwise
        """
        self.client.wait_for_rate_limit()
        
        try:
            redditor = self.client.reddit.redditor(username)
            # Try to access an attribute to trigger API call
            _ = redditor.id
            return True
        except Exception:
            return False
        except Exception:
            return False
