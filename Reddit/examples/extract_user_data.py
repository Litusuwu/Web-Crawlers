"""
Example: Extract data from a specific Reddit user.

This script demonstrates how to get user profile information
and their submission history.
"""

import json

from reddit_scraper import RedditAPIClient, UserScraper


def main():
    """Extract data from a Reddit user."""
    
    # Initialize the Reddit API client
    print("Initializing Reddit API client...")
    client = RedditAPIClient()
    
    # Test the connection
    if not client.test_connection():
        print("Failed to connect to Reddit API. Check your credentials.")
        return
    
    print("Connected successfully!\n")
    
    # Initialize user scraper
    scraper = UserScraper(client)
    
    # Example username (change this to any Reddit username)
    username = "spez"  # Reddit CEO's account
    
    print(f"Fetching data for user: u/{username}\n")
    
    # Get user profile
    print("Getting user profile...")
    try:
        user = scraper.get_user_profile(username)
        
        print(f"\n{'=' * 60}")
        print(f"User Profile: u/{user.username}")
        print(f"{'=' * 60}")
        print(f"Account created: {user.created_utc}")
        print(f"Comment karma: {user.comment_karma:,}")
        print(f"Link karma: {user.link_karma:,}")
        print(f"Reddit Gold: {'Yes' if user.is_gold else 'No'}")
        print(f"Moderator: {'Yes' if user.is_mod else 'No'}")
        print(f"Verified: {'Yes' if user.verified else 'No'}")
        
    except Exception as e:
        print(f"Error fetching user profile: {e}")
        return
    
    # Get user submissions
    print(f"\nFetching recent submissions by u/{username}...")
    try:
        submissions = scraper.get_user_submissions(username, limit=10)
        
        print(f"\nFound {len(submissions)} recent submissions:\n")
        
        for i, post in enumerate(submissions, 1):
            print(f"{i}. {post.title}")
            print(f"   Subreddit: r/{post.subreddit}")
            print(f"   Score: {post.score} | Comments: {post.num_comments}")
            print(f"   Posted: {post.timestamp}")
            print(f"   URL: {post.permalink}")
            print()
        
        # Save to JSON
        output_data = {
            'user': user.model_dump(mode='json'),
            'submissions': [post.model_dump(mode='json') for post in submissions]
        }
        
        output_file = f"{username}_data.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, indent=2, ensure_ascii=False)
        
        print(f"✓ Data saved to {output_file}")
        
    except Exception as e:
        print(f"Error fetching user submissions: {e}")
    
    print(f"\n✓ Remaining API requests: {client.get_remaining_requests()}")


if __name__ == "__main__":
    main()
    main()
