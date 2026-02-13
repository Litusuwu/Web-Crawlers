"""
SerpAPI Google Search for Reddit content using site:reddit.com queries.
"""

import json
import os
from datetime import datetime

import requests
from dotenv import load_dotenv

load_dotenv()

SERPAPI_KEY = os.getenv("SERP_API_KEY")
SERPAPI_URL = "https://serpapi.com/search"


def search_reddit(query, limit=10):
    """Search Reddit via Google using site:reddit.com"""
    params = {
        "engine": "google",
        "q": f"site:reddit.com {query}",
        "api_key": SERPAPI_KEY,
        "num": limit
    }
    
    response = requests.get(SERPAPI_URL, params=params)
    return response.json()


def extract_results(data):
    """Extract relevant fields from SerpAPI response"""
    results = []
    
    for item in data.get("organic_results", []):
        result = {
            "title": item.get("title", ""),
            "link": item.get("link", ""),
            "snippet": item.get("snippet", ""),
            "date": item.get("date", ""),
            "subreddit": extract_subreddit(item.get("link", "")),
            "source": item.get("source", ""),
            "position": item.get("position", 0)
        }
        results.append(result)
    
    return results


def extract_subreddit(url):
    """Extract subreddit name from Reddit URL"""
    if "/r/" in url:
        parts = url.split("/r/")[1].split("/")
        return parts[0] if parts else ""
    return ""


def search_person(name, limit=10):
    """Search for a person on Reddit"""
    return search_reddit(f'"{name}"', limit)


def search_in_subreddit(query, subreddit, limit=10):
    """Search within a specific subreddit"""
    return search_reddit(f'site:reddit.com/r/{subreddit} {query}', limit)


def save_results(results, filename):
    """Save results to JSON file"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    out_dir = os.path.join(script_dir, "out")
    os.makedirs(out_dir, exist_ok=True)
    filepath = os.path.join(out_dir, filename)
    with open(filepath, "w") as f:
        json.dump(results, f, indent=2)
    return filepath


def main():
    print("=" * 60)
    print("SerpAPI Google Search for Reddit")
    print("=" * 60)
    
    # Test 1: Search for a person
    print("\n[Test 1] Searching for 'John Cena' on Reddit...")
    raw_response = search_person("John Cena", limit=5)
    results = extract_results(raw_response)
    
    print(f"Found {len(results)} results:\n")
    for r in results:
        print(f"  {r['position']}. {r['title'][:60]}...")
        print(f"     Subreddit: r/{r['subreddit']}")
        print(f"     Date: {r['date']}")
        print(f"     Link: {r['link'][:80]}...")
        print()
    
    # Save raw response
    save_results(raw_response, "serpapi_raw_response.json")
    save_results(results, "serpapi_extracted_results.json")
    
    # Test 2: Search in specific subreddit
    print("\n[Test 2] Searching in r/SquaredCircle...")
    raw_subreddit = search_in_subreddit("John Cena", "SquaredCircle", limit=3)
    subreddit_results = extract_results(raw_subreddit)
    
    print(f"Found {len(subreddit_results)} results in r/SquaredCircle:\n")
    for r in subreddit_results:
        print(f"  {r['position']}. {r['title'][:60]}...")
        print()
    
    save_results(raw_subreddit, "serpapi_subreddit_response.json")
    
    # Show search metadata
    print("\n[Metadata]")
    print(f"  Search engine: Google via SerpAPI")
    print(f"  Credits used: {raw_response.get('search_metadata', {}).get('total_time_taken', 'N/A')}")
    print(f"  Cached: {raw_response.get('search_metadata', {}).get('cached', False)}")
    
    print("\n" + "=" * 60)
    print("Results saved to out/ directory")
    print("=" * 60)


if __name__ == "__main__":
    main()
    main()
