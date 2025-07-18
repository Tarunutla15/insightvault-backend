# sentiment.py
from transformers import pipeline
from loguru import logger

# Load the sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

def analyze_sentiment(text: str) -> str:
    try:
        # Limit to 512 tokens for transformer compatibility
        result = sentiment_pipeline(text[:512])[0]
        label = result['label']  # e.g., 'POSITIVE' or 'NEGATIVE'
        logger.info(f"Sentiment: {label}")
        return label
    except Exception as e:
        logger.exception("Sentiment analysis failed")
        raise RuntimeError(f"Sentiment analysis failed: {e}")
