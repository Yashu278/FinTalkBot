# Fetch stock data
import yfinance as yf
import requests
from bs4 import BeautifulSoup

def get_stock_price(ticker):
    stock = yf.Ticker(ticker)
    hist = stock.history(period="1d")
    return hist['Close'].iloc[-1]

def get_finance_news(query="stock market"):
    url = f"https://news.google.com/search?q={query}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = [h.text for h in soup.find_all("a", {"class": "JtKRv"})]
    return headlines[:5]
