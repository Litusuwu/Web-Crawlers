"""Search scraper for Reddit."""

from typing import Optional

import praw

from ..api_client import RedditAPIClient
from ..models import RedditPost
from ..utils import extract_media_urls, safe_get_author, timestamp_from_utc


class SearchScraper:
    """
    Scraper for Reddit search functionality.
    Supports searching for posts, users, and specific queries.
    """

    def __init__(self, client: RedditAPIClient):
        """
        Initialize search scraper.

        Args:
            client: Authenticated Reddit API client
        """
        self.client = client

    def search_all(
        self,
        query: str,
        limit: int = 100,
        sort: str = "relevance",
        time_filter: str = "all",
    ) -> list[RedditPost]:
        """
        Search across all of Reddit.

        Args:
            query: Search query (e.g., "John Cena")
            limit: Maximum number of results (default 100)
            sort: Sort method ('relevance', 'hot', 'top', 'new', 'comments')
            time_filter: Time filter ('all', 'day', 'hour', 'month', 'week', 'year')

        Returns:
            List of RedditPost objects
        """
        self.client.wait_for_rate_limit()

        results = []
        search_results = self.client.reddit.subreddit("all").search(
            query=query, limit=limit, sort=sort, time_filter=time_filter
        )

        for submission in search_results:
            post = self._submission_to_post(submission)
            results.append(post)

        return results

    def search_subreddit(
        self,
        subreddit: str,
        query: str,
        limit: int = 100,
        sort: str = "relevance",
        time_filter: str = "all",
    ) -> list[RedditPost]:
        """
        Search within a specific subreddit.

        Args:
            subreddit: Subreddit name (without 'r/')
            query: Search query
            limit: Maximum number of results
            sort: Sort method
            time_filter: Time filter

        Returns:
            List of RedditPost objects
        """
        self.client.wait_for_rate_limit()

        results = []
        search_results = self.client.reddit.subreddit(subreddit).search(
            query=query, limit=limit, sort=sort, time_filter=time_filter
        )

        for submission in search_results:
            post = self._submission_to_post(submission)
            results.append(post)

        return results

    def search_by_author(self, username: str, limit: int = 100) -> list[RedditPost]:
        """
        Get all submissions by a specific user.

        Args:
            username: Reddit username
            limit: Maximum number of results

        Returns:
            List of RedditPost objects
        """
        self.client.wait_for_rate_limit()

        results = []
        redditor = self.client.reddit.redditor(username)

        for submission in redditor.submissions.new(limit=limit):
            post = self._submission_to_post(submission)
            results.append(post)

        return results

    def search_mentions(
        self, name: str, limit: int = 100, subreddits: Optional[list[str]] = None
    ) -> list[RedditPost]:
        """
        Search for mentions of a person/name across Reddit.
        This is useful for finding posts about specific people like "John Cena".

        Args:
            name: Name to search for (e.g., "John Cena")
            limit: Maximum number of results
            subreddits: Optional list of subreddits to search (default: all)

        Returns:
            List of RedditPost objects
        """
        if subreddits:
            # Search across multiple subreddits
            subreddit_str = "+".join(subreddits)
        else:
            # Search all of Reddit
            subreddit_str = "all"

        return self.search_subreddit(
            subreddit=subreddit_str,
            query=f'"{name}"',  # Use quotes for exact phrase matching
            limit=limit,
            sort="relevance",
        )

    def _submission_to_post(self, submission: praw.models.Submission) -> RedditPost:
        """
        Convert PRAW submission to RedditPost model.

        Args:
            submission: PRAW submission object

        Returns:
            RedditPost object
        """
        return RedditPost(
            id=submission.id,
            title=submission.title,
            body=submission.selftext if submission.is_self else None,
            author=safe_get_author(submission),
            timestamp=timestamp_from_utc(submission.created_utc),
            subreddit=submission.subreddit.display_name,
            url=submission.url,
            score=submission.score,
            num_comments=submission.num_comments,
            media_urls=extract_media_urls(submission),
            permalink=f"https://reddit.com{submission.permalink}",
            is_self=submission.is_self,
            link_flair_text=submission.link_flair_text,
        )
