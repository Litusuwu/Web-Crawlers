# Web-Crawlers

Collection of web scrapers and crawlers for various platforms.

## 🔴 Reddit Scraper

**Status:** ✅ Complete and production-ready

Python-based Reddit scraper using the official Reddit API with OAuth2 authentication.

**Quick Start:**
```bash
cd Reddit
make install && make setup
# Edit .env with your Reddit API credentials
make verify
make run-search
```

**[➜ Full Documentation](Reddit/README.md)**

### Features
- Search Reddit posts, users, and comments
- OAuth2 authentication with automatic rate limiting
- Optimized for searching people/names
- Export to JSON
- Free to use

### Quick Commands
```bash
cd Reddit
make help           # Show all commands
make test           # Run tests
make run-search     # Search for "John Cena"
make run-user       # Extract user data
```

---

## 📚 Documentation

- **[Reddit/README.md](Reddit/README.md)** - Complete guide
- **[Makefile](Makefile)** - Available commands

---

## 🚀 Coming Soon

- TikTok scraper
- Additional platforms

---

## Requirements

- Python 3.14+
- [UV package manager](https://github.com/astral-sh/uv)

Install UV:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```
