Do some code with uv using this, searching some names like John Cena principally this experiment is for searching names or people

1 Evaluate the Reddit Data API (OAuth2).

Document: 

    search endpoints (/search, /r/{sub}/search, /users/{username}/submitted, /comments/{post_id}),

    rate limits (~100 queries/min per OAuth client), pricing (free),

    approval process, and 

    data fields returned (title, body, author, timestamp, subreddit, media URLs).

Key finding: the official API is free, well-documented, and fully sufficient for our use case.



2 Test the existing GoogleScraper with site:reddit.com queries via SerpAPI. This requires zero new code and uses the existing SerpAPI subscription.

Document: 

    data coverage (Google index lag means recent posts may be missed, no comment content), and

    viability as an interim solution while the official Reddit API integration is built.

3 Research Node.js/TypeScript tools for the Reddit API:

snoowrap (Node.js) — a full Reddit API wrapper, TypeScript-compatible, production-ready. Perfect fit for the existing stack.

PRAW (Python) — full wrapper but Python-only.

RSS feeds (/r/{subreddit}/new/.rss) — limited, no images.

Pushshift — historical data, API status in flux.

Recommendation: Use snoowrap as the API client.

References:

https://www.npmjs.com/package/snoowrap

4 Evaluate third-party options (for completeness):

    Apify Reddit Scraper (~$5/1,000 items)

    Bright Data Reddit APIs (per-record)

    EnsembleData Reddit API (~$100-200/mo)