# Reddit Scraper

A Python package for scraping Reddit data using the official Reddit API with OAuth2 authentication and automatic rate limiting.

## 🚀 Quick Start (3 Steps)

### 1. Get Reddit API Credentials

1. Go to https://www.reddit.com/prefs/apps
2. Click **"Create App"** → Select **"script"**
3. Set redirect uri: `http://localhost:8080`
4. Copy your **client_id** and **client_secret**

### 2. Setup

```bash
cd Reddit
make install          # Install dependencies
make setup            # Create .env file
nano .env             # Add your credentials
```

Edit `.env`:
```env
REDDIT_CLIENT_ID=your_client_id_here
REDDIT_CLIENT_SECRET=your_client_secret_here
```

### 3. Run

```bash
make verify           # Test connection
make test             # Run tests
make run-search       # Search for "John Cena"
```

Done! Results saved to `john_cena_results.json`

---

## 📋 Common Commands (Makefile)

```bash
# Testing
make test             # Run all tests
make test-verbose     # Verbose output
make lint             # Check code quality

# Run Examples  
make run-search       # Search for "John Cena"
make run-user         # Extract user data
make run-all          # Run all examples

# Development
make check            # Lint + tests (use before commits!)
make format           # Format code
make clean            # Clean cache files

# Help
make help             # Show all commands
```

---

## 💻 Basic Usage

### Search for People/Names

```python
from reddit_scraper import RedditAPIClient, SearchScraper

# Initialize
client = RedditAPIClient()
scraper = SearchScraper(client)

# Search for mentions of a person
results = scraper.search_all(
    query="John Cena",
    limit=50
)

# Use results
for post in results:
    print(f"{post.title} - r/{post.subreddit}")
    print(f"Score: {post.score} | Comments: {post.num_comments}")
```

### Search Specific Subreddits

```python
# Search in specific communities
results = scraper.search_subreddit(
    subreddit="SquaredCircle",
    query="John Cena",
    limit=50,
    sort="top",
    time_filter="month"
)
```

### Get User Data

```python
from reddit_scraper import UserScraper

scraper = UserScraper(client)

# Get profile
user = scraper.get_user_profile("username")
print(f"Karma: {user.comment_karma + user.link_karma}")

# Get submissions
posts = scraper.get_user_submissions("username", limit=20)
```

### Export to JSON

```python
import json

with open('results.json', 'w') as f:
    json.dump(
        [post.model_dump(mode='json') for post in results],
        f,
        indent=2
    )
```

---

## 🎯 Features

- ✅ Search entire Reddit or specific subreddits
- ✅ Search for people/names (optimized for "John Cena" use case)
- ✅ Extract user profiles and submissions
- ✅ Get comment threads
- ✅ Extract media URLs (images, videos, galleries)
- ✅ OAuth2 authentication
- ✅ Automatic rate limiting (100 requests/min)
- ✅ Structured data models (Pydantic)
- ✅ Free (official Reddit API)

## 📚 Documentation

- **[ENDPOINTS.md](ENDPOINTS.md)** - Complete reference for all Reddit API endpoints
- **[Report.md](../Report.md)** - Research report on Reddit API (English)
- **[.env.example](.env.example)** - Example environment configuration

Run `make help` to see all available commands.

---

## 📦 Installation

### Requirements

