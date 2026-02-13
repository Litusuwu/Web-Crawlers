# Reddit API Endpoints - Complete Reference

All endpoint responses saved to `out/` directory.

## ✅ Tested Endpoints (All Working)

### 1. Search All Reddit
**Endpoint:** `GET /search.json`
- **File:** `out/endpoint_search.json` (24 KB)
- **Purpose:** Search across all of Reddit
- **Parameters:**
  - `q` - Search query (e.g., "John Cena")
  - `limit` - Max results (1-100)
  - `sort` - relevance, hot, top, new, comments
  - `t` - Time filter (hour, day, week, month, year, all)
  - `raw_json` - Set to 1 to prevent HTML escaping

**Example:**
```bash
GET https://www.reddit.com/search.json?q=John+Cena&limit=25&sort=relevance
```

### 2. Search Subreddit
**Endpoint:** `GET /r/{subreddit}/search.json`
- **File:** `out/endpoint_r_subreddit_search.json` (18 KB)
- **Purpose:** Search within specific subreddit
- **Parameters:**
  - `q` - Search query
  - `restrict_sr` - Set to "on" to limit to subreddit
  - `limit` - Max results
  - `sort` - Sort method
  - `raw_json` - Set to 1

**Example:**
```bash
GET https://www.reddit.com/r/SquaredCircle/search.json?q=John+Cena&restrict_sr=on
```

### 3. User Submitted Posts
**Endpoint:** `GET /user/{username}/submitted.json`
- **File:** `out/endpoint_user_submitted.json` (77 KB)
- **Purpose:** Get all posts submitted by a user
- **Parameters:**
  - `limit` - Max results
  - `sort` - new, hot, top, controversial
  - `t` - Time filter
  - `raw_json` - Set to 1

**Example:**
```bash
GET https://www.reddit.com/user/spez/submitted.json?limit=25
```

### 4. Post Comments
**Endpoint:** `GET /r/{subreddit}/comments/{post_id}.json`
- **File:** `out/endpoint_comments.json` (14 KB)
- **Purpose:** Get post with complete comment tree
- **Parameters:**
  - `limit` - Max comments
  - `sort` - best, top, new, controversial, old, qa
  - `raw_json` - Set to 1

**Response Structure:** Array of 2 listings
1. First element: Post data
2. Second element: Comments tree

**Example:**
```bash
GET https://www.reddit.com/r/Python/comments/abc123.json
```

### 5. User Information
**Endpoint:** `GET /user/{username}/about.json`
- **File:** `out/endpoint_user_about.json` (2.8 KB)
- **Purpose:** Get user profile information
- **Returns:**
  - username, created_utc
  - comment_karma, link_karma, total_karma
  - is_gold, is_mod, verified
  - icon_img, subreddit (profile info)

**Example:**
```bash
GET https://www.reddit.com/user/spez/about.json
```

### 6. Subreddit Information
**Endpoint:** `GET /r/{subreddit}/about.json`
- **File:** `out/endpoint_subreddit_about.json` (19 KB)
- **Purpose:** Get subreddit metadata
- **Returns:**
  - display_name, title, public_description
  - subscribers, active_user_count
  - created_utc, over18
  - community_icon, banner_img

**Example:**
```bash
GET https://www.reddit.com/r/python/about.json
```

## Additional Endpoints (Not Tested, But Available)

### Subreddit Feeds
```bash
GET /r/{subreddit}/hot.json       # Hot posts
GET /r/{subreddit}/new.json       # New posts
GET /r/{subreddit}/top.json       # Top posts
GET /r/{subreddit}/rising.json    # Rising posts
```

### User Data
```bash
GET /user/{username}/comments.json    # User comments
GET /user/{username}/overview.json    # Combined posts + comments
```

### Post Data
```bash
GET /r/{subreddit}/comments/{id}/{title}.json  # Post with comments
```

## Response Structure

All endpoints return JSON in this format:

