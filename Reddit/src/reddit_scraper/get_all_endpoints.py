#!/usr/bin/env python3
"""
Reddit API Endpoints - Complete Response Examples
Gets actual responses from all major Reddit endpoints.
"""

import json
import time
from datetime import datetime

import requests


class RedditEndpointTester:
    """Test and document Reddit API endpoints."""

    def __init__(self):
        self.base_url = "https://www.reddit.com"
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "python:reddit-endpoint-tester:v1.0"
        })
        self.results = {}

    def save_response(self, endpoint_name, url, params, response):
        """Save endpoint response to file and memory."""
        data = {
            "endpoint": endpoint_name,
            "url": url,
            "params": params,
            "timestamp": datetime.now().isoformat(),
            "status_code": response.status_code,
            "headers": {
                "content-type": response.headers.get("content-type"),
                "x-ratelimit-remaining": response.headers.get("x-ratelimit-remaining"),
                "x-ratelimit-reset": response.headers.get("x-ratelimit-reset"),
            },
            "response": response.json() if response.status_code == 200 else None
        }
        
        self.results[endpoint_name] = data
        
        # Save to individual file
        filename = f"out/endpoint_{endpoint_name.replace('/', '_')}.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        return data

    def test_search_all(self):
        """Test /search endpoint - Search all Reddit."""
        print("\n" + "=" * 70)
        print("1. ENDPOINT: /search (Search all Reddit)")
        print("=" * 70)
        
        url = f"{self.base_url}/search.json"
        params = {
            "q": "John Cena",
            "limit": 1,
            "sort": "relevance",
            "raw_json": 1
        }
        
        print(f"URL: {url}")
        print(f"Params: {json.dumps(params, indent=2)}")
        
        response = self.session.get(url, params=params, timeout=10)
        data = self.save_response("search", url, params, response)
        
        if response.status_code == 200:
            result = response.json()
            count = len(result.get('data', {}).get('children', []))
            print(f"✅ Success! Found {count} posts")
        else:
            print(f"❌ Error: {response.status_code}")
        
        return data

    def test_subreddit_search(self):
        """Test /r/{sub}/search endpoint - Search within subreddit."""
        print("\n" + "=" * 70)
        print("2. ENDPOINT: /r/{subreddit}/search (Search within subreddit)")
        print("=" * 70)
        
        url = f"{self.base_url}/r/SquaredCircle/search.json"
        params = {
            "q": "John Cena",
            "restrict_sr": "on",
            "limit": 1,
            "sort": "relevance",
            "raw_json": 1
        }
        
        print(f"URL: {url}")
        print(f"Params: {json.dumps(params, indent=2)}")
        
        response = self.session.get(url, params=params, timeout=10)
        data = self.save_response("r_subreddit_search", url, params, response)
        
        if response.status_code == 200:
            result = response.json()
            count = len(result.get('data', {}).get('children', []))
            print(f"✅ Success! Found {count} posts in r/SquaredCircle")
        else:
            print(f"❌ Error: {response.status_code}")
        
        return data

    def test_user_submitted(self):
        """Test /user/{username}/submitted endpoint."""
        print("\n" + "=" * 70)
        print("3. ENDPOINT: /user/{username}/submitted (User submissions)")
        print("=" * 70)
        
        url = f"{self.base_url}/user/spez/submitted.json"
        params = {
            "limit": 1,
            "raw_json": 1
        }
        
        print(f"URL: {url}")
        print(f"Params: {json.dumps(params, indent=2)}")
        
        response = self.session.get(url, params=params, timeout=10)
        data = self.save_response("user_submitted", url, params, response)
        
        if response.status_code == 200:
            result = response.json()
            count = len(result.get('data', {}).get('children', []))
            print(f"✅ Success! Found {count} submissions from u/spez")
        else:
            print(f"❌ Error: {response.status_code}")
        
        return data

    def test_post_comments(self):
        """Test /comments/{post_id} endpoint."""
        print("\n" + "=" * 70)
        print("4. ENDPOINT: /r/{subreddit}/comments/{post_id} (Post comments)")
        print("=" * 70)
        
        # First, get a post ID from search
        search_url = f"{self.base_url}/r/python/hot.json"
        search_response = self.session.get(
            search_url, 
            params={"limit": 1, "raw_json": 1}, 
            timeout=10
        )
        
        if search_response.status_code != 200:
            print("❌ Could not fetch a post ID")
            return None
        
        posts = search_response.json()['data']['children']
        if not posts:
            print("❌ No posts found")
            return None
        
        post = posts[0]['data']
        post_id = post['id']
        subreddit = post['subreddit']
        
        # Now get comments
        url = f"{self.base_url}/r/{subreddit}/comments/{post_id}.json"
        params = {
            "limit": 1,
            "raw_json": 1
        }
        
        print(f"URL: {url}")
        print(f"Params: {json.dumps(params, indent=2)}")
        print(f"Post: {post['title'][:60]}...")
        
        response = self.session.get(url, params=params, timeout=10)
        data = self.save_response("comments", url, params, response)
        
        if response.status_code == 200:
            result = response.json()
            # Comments response has 2 listings: post and comments
            if len(result) >= 2:
                comments = result[1]['data']['children']
                print(f"✅ Success! Found {len(comments)} comments")
            else:
                print("✅ Success! (response structure retrieved)")
        else:
            print(f"❌ Error: {response.status_code}")
        
        return data

    def test_user_about(self):
        """Test /user/{username}/about endpoint - User info."""
        print("\n" + "=" * 70)
        print("5. ENDPOINT: /user/{username}/about (User information)")
        print("=" * 70)
        
        url = f"{self.base_url}/user/spez/about.json"
        params = {"raw_json": 1}
        
        print(f"URL: {url}")
        print(f"Params: {json.dumps(params, indent=2)}")
        
        response = self.session.get(url, params=params, timeout=10)
        data = self.save_response("user_about", url, params, response)
        
        if response.status_code == 200:
            result = response.json()
            user = result.get('data', {})
            print(f"✅ Success! User: u/{user.get('name', 'unknown')}")
            print(f"   Karma: {user.get('total_karma', 0):,}")
        else:
            print(f"❌ Error: {response.status_code}")
        
        return data

    def test_subreddit_about(self):
        """Test /r/{subreddit}/about endpoint - Subreddit info."""
        print("\n" + "=" * 70)
        print("6. ENDPOINT: /r/{subreddit}/about (Subreddit information)")
        print("=" * 70)
        
        url = f"{self.base_url}/r/python/about.json"
        params = {"raw_json": 1}
        
        print(f"URL: {url}")
        print(f"Params: {json.dumps(params, indent=2)}")
        
        response = self.session.get(url, params=params, timeout=10)
        data = self.save_response("subreddit_about", url, params, response)
        
        if response.status_code == 200:
            result = response.json()
            sub = result.get('data', {})
            print(f"✅ Success! r/{sub.get('display_name', 'unknown')}")
            print(f"   Subscribers: {sub.get('subscribers', 0):,}")
        else:
            print(f"❌ Error: {response.status_code}")
        
        return data

    def create_summary(self):
        """Create a summary document of all endpoints."""
        summary = {
            "test_date": datetime.now().isoformat(),
            "total_endpoints_tested": len(self.results),
            "endpoints": []
        }
        
        for name, data in self.results.items():
            summary["endpoints"].append({
                "name": name,
                "url": data["url"],
                "status": "✅ Success" if data["status_code"] == 200 else "❌ Failed",
                "status_code": data["status_code"],
                "response_file": f"endpoint_{name.replace('/', '_')}.json"
            })
        
        # Save summary
        with open("out/endpoints_summary.json", 'w', encoding='utf-8') as f:
            json.dump(summary, f, indent=2, ensure_ascii=False)
        
        return summary


