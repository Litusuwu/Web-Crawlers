"""Human-like behavioral simulation for headless browsers.

TikTok tracks mouse movement, scroll cadence, click timing, and dwell time.
This module generates realistic interaction patterns to reduce detection.
"""

import asyncio
import random


async def human_delay(min_seconds: float = 1.0, max_seconds: float = 3.0) -> None:
    """Sleep for a random human-like duration."""
    delay = random.uniform(min_seconds, max_seconds)
    await asyncio.sleep(delay)


async def simulate_scroll(page, scrolls: int = 3) -> None:
    """Simulate human-like scrolling with variable speed and pauses.

    Args:
        page: Playwright page object.
        scrolls: Number of scroll actions to perform.
    """
    for _i in range(scrolls):
        scroll_distance = random.randint(300, 800)
        scroll_duration = random.uniform(0.5, 1.5)

        await page.evaluate(
            f"""
            new Promise((resolve) => {{
                const distance = {scroll_distance};
                const duration = {scroll_duration * 1000};
                const start = performance.now();
                const startY = window.scrollY;

                function step(timestamp) {{
                    const elapsed = timestamp - start;
                    const progress = Math.min(elapsed / duration, 1);
                    // Ease-in-out cubic
                    const ease = progress < 0.5
                        ? 4 * progress * progress * progress
                        : 1 - Math.pow(-2 * progress + 2, 3) / 2;
                    window.scrollTo(0, startY + distance * ease);
                    if (progress < 1) {{
                        requestAnimationFrame(step);
                    }} else {{
                        resolve();
                    }}
                }}
                requestAnimationFrame(step);
            }})
            """
        )

        dwell = random.uniform(2.0, 6.0)
        await asyncio.sleep(dwell)

        if random.random() < 0.2:
            small_scroll_back = random.randint(50, 150)
            await page.evaluate(f"window.scrollBy(0, -{small_scroll_back})")
            await asyncio.sleep(random.uniform(0.5, 1.0))


async def simulate_mouse_movement(page, target_x: int, target_y: int) -> None:
    """Move mouse to target with a Bezier-like curve (not linear).

    Args:
        page: Playwright page object.
        target_x: Target X coordinate.
        target_y: Target Y coordinate.
    """
    steps = random.randint(15, 30)
    current = await page.evaluate("({x: 0, y: 0})")
    start_x, start_y = current.get("x", 0), current.get("y", 0)

    ctrl_x = start_x + random.randint(-100, 100)
    ctrl_y = start_y + random.randint(-50, 50)

    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * start_x + 2 * (1 - t) * t * ctrl_x + t**2 * target_x
        y = (1 - t) ** 2 * start_y + 2 * (1 - t) * t * ctrl_y + t**2 * target_y
        await page.mouse.move(x, y)
        await asyncio.sleep(random.uniform(0.01, 0.04))


async def random_viewport_interaction(page) -> None:
    """Perform random small interactions to appear human.

    Occasionally moves mouse, hovers over elements, or adjusts scroll
    to simulate idle browsing behavior.
    """
    action = random.choice(["mouse_move", "small_scroll", "idle"])

    if action == "mouse_move":
        x = random.randint(100, 1800)
        y = random.randint(100, 900)
        await simulate_mouse_movement(page, x, y)
    elif action == "small_scroll":
        delta = random.randint(-100, 100)
        await page.evaluate(f"window.scrollBy(0, {delta})")
    else:
        await asyncio.sleep(random.uniform(1.0, 3.0))
