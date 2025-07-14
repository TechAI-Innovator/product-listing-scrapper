# Main scraping logic

# Importing dependencies
import os
import asyncio
import random
from urllib.parse import urljoin
from playwright.async_api import async_playwright
from utils import random_delay
from parsers import get_star_rating
from config import USER_AGENTS, BASE_URL

async def scrape_page(page, url):
    await page.goto(url)
    await random_delay()

    books = await page.query_selector_all(".product_pod")
    data = []

    if not books:
        print(f"[!] No products found at {url}")
        return []

    for book in books:
        a_tag = await book.query_selector("h3 > a")
        title = await a_tag.get_attribute("title")
        href = await a_tag.get_attribute("href")

        price_el = await book.query_selector(".price_color")
        price = await price_el.text_content() if price_el else "N/A"

        rating_el = await book.query_selector("p.star-rating")
        rating_class = await rating_el.get_attribute("class") if rating_el else ""  # e.g., "product_pod star-rating Three"
        rating = get_star_rating(rating_class)

        full_url = urljoin(BASE_URL, href)

        data.append({
            "title": title.strip(),
            "price": price.strip(),
            "rating": rating,
            "detail_url": full_url,
        })

    return data


async def retry_scrape(page, url, retries=3):
    for attempt in range(retries):
        try:
            return await scrape_page(page, url)
        except Exception as e:
            print(f"[!] Error on attempt {attempt+1} for {url}: {e}")
            await random_delay()
    return []


async def scrape_books(max_pages=3, headless=True, reuse_session=False):
    all_books = []
    session_path = "session.json"

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=headless)
        user_agent = random.choice(USER_AGENTS)

        if reuse_session and os.path.exists(session_path):
            context = await browser.new_context(storage_state=session_path)
            print("[*] Loaded session from session.json")
        else:
            context = await browser.new_context(user_agent=user_agent)
            print("[*] Started new session with UA:", user_agent)

        # ✅ Create a page per task
        tasks = []
        for i in range(1, max_pages + 1):
            page = await context.new_page()
            url = f"{BASE_URL}catalogue/page-{i}.html" if i > 1 else BASE_URL
            tasks.append(retry_scrape(page, url))

        results = await asyncio.gather(*tasks)

        # Flatten nested results
        all_books = [book for result in results for book in result]

        await context.storage_state(path=session_path)
        print("[*] Session saved to session.json")
        await browser.close()

    return all_books
