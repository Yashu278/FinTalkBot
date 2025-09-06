# NLP for news & tweets
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import logging

try:
    nltk.download("vader_lexicon", quiet=True)
except Exception as e:
    logging.getLogger(__name__).warning("Failed to download vader_lexicon: %s", e)

sia = SentimentIntensityAnalyzer()

def analyze_sentiment(text: str) -> str:
    score = sia.polarity_scores(text)
    if score['compound'] > 0.05:
        return "Positive"
    elif score['compound'] < -0.05:
        return "Negative"
    else:
        return "Neutral"
