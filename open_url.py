import asyncio
import sys

from playwright.async_api import async_playwright

DEFAULT_URL = "https://example.com"
WAIT_SECONDS = 30


async def main() -> None:
    url = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_URL

    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=True)
        try:
            page = await browser.new_page()
            await page.goto(url, wait_until="domcontentloaded")
            print(f"Navegando a: {url}")
            await asyncio.sleep(WAIT_SECONDS)
        finally:
            await browser.close()


if __name__ == "__main__":
    asyncio.run(main())