# 📘 Book Scraper CLI — Python Automation Engineer Take-Home

A modular web scraper built with **Playwright** that extracts product data from [books.toscrape.com](https://books.toscrape.com), simulates human browsing behavior, and saves the results in your chosen format.

---

## 🎯 Features

- ✅ Asynchronous scraping with Playwright
- ✅ CLI support with customizable options
- ✅ Human-like behavior: random delays, user-agent rotation
- ✅ Reuses browser sessions/cookies
- ✅ Supports saving to JSON, CSV, or SQLite (via SQLAlchemy)
- ✅ Graceful error handling and retry logic
- ✅ Modular, testable, and scalable code structure

---

## 🛠️ Setup

```bash
# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Install browser binaries for Playwright
playwright install
```

---

## 🚀 Usage

Run the CLI tool with desired options:

```bash
python scraper/cli.py --max-pages 3 --output-format csv --headless --reuse-session
```

### CLI Options

| Argument         | Description                                         | Default    |
|------------------|-----------------------------------------------------|------------|
| `--max-pages`    | Max number of pages to scrape                       | `3`        |
| `--output-format`| Output type: `json`, `csv`, or `sqlite`             | `json`     |
| `--headless`     | Run browser in headless mode                        | `True`     |
| `--reuse-session`| Reuse cookies/session state from previous run       | `False`    |

---

## 📂 Project Structure

```
scraper/
├── cli.py           # CLI interface and entry point
├── scraper.py       # Core scraping logic
├── storage.py       # Save to JSON, CSV, or SQLite
├── utils.py         # Helpers (delays, star rating parsing)
├── config.py        # Constants like BASE_URL, user-agents
├── parsers.py       # Rating parser from CSS classes
requirements.txt
README.md
output.json / output.csv / books.db
```

---

## 📦 Sample Outputs

- `output_20250624_1450.json`
- `output_20250624_1451.csv`
- `books_20250624_1452.db`

---

## 🧪 Running Tests

```bash
pytest tests/
```

## 🧪 Optional Enhancements (Not Implemented)

- Dockerfile for containerized execution
- Proxy rotation (e.g., ProxyMesh)

---


## 🧑‍💻 Author

**NAME: Ayomide Adu**  
**EMAIL: techai.innovator@gmail.com**
**GITHUB: https://github.com/techai-innovator**
