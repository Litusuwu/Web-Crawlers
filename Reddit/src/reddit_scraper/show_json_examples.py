#!/usr/bin/env python3
"""
Reddit Public API - JSON Request/Response Examples
Shows complete JSON structure of requests and responses.
"""

import json

import requests


def print_json(title: str, data: dict):
    """Pretty print JSON data."""
    print(f"\n{'=' * 70}")
    print(f"{title}")
    print(f"{'=' * 70}")
    print(json.dumps(data, indent=2, ensure_ascii=False))
    print()


def example_1_search_all():
    """Example 1: Search all of Reddit."""
    print("\n" + "=" * 70)
    print("EXAMPLE 1: Search all Reddit for 'John Cena'")
    print("=" * 70)

    # Request configuration
    url = "https://www.reddit.com/search.json"
    params = {"q": "John Cena", "limit": 3, "sort": "relevance", "raw_json": 1}
    headers = {"User-Agent": "python:reddit-public-scraper:v0.1"}

    # Show request details
    print("\n📤 REQUEST:")
    print(f"URL: {url}")
    print("Method: GET")
    print_json("Headers", headers)
    print_json("Query Parameters", params)

    # Make request
    response = requests.get(url, params=params, headers=headers, timeout=10)

    # Show response details
    print("📥 RESPONSE:")
    print(f"Status Code: {response.status_code}")
    print("\nResponse Headers (relevant):")
    relevant_headers = {
        "content-type": response.headers.get("content-type"),
        "x-ratelimit-remaining": response.headers.get("x-ratelimit-remaining"),
        "x-ratelimit-reset": response.headers.get("x-ratelimit-reset"),
        "x-ratelimit-used": response.headers.get("x-ratelimit-used"),
    }
    print(json.dumps(relevant_headers, indent=2))

    # Parse and show full JSON response
    data = response.json()
    print_json("Full JSON Response", data)

    # Show simplified structure
    print("\n📊 SIMPLIFIED POST STRUCTURE:")
    if "data" in data and "children" in data["data"]:
        for i, child in enumerate(data["data"]["children"][:2], 1):  # Show only 2
            post = child["data"]
            simplified = {
                "id": post.get("id"),
                "title": post.get("title"),
                "author": post.get("author"),
                "subreddit": post.get("subreddit"),
                "score": post.get("score"),
                "num_comments": post.get("num_comments"),
                "url": post.get("url"),
                "permalink": post.get("permalink"),
                "created_utc": post.get("created_utc"),
                "selftext": post.get("selftext", "")[:100] + "..."
                if post.get("selftext")
                else None,
                "is_self": post.get("is_self"),
                "thumbnail": post.get("thumbnail"),
                "link_flair_text": post.get("link_flair_text"),
            }
            print(f"\nPost {i}:")
            print(json.dumps(simplified, indent=2, ensure_ascii=False))


def example_2_search_subreddit():
    """Example 2: Search specific subreddit."""
    print("\n" + "=" * 70)
    print("EXAMPLE 2: Search r/SquaredCircle for 'John Cena'")
    print("=" * 70)

    # Request configuration
    url = "https://www.reddit.com/r/SquaredCircle/search.json"
    params = {
        "q": "John Cena",
        "restrict_sr": "on",
        "limit": 2,
        "sort": "relevance",
        "raw_json": 1,
    }
    headers = {"User-Agent": "python:reddit-public-scraper:v0.1"}

    # Show request details
    print("\n📤 REQUEST:")
    print(f"URL: {url}")
    print("Method: GET")
    print_json("Headers", headers)
    print_json("Query Parameters", params)
    print(f"Full Request URL: {url}?{requests.compat.urlencode(params)}")

    # Make request
    response = requests.get(url, params=params, headers=headers, timeout=10)

    # Show response
    print("\n📥 RESPONSE:")
    print(f"Status Code: {response.status_code}")

    data = response.json()

    # Show only the structure (not full response to save space)
    print("\n📊 RESPONSE STRUCTURE:")
    structure = {
        "kind": data.get("kind"),
        "data": {
            "after": data["data"].get("after"),
            "before": data["data"].get("before"),
            "children": f"{len(data['data'].get('children', []))} posts",
            "dist": data["data"].get("dist"),
        },
    }
    print(json.dumps(structure, indent=2))

    # Show first post in detail
    if data["data"]["children"]:
        print("\n📄 FIRST POST (Full JSON):")
        first_post = data["data"]["children"][0]["data"]
        # Select relevant fields only
        relevant_fields = {
            "id": first_post.get("id"),
            "title": first_post.get("title"),
            "author": first_post.get("author"),
            "subreddit": first_post.get("subreddit"),
            "subreddit_name_prefixed": first_post.get("subreddit_name_prefixed"),
            "score": first_post.get("score"),
            "upvote_ratio": first_post.get("upvote_ratio"),
            "num_comments": first_post.get("num_comments"),
            "created_utc": first_post.get("created_utc"),
            "created": first_post.get("created"),
            "url": first_post.get("url"),
            "permalink": first_post.get("permalink"),
            "selftext": first_post.get("selftext", "")[:200] + "..."
            if first_post.get("selftext")
            else None,
            "is_self": first_post.get("is_self"),
            "is_video": first_post.get("is_video"),
            "thumbnail": first_post.get("thumbnail"),
            "link_flair_text": first_post.get("link_flair_text"),
            "link_flair_background_color": first_post.get(
                "link_flair_background_color"
            ),
            "author_flair_text": first_post.get("author_flair_text"),
            "domain": first_post.get("domain"),
            "stickied": first_post.get("stickied"),
            "locked": first_post.get("locked"),
            "over_18": first_post.get("over_18"),
        }
        print(json.dumps(relevant_fields, indent=2, ensure_ascii=False))


