# CLI interface

import argparse
import asyncio
from scraper import scrape_books
from storage import save_data

def parse_args():
    parser = argparse.ArgumentParser(description="📘 Book Scraper CLI")

    parser.add_argument("--max-pages", type=int, default=3, help="Maximum number of pages to scrape (default: 3)")
    parser.add_argument("--output-format", type=str, default="json", choices=["json", "csv", "sqlite"], help="Format to store scraped data (default: json)")
    parser.add_argument("--headless", action="store_true", help="Run browser in headless mode")
    parser.add_argument("--reuse-session", action="store_true", help="Reuse session/cookies from previous run")

    return parser.parse_args()


async def main():
    args = parse_args()
    books = await scrape_books(
        max_pages=args.max_pages,
        headless=args.headless,
        reuse_session=args.reuse_session
    )
    save_data(books, args.output_format)

if __name__ == "__main__":
    asyncio.run(main())