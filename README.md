# Web-Crawlers Research Repository

Research and evaluation of web scraping capabilities for social media platforms.

## Purpose

This repository documents research into data collection APIs and scraping methods, focusing on:
- API capabilities and limitations
- Rate limits and pricing models
- Authentication and approval processes
- Data structures and available fields
- Legal and practical considerations

## Reddit API Research

**Status:** Research Complete | Implementation Ready

Comprehensive evaluation of Reddit's Data API (OAuth2) with working Python implementation.

### Key Findings

**API Capabilities:**
- Free tier: 100 requests/min per OAuth client
- Well-documented endpoints for search, users, and comments
- Returns complete data fields: title, body, author, timestamp, subreddit, media URLs

**Limitations:**
- Approval process: 1-2+ months with high rejection rate
- Scraping prohibited in terms of service
- Not scalable for high-volume use (100k+ users)

**Implementation:**
```bash
cd Reddit
make install && make setup
make verify
make run-search
```

### Documentation

- **[RedditReport.md](RedditReport.md)** - Complete API research report
- **[Reddit/README.md](Reddit/README.md)** - Implementation guide
- **[Reddit/context/ENDPOINTS.md](Reddit/context/ENDPOINTS.md)** - API reference

### Components

- Python scraper with OAuth2 authentication
- Rate limiter (100 req/min compliance)
- 6 tested endpoints with response examples
- Pydantic data models for validation
- Complete API documentation

## Research Methodology

1. API documentation review
2. Practical endpoint testing
3. Rate limit verification
4. Approval process investigation
5. Alternative solutions analysis
6. Legal considerations review
7. Scalability assessment

## Repository Structure

```
Web-Crawlers/
├── RedditReport.md              # Research findings
├── Reddit/
│   ├── README.md                # Implementation guide
│   ├── context/
│   │   ├── ENDPOINTS.md         # API reference
│   │   └── MAKEFILE_GUIDE.md    # Command reference
│   ├── out/                     # API response examples
│   │   ├── endpoint_*.json      # Full responses
│   │   └── endpoints_summary.json
│   ├── src/reddit_scraper/      # Python implementation
│   └── examples/                # Usage examples
└── Makefile                     # Automation commands
```

## Technical Stack

- Python 3.14+
- UV package manager
- PRAW (Reddit API wrapper)
- Pydantic (data validation)
- pytest (testing)
- Ruff (linting/formatting)

## Installation

```bash
# Install UV
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install Reddit scraper
cd Reddit
make install
```

## Statistics

- Platforms researched: 1 (Reddit)
- API endpoints tested: 6
- Response examples: 7 files (~160 KB)
- Documentation: 4 pages (916+ lines)
- Test coverage: 7 passing tests

## Future Research

- TikTok API evaluation
- Instagram/Facebook API research
- Twitter/X API assessment
- LinkedIn scraping methods
- Cross-platform comparative analysis

## Legal & Ethical Considerations

This research is for educational and evaluation purposes. Users should:
- Review platform Terms of Service before implementation
- Respect rate limits and API guidelines
- Consider ethical implications of data collection
- Be aware of ongoing litigation (e.g., Reddit vs. SerpAPI)
- Obtain proper authorization for commercial use

## License

Research documentation and code examples provided as-is for educational purposes.
