#!/usr/bin/env python3
"""
Reddit Public API - No OAuth Required
Uses public JSON endpoints that don't require authentication.

Note: Rate limits are much stricter without OAuth (~10 req/min vs 100 req/min)
"""

import time
from datetime import datetime

import requests


class RedditPublicScraper:
    """
    Scraper using Reddit's public JSON endpoints.
    No authentication required, but limited rate limits.
    """

    def __init__(self, user_agent: str = "python:reddit-public-scraper:v0.1"):
        """Initialize scraper with custom user agent."""
        self.user_agent = user_agent
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": self.user_agent})
        self.base_url = "https://www.reddit.com"

    def search(self, query: str, limit: int = 25, sort: str = "relevance") -> list:
        """
        Search Reddit without authentication.

        Args:
            query: Search query (e.g., "John Cena")
            limit: Max results (max 100)
            sort: Sort by 'relevance', 'hot', 'top', 'new', 'comments'

        Returns:
            List of post dictionaries
        """
        url = f"{self.base_url}/search.json"
        params = {"q": query, "limit": min(limit, 100), "sort": sort, "raw_json": 1}

        print(f"Requesting: {url}")
        print(f"Query: {query}, Limit: {limit}, Sort: {sort}")
        print()

        try:
            response = self.session.get(url, params=params, timeout=10)

            # Check rate limit headers
            if "x-ratelimit-remaining" in response.headers:
                remaining = response.headers.get("x-ratelimit-remaining")
                reset = response.headers.get("x-ratelimit-reset")
                print(f"Rate limit - Remaining: {remaining}, Reset in: {reset}s")

            response.raise_for_status()

            data = response.json()
            posts = []

            if "data" in data and "children" in data["data"]:
                for child in data["data"]["children"]:
                    post_data = child["data"]
                    posts.append(
                        {
                            "id": post_data.get("id"),
                            "title": post_data.get("title"),
                            "author": post_data.get("author"),
                            "subreddit": post_data.get("subreddit"),
                            "score": post_data.get("score"),
                            "num_comments": post_data.get("num_comments"),
                            "url": post_data.get("url"),
                            "permalink": f"{self.base_url}{post_data.get('permalink')}",
                            "created_utc": post_data.get("created_utc"),
                            "selftext": post_data.get("selftext"),
                            "is_self": post_data.get("is_self"),
                        }
                    )

            return posts

        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 429:
                print("❌ Rate limit exceeded!")
                print(f"Response: {e.response.text}")
            elif e.response.status_code == 403:
                print(
                    "❌ Access forbidden - Reddit may be blocking unauthenticated requests"
                )
                print(f"Response: {e.response.text}")
            else:
                print(f"❌ HTTP Error: {e.response.status_code}")
                print(f"Response: {e.response.text}")
            return []
        except Exception as e:
            print(f"❌ Error: {e}")
            return []

    def search_subreddit(self, subreddit: str, query: str, limit: int = 25) -> list:
        """
        Search within a specific subreddit.

        Args:
            subreddit: Subreddit name (without r/)
            query: Search query
            limit: Max results

        Returns:
            List of post dictionaries
        """
        url = f"{self.base_url}/r/{subreddit}/search.json"
        params = {
            "q": query,
            "restrict_sr": "on",
            "limit": min(limit, 100),
            "raw_json": 1,
        }

        print(f"Requesting: {url}")
        print(f"Subreddit: r/{subreddit}, Query: {query}")
        print()

        try:
            response = self.session.get(url, params=params, timeout=10)
            response.raise_for_status()

            data = response.json()
            posts = []

            if "data" in data and "children" in data["data"]:
                for child in data["data"]["children"]:
                    post_data = child["data"]
                    posts.append(
                        {
                            "id": post_data.get("id"),
                            "title": post_data.get("title"),
                            "author": post_data.get("author"),
                            "subreddit": post_data.get("subreddit"),
                            "score": post_data.get("score"),
                            "num_comments": post_data.get("num_comments"),
                            "url": post_data.get("url"),
                            "permalink": f"{self.base_url}{post_data.get('permalink')}",
                            "created_utc": post_data.get("created_utc"),
                        }
                    )

            return posts

        except Exception as e:
            print(f"❌ Error: {e}")
            return []

    def get_subreddit_posts(
        self, subreddit: str, sort: str = "hot", limit: int = 25
    ) -> list:
        """
        Get posts from a subreddit without search.

        Args:
            subreddit: Subreddit name
            sort: 'hot', 'new', 'top', 'rising'
            limit: Max results
        """
        url = f"{self.base_url}/r/{subreddit}/{sort}.json"
        params = {"limit": min(limit, 100), "raw_json": 1}

        try:
            response = self.session.get(url, params=params, timeout=10)
            response.raise_for_status()

            data = response.json()
            posts = []

            if "data" in data and "children" in data["data"]:
                for child in data["data"]["children"]:
                    post_data = child["data"]
                    posts.append(
                        {
                            "id": post_data.get("id"),
                            "title": post_data.get("title"),
                            "author": post_data.get("author"),
                            "score": post_data.get("score"),
                            "num_comments": post_data.get("num_comments"),
                            "permalink": f"{self.base_url}{post_data.get('permalink')}",
                        }
                    )

            return posts

        except Exception as e:
            print(f"❌ Error: {e}")
            return []


