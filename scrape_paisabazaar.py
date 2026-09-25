"""
Scrape public personal-loan comparison tables.

Respect robots.txt, terms of use, rate limits, and applicable law.
"""
from pathlib import Path
import pandas as pd
import requests

URL = "https://www.paisabazaar.com/personal-loan/"
OUT = Path("data")
OUT.mkdir(exist_ok=True)
HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; BA-case-study/1.0)"}

def fetch(url):
    r = requests.get(url, headers=HEADERS, timeout=30)
    r.raise_for_status()
    return r.text

if __name__ == "__main__":
    html = fetch(URL)
    (OUT/"paisabazaar_raw.html").write_text(html, encoding="utf-8")
    tables = pd.read_html(html)
    for i, table in enumerate(tables):
        table.to_csv(OUT/f"paisabazaar_table_{i}.csv", index=False)
    print(f"Saved {len(tables)} tables from {URL}")
