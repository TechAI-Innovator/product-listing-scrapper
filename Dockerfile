# Use official Python image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system dependencies for Playwright
RUN apt-get update && \
    apt-get install -y wget curl gnupg ca-certificates && \
    apt-get install -y libnss3 libatk1.0-0 libatk-bridge2.0-0 libxcomposite1 libxdamage1 libxrandr2 libgbm1 libxshmfence1 libasound2 libx11-xcb1 && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Install Playwright and its browsers
RUN playwright install --with-deps

# Copy source code
COPY . .

# Default command
CMD ["python", "scraper/cli.py", "--max-pages", "3", "--output-format", "json", "--headless"]
