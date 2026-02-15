"""Phase 2 & 3: Evaluate stealth approaches against TikTok.

Compares Playwright+stealth, nodriver, and httpx hydration approaches.
Requires proxy configuration in .env for meaningful results.

Usage:
    uv run python scripts/evaluate_stealth.py
"""

from __future__ import annotations

import asyncio
import time

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from tiktok_scraper.config import get_config
from tiktok_scraper.scrapers.hydration_scraper import extract_hydration_data
from tiktok_scraper.scrapers.playwright_scraper import scrape_with_playwright

console = Console()

TEST_URLS = [
    ("TikTok Home (en)", "https://www.tiktok.com/en"),
    ("TikTok Explore", "https://www.tiktok.com/explore"),
    ("TikTok Profile (@tiktok)", "https://www.tiktok.com/@tiktok"),
]


async def evaluate_playwright() -> list[dict]:
    """Test Playwright + stealth against TikTok pages."""
    config = get_config()
    results = []

    for name, url in TEST_URLS:
        console.print(f"  [Playwright] Testing: [yellow]{name}[/yellow] ...", end=" ")
        start = time.monotonic()

        try:
            result = await scrape_with_playwright(url=url, config=config)
            elapsed = time.monotonic() - start

            status = "OK" if result.success else "BLOCKED"
            status_color = "green" if result.success else "red"
            console.print(f"[{status_color}]{status}[/{status_color}] ({elapsed:.1f}s)")

            results.append({
                "approach": "Playwright + stealth",
                "target": name,
                "success": result.success,
                "blocked": result.blocked,
                "captcha": result.captcha,
                "login_wall": result.login_wall,
                "has_hydration": result.hydration_data is not None,
                "status_code": result.response_status,
                "time_s": round(elapsed, 1),
                "signals": result.detection_signals,
                "error": result.error,
            })

        except Exception as e:
            elapsed = time.monotonic() - start
            console.print(f"[red]ERROR[/red] ({elapsed:.1f}s)")
            results.append({
                "approach": "Playwright + stealth",
                "target": name,
                "success": False,
                "error": str(e),
                "time_s": round(elapsed, 1),
            })

    return results


async def evaluate_hydration() -> list[dict]:
    """Test httpx hydration extraction against TikTok profile pages."""
    config = get_config()
    results = []

    hydration_urls = [
        ("Profile (@tiktok)", "https://www.tiktok.com/@tiktok"),
        ("Profile (@charlidamelio)", "https://www.tiktok.com/@charlidamelio"),
    ]

    for name, url in hydration_urls:
        console.print(f"  [httpx] Testing: [yellow]{name}[/yellow] ...", end=" ")
        start = time.monotonic()

        try:
            result = await extract_hydration_data(url=url, config=config)
            elapsed = time.monotonic() - start

            status = "OK" if result.success else "BLOCKED"
            status_color = "green" if result.success else "red"
            console.print(f"[{status_color}]{status}[/{status_color}] ({elapsed:.1f}s)")

            results.append({
                "approach": "httpx hydration",
                "target": name,
                "success": result.success,
                "has_hydration": result.hydration_data is not None,
                "has_user_data": result.user_data is not None,
                "status_code": result.status_code,
                "time_s": round(elapsed, 1),
                "tls_risk": result.tls_fingerprint_risk,
                "error": result.error,
            })

        except Exception as e:
            elapsed = time.monotonic() - start
            console.print(f"[red]ERROR[/red] ({elapsed:.1f}s)")
            results.append({
                "approach": "httpx hydration",
                "target": name,
                "success": False,
                "error": str(e),
                "time_s": round(elapsed, 1),
            })

    return results


async def main() -> None:
    """Run full stealth evaluation comparing all approaches."""
    config = get_config()

    console.print(Panel.fit(
        "[bold cyan]TikTok Headless Scraping Evaluation[/bold cyan]\n"
        "Phase 2: Approach Comparison",
        border_style="cyan",
    ))

    if not config.proxy.is_configured:
        console.print(
            "\n[bold yellow]WARNING:[/bold yellow] No proxy configured in .env\n"
            "Results without a residential proxy are expected to fail.\n"
            "Configure PROXY_URL in .env for meaningful evaluation.\n"
        )

    # Run evaluations
    console.print("\n[bold]1. Playwright + Stealth Plugin[/bold]")
    pw_results = await evaluate_playwright()

    console.print("\n[bold]2. httpx Hydration Extraction[/bold]")
    hydration_results = await evaluate_hydration()

    # Summary table
    all_results = pw_results + hydration_results

    table = Table(title="\nEvaluation Summary")
    table.add_column("Approach", style="cyan")
    table.add_column("Target")
    table.add_column("Success", justify="center")
    table.add_column("Blocked", justify="center")
    table.add_column("CAPTCHA", justify="center")
    table.add_column("Login Wall", justify="center")
    table.add_column("Hydration", justify="center")
    table.add_column("Time", justify="right")
    table.add_column("Notes")

    for r in all_results:
        success = "[green]YES[/green]" if r.get("success") else "[red]NO[/red]"
        blocked = "[red]YES[/red]" if r.get("blocked") else "[green]NO[/green]"
        captcha = "[red]YES[/red]" if r.get("captcha") else "[green]NO[/green]"
        login = "[yellow]YES[/yellow]" if r.get("login_wall") else "[green]NO[/green]"
        hydration = "[green]YES[/green]" if r.get("has_hydration") else "[red]NO[/red]"
        notes = r.get("error", "") or ", ".join(r.get("signals", []))

        table.add_row(
            r.get("approach", ""),
            r.get("target", ""),
            success,
            blocked,
            captcha,
            login,
            hydration,
            f"{r.get('time_s', 0)}s",
            notes[:60],
        )

    console.print(table)

    # Final assessment
    total = len(all_results)
    successes = sum(1 for r in all_results if r.get("success"))
    console.print(f"\n[bold]Overall: {successes}/{total} successful[/bold]")

    if successes == 0:
        console.print(
            "[red bold]All approaches failed.[/red bold] "
            "TikTok's anti-bot measures are blocking all attempts.\n"
            "Recommendations:\n"
            "  1. Verify residential proxy is correctly configured\n"
            "  2. Consider third-party scraping services (Apify, ScrapFly)\n"
            "  3. Re-evaluate whether TikTok scraping is viable for this use case"
        )
    elif successes < total:
        console.print(
            "[yellow]Partial success.[/yellow] Some approaches work but reliability is limited.\n"
            "Proceed to Phase 3 (reliability testing) with the working approach(es)."
        )
    else:
        console.print(
            "[green]All approaches succeeded.[/green] "
            "Proceed to Phase 3 reliability testing and Phase 4 Lambda evaluation."
        )


if __name__ == "__main__":
    asyncio.run(main())
