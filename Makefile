# Makefile for Web-Crawlers Repository
# Root-level commands for managing all scraper projects

.PHONY: help test-all clean-all reddit-help reddit-test reddit-setup

# Default target - show help
help:
	@echo "Web-Crawlers - Available Commands"
	@echo "================================="
	@echo ""
	@echo "Repository Commands:"
	@echo "  make test-all     - Run tests for all projects"
	@echo "  make clean-all    - Clean all projects"
	@echo "  make info         - Show repository info"
	@echo ""
	@echo "Reddit Scraper Commands:"
	@echo "  make reddit-help    - Show Reddit scraper commands"
	@echo "  make reddit-test    - Run Reddit scraper tests"
	@echo "  make reddit-setup   - Setup Reddit scraper"
	@echo "  make reddit-verify  - Verify Reddit scraper setup"
	@echo "  make reddit-lint    - Lint Reddit scraper code"
	@echo "  make reddit-format  - Format Reddit scraper code"
	@echo "  make reddit-clean   - Clean Reddit scraper cache"
	@echo ""
	@echo "Quick Examples:"
	@echo "  make reddit-search  - Run John Cena search example"
	@echo "  make reddit-user    - Run user extraction example"
	@echo ""
	@echo "To see more Reddit commands: cd Reddit && make help"
	@echo ""

# Test all projects
test-all:
	@echo "Running tests for all projects..."
	@echo ""
	@echo "=== Reddit Scraper Tests ==="
	@$(MAKE) -C Reddit test
	@echo ""
	@echo "✓ All project tests completed!"

# Clean all projects
clean-all:
	@echo "Cleaning all projects..."
	@$(MAKE) -C Reddit clean
	@echo "✓ All projects cleaned!"

# Repository info
info:
	@echo "Web-Crawlers Repository"
	@echo "======================"
	@echo ""
	@echo "Projects:"
	@echo "  - Reddit (Python/UV) - Reddit scraper with OAuth2"
	@echo ""
	@echo "Structure:"
	@tree -L 2 -I '.venv|__pycache__|*.pyc|.pytest_cache|uv.lock|.git' . 2>/dev/null || find . -maxdepth 2 -type d | grep -v -E '\./\.git|\.venv|__pycache__' | head -20
	@echo ""

# Reddit-specific commands (delegate to Reddit/Makefile)
reddit-help:
	@$(MAKE) -C Reddit help

reddit-test:
	@$(MAKE) -C Reddit test

reddit-setup:
	@$(MAKE) -C Reddit setup

reddit-verify:
	@$(MAKE) -C Reddit verify

reddit-lint:
	@$(MAKE) -C Reddit lint

reddit-format:
	@$(MAKE) -C Reddit format

reddit-clean:
	@$(MAKE) -C Reddit clean

reddit-search:
	@$(MAKE) -C Reddit run-search

reddit-user:
	@$(MAKE) -C Reddit run-user

reddit-check:
	@$(MAKE) -C Reddit check

# Quick development setup for Reddit
reddit-dev:
	@$(MAKE) -C Reddit dev

# Show git status
status:
	@echo "Git Status:"
	@echo "==========="
	@git status -s || echo "Not a git repository"
	@echo ""
	@echo "Untracked files in Reddit/:"
	@cd Reddit && git status -s | grep "^??" || echo "None"