def example_3_subreddit_hot():
    """Example 3: Get hot posts from subreddit."""
    print("\n" + "=" * 70)
    print("EXAMPLE 3: Get hot posts from r/Python")
    print("=" * 70)

    # Request configuration
    url = "https://www.reddit.com/r/python/hot.json"
    params = {"limit": 2, "raw_json": 1}
    headers = {"User-Agent": "python:reddit-public-scraper:v0.1"}

    # Show request details
    print("\n📤 REQUEST:")
    print(f"URL: {url}")
    print("Method: GET")
    print_json("Headers", headers)
    print_json("Query Parameters", params)

    # Make request
    response = requests.get(url, params=params, headers=headers, timeout=10)

    print("\n📥 RESPONSE:")
    print(f"Status Code: {response.status_code}")

    data = response.json()

    # Show posts list
    print("\n📊 POSTS LIST:")
    if "data" in data and "children" in data["data"]:
        posts_list = []
        for child in data["data"]["children"]:
            post = child["data"]
            posts_list.append(
                {
                    "id": post.get("id"),
                    "title": post.get("title"),
                    "author": post.get("author"),
                    "score": post.get("score"),
                    "num_comments": post.get("num_comments"),
                    "permalink": post.get("permalink"),
                    "created_utc": post.get("created_utc"),
                }
            )
        print(json.dumps(posts_list, indent=2, ensure_ascii=False))


def example_4_user_posts():
    """Example 4: Get user's submitted posts."""
    print("\n" + "=" * 70)
    print("EXAMPLE 4: Get user posts (u/spez/submitted)")
    print("=" * 70)

    # Request configuration
    url = "https://www.reddit.com/user/spez/submitted.json"
    params = {"limit": 2, "raw_json": 1}
    headers = {"User-Agent": "python:reddit-public-scraper:v0.1"}

    # Show request details
    print("\n📤 REQUEST:")
    print(f"URL: {url}")
    print("Method: GET")
    print_json("Headers", headers)
    print_json("Query Parameters", params)

    # Make request
    response = requests.get(url, params=params, headers=headers, timeout=10)

    print("\n📥 RESPONSE:")
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        data = response.json()

        # Show structure
        print("\n📊 USER POSTS:")
        if "data" in data and "children" in data["data"]:
            for i, child in enumerate(data["data"]["children"], 1):
                post = child["data"]
                print(f"\nPost {i}:")
                print(
                    json.dumps(
                        {
                            "title": post.get("title"),
                            "subreddit": post.get("subreddit"),
                            "score": post.get("score"),
                            "created_utc": post.get("created_utc"),
                            "permalink": post.get("permalink"),
                        },
                        indent=2,
                        ensure_ascii=False,
                    )
                )


def save_full_response():
    """Save a complete response to file for inspection."""
    print("\n" + "=" * 70)
    print("SAVING FULL RESPONSE TO FILE")
    print("=" * 70)

    url = "https://www.reddit.com/search.json"
    params = {"q": "John Cena", "limit": 1, "raw_json": 1}
    headers = {"User-Agent": "python:reddit-public-scraper:v0.1"}

    response = requests.get(url, params=params, headers=headers, timeout=10)

    if response.status_code == 200:
        # Save complete response
        filename = "reddit_response_full.json"
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(response.json(), f, indent=2, ensure_ascii=False)
        print(f"\n✅ Full response saved to: {filename}")

        # Save request details
        filename_req = "reddit_request_example.json"
        request_data = {
            "url": url,
            "method": "GET",
            "headers": headers,
            "params": params,
            "full_url": f"{url}?{requests.compat.urlencode(params)}",
        }
        with open(filename_req, "w", encoding="utf-8") as f:
            json.dump(request_data, f, indent=2, ensure_ascii=False)
        print(f"✅ Request details saved to: {filename_req}")


def main():
    """Run all examples."""
    print("\n" + "=" * 70)
    print("REDDIT PUBLIC API - JSON REQUEST/RESPONSE EXAMPLES")
    print("=" * 70)
    print("\nThis script shows the complete JSON structure of requests and responses")
    print("when using Reddit's public API without OAuth.\n")

    # Run examples
    example_1_search_all()

    print("\n⏳ Waiting 3 seconds...")
    import time

    time.sleep(3)

    example_2_search_subreddit()

    print("\n⏳ Waiting 3 seconds...")
    time.sleep(3)

    example_3_subreddit_hot()

    print("\n⏳ Waiting 3 seconds...")
    time.sleep(3)

    example_4_user_posts()

    # Save full responses
    save_full_response()

    print("\n" + "=" * 70)
    print("SUMMARY - Available Endpoints")
    print("=" * 70)
    print("""
Available public JSON endpoints (no auth required):

1. Search all Reddit:
   GET https://www.reddit.com/search.json?q=query&limit=25

2. Search subreddit:
   GET https://www.reddit.com/r/{subreddit}/search.json?q=query&restrict_sr=on

3. Subreddit posts:
   GET https://www.reddit.com/r/{subreddit}/hot.json
   GET https://www.reddit.com/r/{subreddit}/new.json
   GET https://www.reddit.com/r/{subreddit}/top.json

4. User submissions:
   GET https://www.reddit.com/user/{username}/submitted.json

5. Post comments:
   GET https://www.reddit.com/r/{subreddit}/comments/{post_id}.json

6. User info:
   GET https://www.reddit.com/user/{username}/about.json

All responses are in JSON format. Add ?raw_json=1 to prevent HTML escaping.
    """)

    print("=" * 70)
    print("✅ Check the generated files:")
    print("   - reddit_response_full.json (complete response)")
    print("   - reddit_request_example.json (request structure)")
    print("=" * 70)


if __name__ == "__main__":
    main()
    main()
