# Makefile Quick Reference

This project includes Makefiles to simplify common development tasks.

## 📍 Location

- **Root Makefile**: `/Web-Crawlers/Makefile` - Repository-level commands
- **Reddit Makefile**: `/Web-Crawlers/Reddit/Makefile` - Reddit scraper commands

## 🚀 Quick Start Commands

### From Repository Root (`Web-Crawlers/`)

```bash
# Show all available commands
make help

# Run all tests
make test-all

# Run Reddit scraper tests
make reddit-test

# Setup Reddit scraper
make reddit-setup

# Clean all projects
make clean-all

# Run examples
make reddit-search    # Search for John Cena
make reddit-user      # Extract user data
```

### From Reddit Directory (`Web-Crawlers/Reddit/`)

```bash
# Show all available commands
make help

# Setup & Installation
make install          # Install all dependencies
make setup            # Create .env from template
make verify           # Test API connection

# Testing
make test             # Run all tests
make test-verbose     # Run tests with verbose output
make test-cov         # Run tests with coverage report
make test-api         # Test only API client
make test-scrapers    # Test only scrapers

# Code Quality
make lint             # Check code with ruff
make lint-fix         # Auto-fix linting issues
make format           # Format code with ruff
make check            # Run lint + tests

# Run Examples
make run-search       # Search for John Cena
make run-user         # Extract user data
make run-subs         # Search multiple subreddits
make run-all          # Run all examples

# Cleanup
make clean            # Remove cache and temp files
make clean-all        # Remove cache, temp, and venv

# Development
make dev              # Setup complete dev environment
make info             # Show project information
```

## 📋 Common Workflows

### Initial Setup

```bash
# 1. Install dependencies and setup environment
cd Reddit
make install
make setup

# 2. Edit .env with your Reddit API credentials
nano .env

# 3. Verify setup
make verify
```

### Development Workflow

```bash
cd Reddit

# Run tests frequently
make test

# Check code quality before committing
make check

# Format code
make format

# Clean up when needed
make clean
```

### Testing Workflow

```bash
cd Reddit

# Quick test
make test

# Detailed test output
make test-verbose

# Test with coverage
make test-cov

# Test specific modules
make test-api
make test-scrapers
```

### Running Examples

```bash
cd Reddit

# Run individual examples
make run-search    # John Cena search
make run-user      # User extraction
make run-subs      # Multi-subreddit search

# Or run all at once
make run-all
```

## 🎯 Most Used Commands

### Daily Development
```bash
make test          # ← Most used: Run tests
make lint-fix      # Fix code issues
make format        # Format code
make check         # Lint + test combo
```

### Running Code
```bash
make run-search    # Run main example
make verify        # Test API connection
make info          # Show project info
```

### Cleanup
```bash
make clean         # Quick cleanup
make clean-all     # Full cleanup
```

## 💡 Tips

1. **Always from the right directory**: 
   - Repository-level commands: run from `Web-Crawlers/`
   - Reddit commands: run from `Web-Crawlers/Reddit/`

2. **Check help anytime**: 
   ```bash
   make help
   ```

3. **Chain commands**:
   ```bash
   make clean && make test && make run-search
   ```

4. **Use `make check` before committing**:
   ```bash
   make check  # Runs lint + tests
   ```

5. **Tab completion works**: Type `make ` then press Tab to see options

## 🔍 Troubleshooting

### "make: command not found"
- Install `make`: `sudo dnf install make` (Fedora) or `sudo apt install make` (Ubuntu)

### "uv: command not found"
- UV is installed to `~/.local/bin/uv`
- The Makefiles use full path: `/home/litus/.local/bin/uv`
- Or add to PATH: `export PATH="$HOME/.local/bin:$PATH"`

### Tests failing
```bash
make clean        # Clean cache
make install      # Reinstall dependencies
make test         # Try again
```

### Linting errors
```bash
make lint-fix     # Auto-fix most issues
make format       # Format code
make lint         # Check again
```

## 📚 Examples

### Complete Setup from Scratch
```bash
# From Web-Crawlers directory
cd Reddit
make install
make setup
# Edit .env file
make verify
make test
make run-search
```

### Before Git Commit
```bash
cd Reddit
make format       # Format code
make check        # Lint + test
make clean        # Clean temp files
```

### Run All Examples
```bash
cd Reddit
make run-all      # Runs all 3 examples
```

### Full Cleanup
```bash
cd Reddit
make clean-all    # Removes everything including venv
make install      # Reinstall fresh
```

## 🎨 Makefile Targets Summary

### Setup Targets
- `install` - Install dependencies
- `setup` - Create .env
- `verify` - Test connection
- `dev` - Full dev setup

### Test Targets
- `test` - Run all tests
- `test-verbose` - Verbose test output
- `test-cov` - Tests with coverage
- `test-api` - Test API client only
- `test-scrapers` - Test scrapers only

### Quality Targets
- `lint` - Check code
- `lint-fix` - Fix issues
- `format` - Format code
- `format-check` - Check formatting
- `check` - Lint + tests

### Run Targets
- `run-search` - John Cena search
- `run-user` - User extraction
- `run-subs` - Multi-subreddit
- `run-all` - All examples

### Utility Targets
- `clean` - Clean cache
- `clean-all` - Full cleanup
- `info` - Project info
- `help` - Show help

## 🔗 Related Files

- `Reddit/Makefile` - Reddit scraper Makefile
- `Makefile` - Root repository Makefile
- `Reddit/pyproject.toml` - Project configuration
- `Reddit/.env` - Your credentials (gitignored)

---

**Pro Tip**: Bookmark this file and run `make help` often!
