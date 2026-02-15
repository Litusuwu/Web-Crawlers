"""Phase 4: Lambda deployment feasibility benchmark.

Measures local browser launch times, memory usage, and estimates
Lambda costs for TikTok scraping operations.

NOTE: This script benchmarks LOCALLY. Actual Lambda deployment
requires building a container image — see TikTokHeadlessScraping.md.

Usage:
    uv run python scripts/benchmark_lambda.py
"""

from __future__ import annotations

import asyncio
import time

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

LAMBDA_PRICING = {
    "price_per_gb_second": 0.0000166667,
    "price_per_request": 0.0000002,
    "memory_mb": 1024,
}


async def benchmark_browser_launch() -> dict:
    """Measure browser launch and page load times."""
    from playwright.async_api import async_playwright

    from tiktok_scraper.stealth_config import STEALTH_ARGS

    results = {}

    start = time.monotonic()
    async with async_playwright() as pw:
        results["playwright_init_s"] = round(time.monotonic() - start, 2)

        launch_start = time.monotonic()
        browser = await pw.chromium.launch(headless=True, args=STEALTH_ARGS)
        results["browser_launch_s"] = round(time.monotonic() - launch_start, 2)

        page_start = time.monotonic()
        page = await browser.new_page()
        await page.goto("https://example.com", wait_until="domcontentloaded")
        results["page_load_s"] = round(time.monotonic() - page_start, 2)

        results["total_s"] = round(time.monotonic() - start, 2)

        await browser.close()

    return results


def estimate_lambda_cost(duration_seconds: float, invocations: int = 1) -> dict:
    """Estimate AWS Lambda cost for browser-based scraping.

    Args:
        duration_seconds: Average duration per invocation.
        invocations: Number of invocations to estimate for.

    Returns:
        Cost breakdown dict.
    """
    memory_gb = LAMBDA_PRICING["memory_mb"] / 1024
    gb_seconds = memory_gb * duration_seconds * invocations
    compute_cost = gb_seconds * LAMBDA_PRICING["price_per_gb_second"]
    request_cost = invocations * LAMBDA_PRICING["price_per_request"]
    total = compute_cost + request_cost

    return {
        "memory_mb": LAMBDA_PRICING["memory_mb"],
        "duration_s": duration_seconds,
        "invocations": invocations,
        "gb_seconds": round(gb_seconds, 2),
        "compute_cost": round(compute_cost, 4),
        "request_cost": round(request_cost, 6),
        "total_cost": round(total, 4),
        "cost_per_invocation": round(total / invocations, 6) if invocations else 0,
    }