- Python 3.14+
- [UV package manager](https://github.com/astral-sh/uv)

### Install UV

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Install Project

```bash
cd Reddit
make install      # or: uv sync
```

---

## 📚 API Reference

### RedditAPIClient

```python
from reddit_scraper import RedditAPIClient

client = RedditAPIClient()  # Loads from .env

# Check connection
client.test_connection()

# Check rate limit
client.get_remaining_requests()  # Returns 0-100
```

### SearchScraper

```python
from reddit_scraper import SearchScraper

scraper = SearchScraper(client)

# Search all Reddit
posts = scraper.search_all(
    query="search term",
    limit=100,
    sort='relevance',  # 'relevance', 'hot', 'top', 'new'
    time_filter='all'  # 'all', 'day', 'week', 'month', 'year'
)

# Search specific subreddit
posts = scraper.search_subreddit(
    subreddit="python",
    query="search term",
    limit=100
)

# Search by author
posts = scraper.search_by_author("username", limit=100)

# Search for mentions (optimized for people/names)
posts = scraper.search_mentions(
    name="John Cena",
    limit=100,
    subreddits=["SquaredCircle", "WWE"]  # Optional
)
```

### UserScraper

```python
from reddit_scraper import UserScraper

scraper = UserScraper(client)

# Get profile
user = scraper.get_user_profile("username")

# Get submissions
posts = scraper.get_user_submissions("username", limit=50)

# Check if exists
exists = scraper.user_exists("username")
```

### CommentScraper

```python
from reddit_scraper import CommentScraper

scraper = CommentScraper(client)

# Get post comments
comments = scraper.get_post_comments(
    post_id="abc123",
    sort='best'  # 'best', 'top', 'new', 'controversial'
)

# Get comment by ID
comment = scraper.get_comment_by_id("def456")

# Get user comments
comments = scraper.get_user_comments("username", limit=50)
```

---

## 📊 Data Models

### RedditPost
```python
{
    "id": str,
    "title": str,
    "body": str | None,
    "author": str,
    "timestamp": datetime,
    "subreddit": str,
    "url": str,
    "score": int,
    "num_comments": int,
    "media_urls": list[str],
    "permalink": str,
    "is_self": bool,
    "link_flair_text": str | None
}
```

### RedditComment
```python
{
    "id": str,
    "body": str,
    "author": str,
    "timestamp": datetime,
    "score": int,
    "parent_id": str,
    "post_id": str,
    "permalink": str,
    "is_submitter": bool
}
```

### RedditUser
```python
{
    "username": str,
    "created_utc": datetime,
    "comment_karma": int,
    "link_karma": int,
    "is_gold": bool,
    "is_mod": bool,
    "verified": bool
}
```

---

## 🧪 Testing

```bash
# Run all tests
make test

# Verbose output
make test-verbose

# With coverage
make test-cov

# Specific tests
make test-api         # API client tests
make test-scrapers    # Scraper tests
```

All 7 tests passing ✅

---

## 🛠️ Development

### Code Quality

```bash
make lint             # Check code
make lint-fix         # Auto-fix issues
make format           # Format code
make check            # Lint + tests (pre-commit)
```

### Project Structure

```
Reddit/
├── src/reddit_scraper/
│   ├── api_client.py          # OAuth2 client
│   ├── models.py              # Data models
│   ├── rate_limiter.py        # Rate limiting
│   ├── utils.py               # Helpers
│   └── scrapers/
│       ├── search.py          # Search functionality
│       ├── user.py            # User data
│       └── comments.py        # Comments
├── examples/
│   ├── search_by_name.py      # John Cena search
│   ├── extract_user_data.py   # User extraction
│   └── search_subreddits.py   # Multi-subreddit
├── tests/                     # Test suite
├── pyproject.toml             # UV config
└── Makefile                   # Commands
```

---

## 💡 Examples

### Example 1: Search for a Celebrity

```python
from reddit_scraper import RedditAPIClient, SearchScraper

client = RedditAPIClient()
scraper = SearchScraper(client)

# Search for John Cena
results = scraper.search_mentions("John Cena", limit=100)

# Print results
for post in results:
    print(f"Title: {post.title}")
    print(f"Subreddit: r/{post.subreddit}")
    print(f"Score: {post.score}")
    print()
```

Run: `make run-search`

### Example 2: Monitor Subreddit

```python
# Get posts from specific subreddit
results = scraper.search_subreddit(
    subreddit="python",
    query="web scraping",
    time_filter="week",
    sort="top"
)

# Filter by score
popular = [p for p in results if p.score > 100]
```

### Example 3: Analyze User Activity

```python
from reddit_scraper import UserScraper

scraper = UserScraper(client)

# Get user info
user = scraper.get_user_profile("spez")
posts = scraper.get_user_submissions("spez", limit=50)

# Calculate average score
avg_score = sum(p.score for p in posts) / len(posts)
print(f"Average score: {avg_score}")
```

Run: `make run-user`

### Example 4: Multi-Subreddit Search

```python
# Search across multiple subreddits
subreddits = ["SquaredCircle", "WWE", "prowrestling"]

for sub in subreddits:
    results = scraper.search_subreddit(
        subreddit=sub,
        query="John Cena",
        limit=10
    )
    print(f"r/{sub}: {len(results)} posts")
```

Run: `make run-subs`

---

## 🔧 Troubleshooting

### "Failed to connect to Reddit API"

✅ **Solution:**
- Check your `.env` file has correct credentials
- Verify `REDDIT_CLIENT_ID` and `REDDIT_CLIENT_SECRET` are set
- Make sure no extra spaces in the values
- Test: `make verify`

### "No module named reddit_scraper"

✅ **Solution:**
```bash
make install          # Reinstall dependencies
# Always use: make test (not just pytest)
```

### Rate limit errors

✅ **Solution:**
- The scraper handles rate limits automatically
- Check remaining: `client.get_remaining_requests()`
- Max: 100 requests per minute
- Wait 60 seconds if needed

### Tests failing

✅ **Solution:**
```bash
make clean            # Clean cache
make install          # Reinstall
make test             # Try again
```

### Linting errors

✅ **Solution:**
```bash
make lint-fix         # Auto-fix
make format           # Format code
```

---

## ⚡ Rate Limits

- **Limit:** 100 requests per minute per OAuth client
- **Free:** Official Reddit API is completely free
- **Automatic:** Rate limiting is handled automatically
- **Check:** `client.get_remaining_requests()`

---

## 🤝 Contributing

```bash
# Setup dev environment
make install

# Make changes
# ...

# Test before committing
make check            # Runs lint + tests
make format           # Format code

# Clean up
make clean
```

---

## 📝 Dependencies

- **praw** - Reddit API wrapper
- **pydantic** - Data validation
- **python-dotenv** - Environment management
- **pytest** - Testing
- **ruff** - Linting/formatting

---

## 📄 License

MIT License

---

## 🎉 Summary

This Reddit scraper is:
- ✅ **Simple** - Easy to install and use
- ✅ **Free** - No API costs
- ✅ **Fast** - Automatic rate limiting
- ✅ **Complete** - All features implemented
- ✅ **Tested** - 7 tests, all passing
- ✅ **Documented** - Clear examples and API reference

**Perfect for searching Reddit for people, topics, and data!**

---

## 🔗 Quick Links

- **Get Started:** `make install && make setup && make verify`
- **Run Example:** `make run-search`
- **See Commands:** `make help`
- **Test Setup:** `make test`
- **Get Credentials:** https://www.reddit.com/prefs/apps

**Need help?** Run `make help` or check the examples in `examples/`
