# src/chatbot.py
import re
from typing import List, Tuple, Optional
from src.data_fetcher import get_stock_price, get_finance_news
from src.sentiment_analyzer import analyze_sentiment


def extract_ticker_symbol(user_input: str) -> Optional[str]:
    """
    Extract ticker symbol from user input.
    Looks for patterns like 'AAPL', 'price of TSLA', etc.
    """
    user_input = user_input.upper()
    
    # Pattern to match common ticker symbols (2-5 uppercase letters)
    ticker_pattern = r'\b[A-Z]{2,5}\b'
    matches = re.findall(ticker_pattern, user_input)
    
    # Filter out common words that might match the pattern
    exclude_words = {'PRICE', 'STOCK', 'NEWS', 'WHAT', 'THE', 'OF', 'IS', 'FOR'}
    valid_tickers = [match for match in matches if match not in exclude_words]
    
    return valid_tickers[0] if valid_tickers else None


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
    
    # Handle stock price queries
    elif "price" in user_input_lower:
        ticker = extract_ticker_symbol(user_input)
        if not ticker:
            return "Please specify a ticker symbol. For example: 'What is the price of AAPL?'"
        
        try:
            price = get_stock_price(ticker)
            if price is None:
                return f"Sorry, I couldn't fetch the price for {ticker}. Please check if it's a valid ticker symbol."
            return f"The current price of {ticker} is ${price:.2f}"
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
    
    # Handle general stock queries
    elif "stock" in user_input_lower:
        return "I can fetch stock prices for you. Try asking: 'What is the price of AAPL?' or ask for 'finance news'."
    
    # Default response
    else:
        return ("Sorry, I didn't understand that 🤔. I can help you with:\n"
                "• Stock prices (e.g., 'What is the price of AAPL?')\n"
                "• Finance news with sentiment analysis (just ask for 'news')")


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