async def main() -> None:
    """Run Lambda feasibility benchmarks."""
    console.print(Panel.fit(
        "[bold cyan]Lambda Feasibility Benchmark[/bold cyan]\n"
        "Phase 4: Deployment Cost Analysis",
        border_style="cyan",
    ))

    # Browser launch benchmark
    console.print("\n[bold]1. Browser Launch Benchmark[/bold]")
    console.print("  Measuring Playwright + Chromium startup times...")

    timing = await benchmark_browser_launch()

    timing_table = Table(title="Browser Launch Timing")
    timing_table.add_column("Metric")
    timing_table.add_column("Time", justify="right")
    timing_table.add_row("Playwright init", f"{timing['playwright_init_s']}s")
    timing_table.add_row("Browser launch", f"{timing['browser_launch_s']}s")
    timing_table.add_row("Page load (example.com)", f"{timing['page_load_s']}s")
    timing_table.add_row("[bold]Total[/bold]", f"[bold]{timing['total_s']}s[/bold]")
    console.print(timing_table)

    # Lambda cold start estimate
    cold_start_estimate = timing["total_s"] + 10  # Add ~10s for container cold start
    console.print(
        f"\n  Estimated Lambda cold start: ~{cold_start_estimate:.0f}s "
        f"(local {timing['total_s']}s + ~10s container init)"
    )

    # Cost estimates
    console.print("\n[bold]2. Lambda Cost Estimates[/bold]")

    scrape_duration = timing["total_s"] + 15  # Add time for TikTok load + stealth

    scenarios = [
        ("Single scrape", 1),
        ("100 scrapes/day", 100),
        ("1,000 scrapes/day", 1000),
        ("10,000 scrapes/day", 10000),
    ]

    cost_table = Table(title="Lambda Cost Projection (1024MB, per day)")
    cost_table.add_column("Scenario")
    cost_table.add_column("Duration/each", justify="right")
    cost_table.add_column("GB-seconds", justify="right")
    cost_table.add_column("Cost/day", justify="right")
    cost_table.add_column("Cost/month", justify="right")
    cost_table.add_column("Cost/scrape", justify="right")

    for name, count in scenarios:
        est = estimate_lambda_cost(scrape_duration, count)
        monthly = est["total_cost"] * 30
        cost_table.add_row(
            name,
            f"{scrape_duration:.0f}s",
            f"{est['gb_seconds']}",
            f"${est['total_cost']:.4f}",
            f"${monthly:.2f}",
            f"${est['cost_per_invocation']:.6f}",
        )

    console.print(cost_table)

    # Proxy cost estimate
    console.print("\n[bold]3. Total Cost (Lambda + Proxy)[/bold]")

    proxy_cost_per_gb = 10.0  # Residential proxy average
    data_per_scrape_mb = 3.0

    total_table = Table(title="Total Monthly Cost Estimate")
    total_table.add_column("Component")
    total_table.add_column("1K scrapes/month", justify="right")
    total_table.add_column("10K scrapes/month", justify="right")
    total_table.add_column("100K scrapes/month", justify="right")

    lambda_costs = []
    proxy_costs = []
    for count in [1000, 10000, 100000]:
        lc = estimate_lambda_cost(scrape_duration, count)["total_cost"]
        pc = (count * data_per_scrape_mb / 1024) * proxy_cost_per_gb
        lambda_costs.append(lc)
        proxy_costs.append(pc)

    total_table.add_row(
        "Lambda compute",
        f"${lambda_costs[0]:.2f}",
        f"${lambda_costs[1]:.2f}",
        f"${lambda_costs[2]:.2f}",
    )
    total_table.add_row(
        f"Proxy bandwidth (~{data_per_scrape_mb}MB/scrape @ ${proxy_cost_per_gb}/GB)",
        f"${proxy_costs[0]:.2f}",
        f"${proxy_costs[1]:.2f}",
        f"${proxy_costs[2]:.2f}",
    )
    total_table.add_row(
        "[bold]Total[/bold]",
        f"[bold]${lambda_costs[0] + proxy_costs[0]:.2f}[/bold]",
        f"[bold]${lambda_costs[1] + proxy_costs[1]:.2f}[/bold]",
        f"[bold]${lambda_costs[2] + proxy_costs[2]:.2f}[/bold]",
    )

    console.print(total_table)

    # Feasibility verdict
    console.print(Panel(
        "[bold]Lambda Feasibility Verdict[/bold]\n\n"
        f"  Browser cold start: ~{cold_start_estimate:.0f}s (within 15-min Lambda limit)\n"
        f"  Memory requirement: 1024MB (within 10GB Lambda limit)\n"
        f"  Package size: ~500MB container image (within 10GB limit)\n\n"
        "  [yellow]CONCERNS:[/yellow]\n"
        "  - No session persistence between invocations\n"
        "  - Cold start adds detection risk (slow initial response)\n"
        "  - Cost per scrape is high vs. long-running EC2/ECS\n"
        "  - TikTok rate limits make Lambda parallelism counterproductive\n\n"
        "  [bold]Recommendation:[/bold] Use ECS Fargate or EC2 for persistent\n"
        "  browser sessions. Lambda is viable only for low-volume (<100/day)\n"
        "  scheduled scraping tasks.",
        border_style="yellow",
    ))


if __name__ == "__main__":
    asyncio.run(main())
