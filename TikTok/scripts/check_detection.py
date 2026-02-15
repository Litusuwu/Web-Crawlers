"""Phase 1: Stealth baseline — test against bot-detection sites (NOT TikTok).

Run stealth-configured browsers against public bot-detection test pages
to verify evasion effectiveness BEFORE attempting TikTok.

Usage:
    uv run python scripts/check_detection.py
"""

from __future__ import annotations

import asyncio
import json

from playwright.async_api import async_playwright
from playwright_stealth_plugin import async_apply
from rich.console import Console
from rich.table import Table

from tiktok_scraper.stealth_config import STEALTH_ARGS, STEALTH_JS_OVERRIDES, VIEWPORT

console = Console()

BOT_TEST_SITES = [
    {
        "name": "SannySoft Bot Test",
        "url": "https://bot.sannysoft.com/",
        "check": "Look for 'missing' or 'inconsistent' in results",
    },
    {
        "name": "Pixelscan",
        "url": "https://pixelscan.net/",
        "check": "Look for 'inconsistent' status",
    },
    {
        "name": "Incolumitas Bot Detection",
        "url": "https://bot.incolumitas.com/",
        "check": "Check detection score",
    },
    {
        "name": "BrowserLeaks WebRTC",
        "url": "https://browserleaks.com/webrtc",
        "check": "Verify no local IP leak",
    },
]


async def test_stealth_on_site(site: dict) -> dict:
    """Test stealth configuration against a single bot-detection site."""
    result = {
        "name": site["name"],
        "url": site["url"],
        "status": "UNKNOWN",
        "details": "",
    }

    async with async_playwright() as pw:
        await async_apply(pw)

        browser = await pw.chromium.launch(
            headless=True,
            args=STEALTH_ARGS,
        )
        context = await browser.new_context(
            viewport=VIEWPORT,
            locale="en-US",
            timezone_id="America/New_York",
        )
        page = await context.new_page()
        await page.add_init_script(STEALTH_JS_OVERRIDES)

        try:
            await page.goto(site["url"], wait_until="networkidle", timeout=30000)
            await asyncio.sleep(5)

            title = await page.title()
            webdriver_check = await page.evaluate("navigator.webdriver")
            plugins_check = await page.evaluate("navigator.plugins.length")
            languages_check = await page.evaluate("JSON.stringify(navigator.languages)")

            details = {
                "page_title": title,
                "navigator.webdriver": webdriver_check,
                "navigator.plugins.length": plugins_check,
                "navigator.languages": json.loads(languages_check),
            }

            if webdriver_check is True:
                result["status"] = "FAIL"
            elif webdriver_check is None or webdriver_check is False:
                result["status"] = "PASS"

            if not webdriver_check:
                result["status"] = "PASS"

            result["details"] = json.dumps(details, indent=2)

        except Exception as e:
            result["status"] = "ERROR"
            result["details"] = str(e)
        finally:
            await browser.close()

    return result


async def main() -> None:
    """Run stealth tests against all bot-detection sites."""
    console.print("\n[bold cyan]Phase 1: Stealth Baseline Tests[/bold cyan]")
    console.print("Testing stealth configuration against bot-detection sites...\n")

    results = []
    for site in BOT_TEST_SITES:
        console.print(f"  Testing: [yellow]{site['name']}[/yellow] ...", end=" ")
        result = await test_stealth_on_site(site)
        status_color = {
            "PASS": "green",
            "FAIL": "red",
            "ERROR": "red",
            "UNKNOWN": "yellow",
        }.get(result["status"], "white")
        console.print(f"[{status_color}]{result['status']}[/{status_color}]")
        results.append(result)

    table = Table(title="Stealth Baseline Results")
    table.add_column("Site", style="cyan")
    table.add_column("Status", justify="center")
    table.add_column("Key Details")

    for r in results:
        status_style = "green" if r["status"] == "PASS" else "red"
        table.add_row(r["name"], f"[{status_style}]{r['status']}[/{status_style}]", r["details"])

    console.print("\n")
    console.print(table)

    passed = sum(1 for r in results if r["status"] == "PASS")
    total = len(results)
    console.print(f"\n[bold]Result: {passed}/{total} passed[/bold]")

    if passed < total:
        console.print(
            "[yellow]WARNING: Stealth is not fully effective. "
            "TikTok scraping will likely fail.[/yellow]"
        )
    else:
        console.print(
            "[green]Stealth baseline passed. Proceed to Phase 2 (TikTok evaluation).[/green]"
        )


if __name__ == "__main__":
    asyncio.run(main())