def main():
    """Run all endpoint tests."""
    print("=" * 70)
    print("REDDIT API ENDPOINTS - COMPLETE TESTING")
    print("=" * 70)
    print()
    print("Testing all major Reddit API endpoints without OAuth...")
    print("Responses will be saved to out/ directory")
    print()
    
    # Create output directory
    import os
    os.makedirs("out", exist_ok=True)
    
    tester = RedditEndpointTester()
    
    # Test all endpoints
    tests = [
        tester.test_search_all,
        tester.test_subreddit_search,
        tester.test_user_submitted,
        tester.test_post_comments,
        tester.test_user_about,
        tester.test_subreddit_about
    ]
    
    for i, test in enumerate(tests):
        if i > 0:
            print("\n⏳ Waiting 3 seconds to respect rate limits...")
            time.sleep(3)
        
        try:
            test()
        except Exception as e:
            print(f"❌ Error: {e}")
    
    # Create summary
    print("\n" + "=" * 70)
    print("CREATING SUMMARY")
    print("=" * 70)
    summary = tester.create_summary()
    
    print(f"\n✅ Tested {summary['total_endpoints_tested']} endpoints")
    print(f"\nFiles created in out/ directory:")
    for endpoint in summary["endpoints"]:
        status_icon = "✅" if "Success" in endpoint["status"] else "❌"
        print(f"  {status_icon} {endpoint['response_file']}")
    print(f"  📊 endpoints_summary.json")
    
    print("\n" + "=" * 70)
    print("ENDPOINT DOCUMENTATION")
    print("=" * 70)
    print("""
All Reddit public JSON endpoints (no OAuth required):

1. /search.json
   - Search all of Reddit
   - Params: q, limit, sort, t (time)
   
2. /r/{subreddit}/search.json
   - Search within specific subreddit
   - Params: q, restrict_sr=on, limit, sort
   
3. /user/{username}/submitted.json
   - Get user's submitted posts
   - Params: limit, sort, t
   
4. /r/{subreddit}/comments/{post_id}.json
   - Get post with all comments
   - Returns: [post, comments] array
   
5. /user/{username}/about.json
   - Get user profile information
   - Returns: User data (karma, created, etc)
   
6. /r/{subreddit}/about.json
   - Get subreddit information
   - Returns: Subreddit data (subscribers, etc)

Additional endpoints:
- /r/{subreddit}/hot.json
- /r/{subreddit}/new.json
- /r/{subreddit}/top.json
- /user/{username}/comments.json

All responses are in JSON format.
Add ?raw_json=1 to prevent HTML escaping.
    """)
    
    print("=" * 70)
    print("✅ COMPLETE!")
    print("=" * 70)


if __name__ == "__main__":
    main()
    main()
