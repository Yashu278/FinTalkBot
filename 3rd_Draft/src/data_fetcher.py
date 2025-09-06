# Fetch stock data
import yfinance as yf
import requests
from bs4 import BeautifulSoup
from src import config
from typing import List, Tuple, Optional
import io
import base64
import matplotlib

# Use a non-interactive backend suitable for servers
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

def get_stock_price(ticker: str) -> float | None:
    try:
        stock = yf.Ticker(ticker)
        hist = stock.history(period="1d")
        if hist.empty:
            return None
        return float(hist['Close'].iloc[-1])
    except Exception:
        return None


def get_price_details(ticker: str) -> Optional[Tuple[float, Optional[str], Optional[float]]]:
    """
    Return (price, currency, change_percent_today) or None on failure.
    """
    try:
        stock = yf.Ticker(ticker)
        info = stock.fast_info if hasattr(stock, "fast_info") else {}
        price = None
        currency = None
        change_percent = None

        # Current price
        try:
            price = float(info["last_price"]) if "last_price" in info else None
        except Exception:
            price = None

        # Fallback via history
        if price is None:
            hist = stock.history(period="1d")
            if not hist.empty:
                price = float(hist['Close'].iloc[-1])

        # Currency
        try:
            currency = info.get("currency")
        except Exception:
            currency = None

        # Percent change today
        try:
            prev_close = float(info["previous_close"]) if "previous_close" in info else None
            if prev_close and price is not None and prev_close != 0:
                change_percent = (price - prev_close) / prev_close * 100.0
        except Exception:
            change_percent = None

        if price is None:
            return None
        return price, currency, change_percent
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


def get_history_series(ticker: str, days: int = 5):
    """
    Return pandas Series of close prices for last `days` market days, or None.
    """
    try:
        stock = yf.Ticker(ticker)
        hist = stock.history(period=f"{max(days*2, 7)}d")  # fetch extra to be safe
        if hist.empty or 'Close' not in hist:
            return None
        # Take last `days` rows
        close = hist['Close'].dropna().tail(days)
        if close.empty:
            return None
        return close
    except Exception:
        return None


def generate_history_chart_base64(ticker: str, days: int = 5) -> Optional[str]:
    """
    Generate a small line chart for the last `days` closes and return base64 PNG string.
    """
    series = get_history_series(ticker, days=days)
    if series is None:
        return None
    try:
        fig, ax = plt.subplots(figsize=(4, 2.2), dpi=150)
        ax.plot(series.index, series.values, marker='o', linewidth=1.5)
        ax.set_title(f"{ticker} - Last {len(series)} days")
        ax.grid(True, linestyle='--', alpha=0.3)
        ax.tick_params(axis='x', labelrotation=45)
        fig.tight_layout()
        buf = io.BytesIO()
        fig.savefig(buf, format='png')
        plt.close(fig)
        buf.seek(0)
        return base64.b64encode(buf.read()).decode('ascii')
    except Exception:
        return None
