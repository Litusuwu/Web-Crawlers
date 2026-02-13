# Makefile for Reddit Scraper
# Run commands easily without typing full uv commands

.PHONY: help test test-verbose lint format check install clean run-examples setup verify

# Default target - show help
help:
	@echo "Reddit Scraper - Available Commands"
	@echo "===================================="
	@echo ""
	@echo "Setup & Installation:"
	@echo "  make install      - Install all dependencies"
	@echo "  make setup        - Copy .env.example to .env (if needed)"
	@echo "  make verify       - Test API connection and setup"
	@echo ""
	@echo "Testing:"
	@echo "  make test         - Run all tests"
	@echo "  make test-verbose - Run tests with verbose output"
	@echo "  make test-cov     - Run tests with coverage report"
	@echo ""
	@echo "Code Quality:"
	@echo "  make lint         - Check code with ruff"
	@echo "  make format       - Format code with ruff"
	@echo "  make check        - Run both lint and tests"
	@echo ""
	@echo "Examples:"
	@echo "  make demo         - Demo without API credentials (mock data)"
	@echo "  make test-public  - Test public API (NO credentials needed!)"
	@echo "  make show-json    - Show JSON request/response examples"
	@echo "  make show-images  - Show image URL extraction"
	@echo "  make get-endpoints - Get all endpoint responses (saved to out/)"
	@echo "  make run-search   - Search for John Cena (requires OAuth)"
	@echo "  make run-user     - Extract user data (requires OAuth)"
	@echo "  make run-subs     - Search multiple subreddits (requires OAuth)"
	@echo "  make run-all      - Run all examples (requires OAuth)"
	@echo ""
	@echo "Cleanup:"
	@echo "  make clean        - Remove cache and temp files"
	@echo "  make clean-all    - Remove cache, temp files, and venv"
	@echo ""

# Installation and setup
install:
	@echo "Installing dependencies with UV..."
	uv sync

setup:
	@if [ ! -f .env ]; then \
		echo "Creating .env from .env.example..."; \
		cp .env.example .env; \
		echo "✓ .env created. Please edit it with your Reddit API credentials."; \
	else \
		echo ".env already exists. Skipping."; \
	fi

verify: setup
	@echo "Verifying setup..."
	uv run python test_setup.py

# Testing
test:
	@echo "Running tests..."
	uv run pytest tests/ -v

test-verbose:
	@echo "Running tests with verbose output..."
	uv run pytest tests/ -vv -s

test-cov:
	@echo "Running tests with coverage..."
	uv run pytest tests/ -v --cov=reddit_scraper --cov-report=html --cov-report=term
	@echo "Coverage report generated in htmlcov/index.html"

test-watch:
	@echo "Running tests in watch mode..."
	uv run pytest tests/ -v --watch

# Code quality
lint:
	@echo "Checking code with ruff..."
	uv run ruff check src/

lint-fix:
	@echo "Fixing code issues with ruff..."
	uv run ruff check src/ --fix

format:
	@echo "Formatting code with ruff..."
	uv run ruff format src/ tests/ examples/

format-check:
	@echo "Checking code formatting..."
	uv run ruff format src/ tests/ examples/ --check

check: lint test
	@echo "✓ All checks passed!"

# Run examples
demo:
	@echo "Running demo without API credentials..."
	uv run python demo_without_api.py

test-public:
	@echo "Testing Reddit public API (no OAuth needed)..."
	uv run python test_public_api.py

show-json:
	@echo "Showing JSON request/response examples..."
	uv run python show_json_examples.py

show-images:
	@echo "Showing image URL extraction examples..."
	uv run python show_image_urls.py

get-endpoints:
	@echo "Getting all endpoint responses..."
	uv run python get_all_endpoints.py

run-search:
	@echo "Running search_by_name.py (John Cena search)..."
	uv run python examples/search_by_name.py

run-user:
	@echo "Running extract_user_data.py..."
	uv run python examples/extract_user_data.py

run-subs:
	@echo "Running search_subreddits.py..."
	uv run python examples/search_subreddits.py

run-all: run-search run-user run-subs
	@echo "✓ All examples completed!"

# Cleanup
clean:
	@echo "Cleaning cache and temp files..."
	@find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	@find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	@find . -type d -name ".ruff_cache" -exec rm -rf {} + 2>/dev/null || true
	@find . -type d -name "htmlcov" -exec rm -rf {} + 2>/dev/null || true
	@find . -type f -name "*.pyc" -delete 2>/dev/null || true
	@find . -type f -name "*.pyo" -delete 2>/dev/null || true
	@find . -type f -name ".coverage" -delete 2>/dev/null || true
	@find . -type f -name "*.json" -not -path "./examples/*" -delete 2>/dev/null || true
	@echo "✓ Cleaned!"

clean-all: clean
	@echo "Removing virtual environment..."
	@rm -rf .venv
	@echo "✓ All cleaned!"

# Development helpers
dev: install verify
	@echo "✓ Development environment ready!"
	@echo ""
	@echo "Quick start:"
	@echo "  make test      - Run tests"
	@echo "  make run-search - Run John Cena search example"

# Quick test specific modules
test-api:
	@echo "Testing API client..."
	uv run pytest tests/test_api_client.py -v

test-scrapers:
	@echo "Testing scrapers..."
	uv run pytest tests/test_scrapers.py -v

# Show project info
info:
	@echo "Reddit Scraper Project Info"
	@echo "==========================="
	@echo "Python version: $$(uv run python --version)"
	@echo "UV version: $$(uv --version)"
	@echo "Project files:"
	@find src/ -name "*.py" | wc -l | xargs echo "  Source files:"
	@find tests/ -name "*.py" | wc -l | xargs echo "  Test files:"
	@find examples/ -name "*.py" | wc -l | xargs echo "  Example files:"
	@echo ""
	@echo "Dependencies:"
	@uv pip list 2>/dev/null | grep -E "praw|pydantic|pytest|ruff" || echo "  (run 'make install' first)"