```json
{
  "kind": "Listing",
  "data": {
    "modhash": "",
    "dist": 25,
    "after": "t3_xxx",
    "before": null,
    "children": [
      {
        "kind": "t3",  // t3 = link/post, t1 = comment, t2 = user
        "data": {
          // Post/comment/user data here
        }
      }
    ]
  }
}
```

## Image/Media URLs in Responses

Images are returned in multiple fields:

1. **thumbnail** - Small preview (140x78)
   ```json
   "thumbnail": "https://preview.redd.it/xxx.jpg?width=140"
   ```

2. **url** - Direct link
   ```json
   "url": "https://i.redd.it/xyz.jpeg"
   ```

3. **preview** - Multiple resolutions
   ```json
   "preview": {
     "images": [{
       "source": {"url": "...", "width": 4740, "height": 3160},
       "resolutions": [
         {"url": "...", "width": 108, "height": 60},
         {"url": "...", "width": 640, "height": 360}
       ]
     }]
   }
   ```

4. **media** - Videos
   ```json
   "media": {
     "reddit_video": {
       "fallback_url": "https://v.redd.it/xxx.mp4",
       "width": 1920,
       "height": 1080
     }
   }
   ```

5. **media_metadata** - Galleries
   ```json
   "is_gallery": true,
   "media_metadata": {
     "id1": {"s": {"u": "https://preview.redd.it/img1.jpg"}},
     "id2": {"s": {"u": "https://preview.redd.it/img2.jpg"}}
   }
   ```

## Rate Limits

Response headers include rate limit info:

```json
{
  "x-ratelimit-used": "3",
  "x-ratelimit-remaining": "97.0",
  "x-ratelimit-reset": "206"
}
```

## Common Query Parameters

### All Endpoints
- `raw_json=1` - Prevent HTML escaping
- `limit` - Max results (1-100)

### Search Endpoints
- `q` - Query string
- `sort` - relevance, hot, top, new, comments
- `t` - Time filter (hour, day, week, month, year, all)
- `restrict_sr=on` - Limit to subreddit (for /r/{sub}/search)

### Listing Endpoints
- `after` - Pagination cursor (from previous response)
- `before` - Reverse pagination cursor
- `count` - Item count for pagination

## Usage Examples

### Python (requests)
```python
import requests

response = requests.get(
    "https://www.reddit.com/search.json",
    params={"q": "John Cena", "limit": 25, "raw_json": 1},
    headers={"User-Agent": "my-app:v1.0"}
)

data = response.json()
for child in data['data']['children']:
    post = child['data']
    print(f"{post['title']} - {post['score']} points")
```

### cURL
```bash
curl -H "User-Agent: my-app:v1.0" \
  "https://www.reddit.com/search.json?q=John+Cena&limit=25&raw_json=1"
```

## Important Notes

1. **User-Agent Required:** All requests must include a User-Agent header
2. **Rate Limits:** ~100 requests/minute without strict OAuth
3. **Undocumented:** The `.json` endpoints are not officially documented
4. **May Change:** Reddit could disable these anytime
5. **For Production:** Consider OAuth authentication for stability

## Files Generated

Run `make get-endpoints` to generate:

```
Reddit/out/
├── endpoint_search.json              - /search responses
├── endpoint_r_subreddit_search.json  - /r/{sub}/search
├── endpoint_user_submitted.json      - User posts
├── endpoint_comments.json            - Post comments
├── endpoint_user_about.json          - User profile
├── endpoint_subreddit_about.json     - Subreddit info
└── endpoints_summary.json            - Summary
```

## Quick Reference

```bash
# Get all endpoint responses
cd Reddit
make get-endpoints

# View specific endpoint
cat out/endpoint_search.json | jq .

# View summary
cat out/endpoints_summary.json
```

## Related Documentation

- **Report.md** - Complete research report (now in English)
- **README.md** - Main scraper documentation
- **MAKEFILE_GUIDE.md** - Command reference
