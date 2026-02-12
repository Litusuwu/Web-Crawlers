"""
Example: Search for people/names across specific subreddits.

This script demonstrates advanced search functionality,
including searching in specific communities.
"""

import json

from reddit_scraper import RedditAPIClient, SearchScraper


def main():
    """Search for a person across multiple subreddits."""
    
    # Initialize client
    print("Initializing Reddit API client...")
    client = RedditAPIClient()
    
    if not client.test_connection():
        print("Failed to connect to Reddit API. Check your credentials.")
        return
    
    print("Connected successfully!\n")
    
    # Initialize scraper
    scraper = SearchScraper(client)
    
    # Person to search for
    person_name = "John Cena"
    
    # Subreddits to search (wrestling-related communities)
    subreddits = ['SquaredCircle', 'WWE', 'Wrasslin', 'prowrestling']
    
    print(f"Searching for '{person_name}' in wrestling communities...")
    print(f"Subreddits: {', '.join(['r/' + s for s in subreddits])}\n")
    
    all_results = {}
    
    # Search each subreddit
    for subreddit in subreddits:
        print(f"Searching r/{subreddit}...")
        
        results = scraper.search_subreddit(
            subreddit=subreddit,
            query=person_name,
            limit=10,
            sort='relevance'
        )
        
        all_results[subreddit] = results
        print(f"  Found {len(results)} posts")
    
    # Display summary
    print(f"\n{'=' * 80}")
    print("SEARCH SUMMARY")
    print(f"{'=' * 80}\n")
    
    total_posts = sum(len(posts) for posts in all_results.values())
    print(f"Total posts found: {total_posts}\n")
    
    # Show top results from each subreddit
    for subreddit, posts in all_results.items():
        if posts:
            print(f"\nTop posts from r/{subreddit}:")
            print("-" * 60)
            
            # Sort by score and show top 3
            top_posts = sorted(posts, key=lambda p: p.score, reverse=True)[:3]
            
            for i, post in enumerate(top_posts, 1):
                print(f"\n{i}. {post.title}")
                print(f"   Score: {post.score} | Comments: {post.num_comments}")
                print(f"   Posted: {post.timestamp}")
                print(f"   URL: {post.permalink}")
    
    # Save all results
    output_data = {
        'search_query': person_name,
        'subreddits': subreddits,
        'total_results': total_posts,
        'results_by_subreddit': {
            subreddit: [post.model_dump(mode='json') for post in posts]
            for subreddit, posts in all_results.items()
        }
    }
    
    output_file = f"{person_name.replace(' ', '_').lower()}_subreddit_search.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)
    
    print(f"\n\n✓ All results saved to {output_file}")
    print(f"✓ Remaining API requests: {client.get_remaining_requests()}")


if __name__ == "__main__":
    main()
    main()
