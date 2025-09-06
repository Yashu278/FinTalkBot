# src/chatbot.py
import re
from typing import List, Tuple, Optional
from .data_fetcher import (
    get_stock_price,
    get_finance_news,
    get_price_details,
    generate_history_chart_base64,
)
from .sentiment_analyzer import analyze_sentiment


ALIASES = {
    "apple": "AAPL",
    "tesla": "TSLA",
    "bitcoin": "BTC-USD",
    "ethereum": "ETH-USD",
}

# Expandable known names for fuzzy contains
KNOWN_NAMES = {
    "microsoft": "MSFT",
    "google": "GOOGL",
    "alphabet": "GOOGL",
    "amazon": "AMZN",
    "meta": "META",
    "facebook": "META",
    "nvidia": "NVDA",
}


def extract_ticker_symbol(user_input: str) -> Optional[str]:
    """
    Extract ticker symbol from user input.
    Looks for patterns like 'AAPL', 'price of TSLA', etc.
    """
    # Alias mapping first (case-insensitive)
    lowered = user_input.lower()
    for name, ticker in {**ALIASES, **KNOWN_NAMES}.items():
        if name in lowered:
            return ticker

    user_input = user_input.upper()
    
    # Pattern to match common ticker symbols (2-5 uppercase letters)
    ticker_pattern = r'\b[A-Z]{2,5}\b'
    matches = re.findall(ticker_pattern, user_input)
    
    # Filter out common words that might match the pattern
    exclude_words = {'PRICE', 'STOCK', 'NEWS', 'WHAT', 'THE', 'OF', 'IS', 'FOR'}
    valid_tickers = [match for match in matches if match not in exclude_words]
    
    return valid_tickers[0] if valid_tickers else None


def extract_all_tickers(user_input: str) -> List[str]:
    """Extract possibly multiple tickers, including aliases."""
    lowered = user_input.lower()
    found = []
    for name, ticker in {**ALIASES, **KNOWN_NAMES}.items():
        if name in lowered:
            found.append(ticker)
    # Add explicit ticker-like items
    matches = re.findall(r"\b[A-Za-z.-]{2,6}\b", user_input)
    for token in matches:
        token_up = token.upper()
        if token_up.isalpha() and 2 <= len(token_up) <= 5:
            found.append(token_up)
        elif token_up in {"BTC-USD", "ETH-USD"}:
            found.append(token_up)
    # Deduplicate, preserve order
    seen = set()
    unique = []
    for t in found:
        if t not in seen:
            seen.add(t)
            unique.append(t)
    return unique


def format_news_with_sentiment(news_data: List[Tuple[str, str]]) -> str:
    """
    Format news data with sentiment analysis into a readable string.
    """
    if not news_data:
        return "No news available at the moment."
    
    formatted_news = ["Here are the latest finance news with sentiment analysis:\n"]
    
    for i, (news_item, sentiment) in enumerate(news_data[:5], 1):  # Limit to 5 items
        formatted_news.append(f"{i}. {news_item}")
        formatted_news.append(f"   Sentiment: {sentiment}\n")
    
    return "\n".join(formatted_news)


def format_price_response(ticker: str, price: float, currency: Optional[str], change_pct: Optional[float]) -> str:
    arrow = "▲" if (change_pct is not None and change_pct >= 0) else "▼"
    change_str = f"{arrow} {change_pct:+.2f}%" if change_pct is not None else "—"
    currency_str = currency or "USD"
    return (
        f"📈 {ticker}\n"
        f"Price: {currency_str} ${price:.2f}\n"
        f"Change: {change_str} today"
    )


def format_help() -> str:
    return (
        "Here’s what I can do:\n"
        "• Price: 'price of AAPL' or 'What's the price of Apple?'\n"
        "• News: 'Tesla news'\n"
        "• History: 'AAPL history' (last 5 days, with chart)\n"
        "• Compare: 'Compare Apple and Tesla'\n"
        "• Help: '/help' or 'what can you do'"
    )


def chatbot_response(user_input: str) -> str:
    """
    Enhanced chatbot logic for finance-related queries.
    Handles greetings, stock prices, and news requests.
    """
    if not user_input or not isinstance(user_input, str):
        return "I didn't receive any input. Please ask me about stocks or finance!"
    
    user_input_lower = user_input.lower().strip()
    
    # Handle greetings
    if any(greeting in user_input_lower for greeting in ["hello", "hi", "hey", "good morning", "good afternoon"]):
        return "Hello! 👋 I'm FinTalkBot. How can I help you with stocks today?"
    
    # Handle "how are you" queries
    elif "how are you" in user_input_lower:
        return "I'm just a bot, but I'm doing great 😃. Thanks for asking!"
    
    # Help command
    if user_input_lower.startswith("/help") or "what can you do" in user_input_lower or user_input_lower == "help":
        return format_help()

    # Compare multiple tickers
    if "compare" in user_input_lower:
        tickers = extract_all_tickers(user_input)
        if len(tickers) < 2:
            return "Please specify at least two tickers or names to compare (e.g., 'Compare Apple and Tesla')."
        lines: List[str] = ["🔁 Comparison:"]
        for t in tickers[:5]:
            details = get_price_details(t)
            if not details:
                lines.append(f"- {t}: Not found or unavailable")
                continue
            price, currency, change_pct = details
            lines.append("- " + format_price_response(t, price, currency, change_pct).replace("\n", " | "))
        return "\n".join(lines)

    # Handle stock price queries
    elif "price" in user_input_lower:
        ticker = extract_ticker_symbol(user_input)
        if not ticker:
            return "Please specify a ticker symbol. For example: 'What is the price of AAPL?'"
        
        try:
            details = get_price_details(ticker)
            if not details:
                return "Sorry, I couldn’t find that stock/crypto. Try another."
            price, currency, change_pct = details
            return format_price_response(ticker, price, currency, change_pct)
        except Exception as e:
            return f"Error fetching stock price for {ticker}. Please try again later."
    
    # Handle news queries
    elif "news" in user_input_lower:
        try:
            news = get_finance_news()
            if not news:
                return "No finance news available at the moment. Please try again later."
            
            analyzed_news = [(news_item, analyze_sentiment(news_item)) for news_item in news]
            return format_news_with_sentiment(analyzed_news)
        except Exception as e:
            return "Error fetching finance news. Please try again later."

    # Handle history queries
    elif "history" in user_input_lower:
        ticker = extract_ticker_symbol(user_input)
        if not ticker:
            return "Please specify a ticker for history, e.g., 'AAPL history'."
        chart_b64 = generate_history_chart_base64(ticker, days=5)
        if not chart_b64:
            return f"Sorry, I couldn’t generate history for {ticker}. Try again later."
        return (
            f"📉 {ticker} - Last 5 days\n"
            f"[chart: data:image/png;base64,{chart_b64}]"
        )
    
    # Handle general stock queries
    elif "stock" in user_input_lower:
        return format_help()
    
    # Default response
    else:
        # Gentle fallback with hint
        return (
            "Sorry, I don’t know that yet. Try asking about price, news, or history, "
            "e.g., 'price of AAPL' or 'Tesla news'.\n" + format_help()
        )


# Example usage and testing
if __name__ == "__main__":
    # Test cases
    test_inputs = [
        "Hello",
        "What is the price of AAPL?",
        "Show me finance news",
        "How are you?",
        "Tell me about stocks",
        "Random input"
    ]
    
    for test_input in test_inputs:
        print(f"Input: {test_input}")
        print(f"Response: {chatbot_response(test_input)}")
        print("-" * 50)