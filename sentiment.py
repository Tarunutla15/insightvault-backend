# sentiment.py
from transformers import pipeline

# Load the sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

def analyze_sentiment(text: str) -> str:
    try:
        # Limit to 512 tokens for transformer compatibility
        result = sentiment_pipeline(text[:512])[0]
        return result['label']  # e.g., 'POSITIVE' or 'NEGATIVE'
    except Exception as e:
        raise RuntimeError(f"Sentiment analysis failed: {e}")
