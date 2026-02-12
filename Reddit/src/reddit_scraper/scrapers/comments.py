"""Comment scraper for Reddit."""
from typing import Optional

import praw

from ..api_client import RedditAPIClient
from ..models import RedditComment
from ..utils import safe_get_author, timestamp_from_utc


class CommentScraper:
    """
    Scraper for Reddit comments.
    Handles comment extraction from posts and comment threads.
    """
    
    def __init__(self, client: RedditAPIClient):
        """
        Initialize comment scraper.
        
        Args:
            client: Authenticated Reddit API client
        """
        self.client = client
    
    def get_post_comments(
        self,
        post_id: str,
        limit: Optional[int] = None,
        sort: str = 'best'
    ) -> list[RedditComment]:
        """
        Get all comments from a post.
        
        Args:
            post_id: Reddit post ID
            limit: Maximum number of comments (None for all)
            sort: Sort method ('best', 'top', 'new', 'controversial', 'old', 'qa')
            
        Returns:
            List of RedditComment objects
        """
        self.client.wait_for_rate_limit()
        
        submission = self.client.reddit.submission(id=post_id)
        submission.comment_sort = sort
        
        if limit:
            submission.comment_limit = limit
        
        # Expand all comment trees
        submission.comments.replace_more(limit=None)
        
        comments = []
        for comment in submission.comments.list():
            if isinstance(comment, praw.models.Comment):
                reddit_comment = self._comment_to_model(comment, post_id)
                comments.append(reddit_comment)
        
        return comments
    
    def get_comment_by_id(self, comment_id: str) -> RedditComment:
        """
        Get a specific comment by ID.
        
        Args:
            comment_id: Reddit comment ID
            
        Returns:
            RedditComment object
        """
        self.client.wait_for_rate_limit()
        
        comment = self.client.reddit.comment(id=comment_id)
        post_id = comment.submission.id
        
        return self._comment_to_model(comment, post_id)
    
    def get_user_comments(
        self,
        username: str,
        limit: int = 100
    ) -> list[RedditComment]:
        """
        Get comments by a specific user.
        
        Args:
            username: Reddit username
            limit: Maximum number of comments
            
        Returns:
            List of RedditComment objects
        """
        self.client.wait_for_rate_limit()
        
        redditor = self.client.reddit.redditor(username)
        comments = []
        
        for comment in redditor.comments.new(limit=limit):
            if isinstance(comment, praw.models.Comment):
                post_id = comment.submission.id
                reddit_comment = self._comment_to_model(comment, post_id)
                comments.append(reddit_comment)
        
        return comments
    
    def _comment_to_model(
        self,
        comment: praw.models.Comment,
        post_id: str
    ) -> RedditComment:
        """
        Convert PRAW comment to RedditComment model.
        
        Args:
            comment: PRAW comment object
            post_id: ID of the parent post
            
        Returns:
            RedditComment object
        """
        return RedditComment(
            id=comment.id,
            body=comment.body,
            author=safe_get_author(comment),
            timestamp=timestamp_from_utc(comment.created_utc),
            score=comment.score,
            parent_id=comment.parent_id,
            post_id=post_id,
            permalink=f"https://reddit.com{comment.permalink}",
            is_submitter=comment.is_submitter
        )