def main():
    """Test Reddit public API without OAuth."""

    print("=" * 70)
    print("REDDIT PUBLIC API TEST (No OAuth)")
    print("=" * 70)
    print()
    print("⚠️  WARNING: Rate limits without OAuth are very strict (~10 req/min)")
    print("⚠️  Reddit may block or limit these requests")
    print()

    scraper = RedditPublicScraper()

    # Test 1: Search all Reddit
    print("TEST 1: Searching all of Reddit for 'John Cena'")
    print("-" * 70)
    results = scraper.search("John Cena", limit=5)

    if results:
        print(f"✅ Found {len(results)} posts:\n")
        for i, post in enumerate(results, 1):
            timestamp = datetime.fromtimestamp(post["created_utc"]).strftime(
                "%Y-%m-%d %H:%M"
            )
            print(f"{i}. {post['title']}")
            print(f"   r/{post['subreddit']} | u/{post['author']}")
            print(f"   Score: {post['score']} | Comments: {post['num_comments']}")
            print(f"   Posted: {timestamp}")
            print(f"   URL: {post['permalink']}")
            print()
    else:
        print("❌ No results or request blocked\n")

    # Wait to respect rate limits
    print("Waiting 5 seconds to respect rate limits...")
    time.sleep(5)

    # Test 2: Search specific subreddit
    print("\nTEST 2: Searching r/SquaredCircle for 'John Cena'")
    print("-" * 70)
    results = scraper.search_subreddit("SquaredCircle", "John Cena", limit=5)

    if results:
        print(f"✅ Found {len(results)} posts:\n")
        for i, post in enumerate(results, 1):
            print(f"{i}. {post['title']}")
            print(f"   Score: {post['score']} | Comments: {post['num_comments']}")
            print(f"   URL: {post['permalink']}")
            print()
    else:
        print("❌ No results or request blocked\n")

    # Test 3: Get hot posts from subreddit
    print("\nTEST 3: Getting hot posts from r/Python (no search)")
    print("-" * 70)
    results = scraper.get_subreddit_posts("python", sort="hot", limit=5)

    if results:
        print(f"✅ Found {len(results)} posts:\n")
        for i, post in enumerate(results, 1):
            print(f"{i}. {post['title']}")
            print(f"   Score: {post['score']} | Author: u/{post['author']}")
            print()
    else:
        print("❌ No results or request blocked\n")

    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print("""
✅ If tests worked: You can scrape Reddit without OAuth!
   - But rate limits are VERY strict (~10 requests/minute)
   - Reddit may block this at any time

❌ If tests failed: Reddit is blocking unauthenticated requests
   - You NEED OAuth credentials (they're free!)
   - Get them at: https://www.reddit.com/prefs/apps
   - Takes 2 minutes to setup
   - OAuth gives you 100 requests/minute (vs 10)

RECOMMENDED: Use OAuth authentication for reliable access.
Run: make setup (to configure OAuth credentials)
    """)


if __name__ == "__main__":
    main()
    main()
