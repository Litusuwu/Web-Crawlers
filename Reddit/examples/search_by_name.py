"""
Example: Search Reddit for mentions of a person/name.

This script demonstrates how to search Reddit for posts mentioning
a specific person (e.g., "John Cena").
"""

import json

from reddit_scraper import RedditAPIClient, SearchScraper


def main():
    """Search for posts mentioning a specific person."""

    # Initialize the Reddit API client
    # Credentials are loaded from environment variables or .env file
    print("Initializing Reddit API client...")
    client = RedditAPIClient()

    # Test the connection
    if not client.test_connection():
        print("Failed to connect to Reddit API. Check your credentials.")
        return

    print("Connected successfully!")
    print(f"Remaining API requests: {client.get_remaining_requests()}\n")

    # Initialize search scraper
    scraper = SearchScraper(client)

    # Search for mentions of "John Cena"
    search_query = "John Cena"
    print(f"Searching Reddit for: {search_query}")
    print("This may take a moment...\n")

    # Perform search
    results = scraper.search_all(
        query=search_query,
        limit=25,  # Get top 25 results
        sort="relevance",
        time_filter="all",
    )

    # Display results
    print(f"Found {len(results)} posts mentioning '{search_query}':\n")
    print("=" * 80)

    for i, post in enumerate(results, 1):
        print(f"\n{i}. {post.title}")
        print(f"   Author: u/{post.author}")
        print(f"   Subreddit: r/{post.subreddit}")
        print(f"   Score: {post.score} | Comments: {post.num_comments}")
        print(f"   Posted: {post.timestamp}")
        print(f"   URL: {post.permalink}")

        if post.media_urls:
            print(f"   Media: {len(post.media_urls)} file(s)")

        if post.body:
            # Show first 100 characters of body
            body_preview = (
                post.body[:100] + "..." if len(post.body) > 100 else post.body
            )
            print(f"   Preview: {body_preview}")

        print("   " + "-" * 76)

    # Save results to JSON file
    output_file = "john_cena_results.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(
            [post.model_dump(mode="json") for post in results],
            f,
            indent=2,
            ensure_ascii=False,
        )

    print(f"\n✓ Results saved to {output_file}")
    print(f"✓ Remaining API requests: {client.get_remaining_requests()}")


if __name__ == "__main__":
    main()
    main()
