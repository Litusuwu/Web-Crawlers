#!/usr/bin/env python3
"""
Simple CLI for Reddit Scraper

Quick test script to verify the setup is working.
"""

import sys

from reddit_scraper import RedditAPIClient


def main():
    """Test Reddit API connection."""
    print("=" * 60)
    print("Reddit Scraper - Connection Test")
    print("=" * 60)
    
    try:
        print("\n1. Loading credentials from .env file...")
        client = RedditAPIClient()
        print("   ✓ Credentials loaded")
        
        print("\n2. Testing Reddit API connection...")
        if client.test_connection():
            print("   ✓ Connection successful!")
        else:
            print("   ✗ Connection failed")
            print("\nPlease check:")
            print("  - Your .env file has correct credentials")
            print("  - REDDIT_CLIENT_ID is set")
            print("  - REDDIT_CLIENT_SECRET is set")
            sys.exit(1)
        
        print(f"\n3. API Status:")
        print(f"   Remaining requests: {client.get_remaining_requests()}/100")
        print(f"   User agent: {client.user_agent}")
        
        print("\n" + "=" * 60)
        print("✓ Setup Complete! You're ready to scrape Reddit.")
        print("=" * 60)
        print("\nNext steps:")
        print("  - Run: uv run python examples/search_by_name.py")
        print("  - Or check QUICKSTART.md for more examples")
        
    except ValueError as e:
        print(f"\n✗ Error: {e}")
        print("\nSetup instructions:")
        print("  1. Copy .env.example to .env")
        print("  2. Add your Reddit API credentials")
        print("  3. Get credentials at: https://www.reddit.com/prefs/apps")
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
    main()
