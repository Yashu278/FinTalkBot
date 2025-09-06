# Fetch stock data
import yfinance as yf
import requests
from bs4 import BeautifulSoup
from src import config
from typing import List

def get_stock_price(ticker: str) -> float | None:
    try:
        stock = yf.Ticker(ticker)
        hist = stock.history(period="1d")
        if hist.empty:
            return None
        return float(hist['Close'].iloc[-1])
    except Exception:
        return None

def get_finance_news(query: str | None = None) -> List[str]:
    search_term = query or config.NEWS_QUERY
    url = f"https://news.google.com/search?q={search_term}"
    try:
        response = requests.get(
            url,
            headers={"User-Agent": config.USER_AGENT},
            timeout=config.REQUEST_TIMEOUT_SECS,
        )
        response.raise_for_status()
    except Exception:
        return []

    try:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Class names change; fallback to headlines via <h3> tags as well
        anchors = soup.find_all("a", {"class": "JtKRv"})
        headlines = [a.get_text(strip=True) for a in anchors if a.get_text(strip=True)]
        if not headlines:
            h3s = soup.find_all("h3")
            headlines = [h.get_text(strip=True) for h in h3s if h.get_text(strip=True)]
        # Deduplicate and limit
        unique = []
        seen = set()
        for h in headlines:
            if h not in seen:
                seen.add(h)
                unique.append(h)
        return unique[:5]
    except Exception:
        return []
