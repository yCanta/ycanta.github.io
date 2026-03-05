import asyncio
from playwright.async_api import async_playwright
import os

async def capture():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.set_viewport_size({"width": 1280, "height": 800})
        await page.goto(f'file://{os.getcwd()}/index.html')
        await page.wait_for_timeout(2000)

        icon = page.locator('.icon')
        await icon.screenshot(path='/home/jules/verification/svg_initial_v6.png')

        await page.evaluate("document.querySelector('.icon').style.width = '100px'")
        await page.wait_for_timeout(2000)
        await icon.screenshot(path='/home/jules/verification/svg_collapsed_v6.png')

        await browser.close()

if __name__ == "__main__":
    asyncio.run(capture())
