# Nike Shoes Scraper 👟

A Python scraper built with Scrapy framework that extracts Nike women's shoes information from academy.com.

## Features

The scraper extracts the following information about shoes:
- Product name
- Price
- Default color
- All available colors
- Number of reviews
- Average review score

## Technical Details

### Requirements
- Python 3.x
- Scrapy 2.12.0

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Rummiev/scraper.git
cd task
```

2. Create a virtual environment:
```bash
python -m venv venv

source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate  # For Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### How to Run the Scraper

```bash
scrapy crawl nike
```

To save results to a file:
```bash
scrapy crawl nike -o results.json
```

## Project Structure

```
task/
├── scrapy.cfg
├── requirements.txt
└── task/
    ├── __init__.py
    ├── items.py
    ├── middlewares.py
    ├── pipelines.py
    ├── settings.py
    └── spiders/
        └── nike_spider.py
```

## Settings

- Project respects robots.txt rules (ROBOTSTXT_OBEY = True)
- Uses AsyncioSelectorReactor
- Encoding is set to UTF-8

