# keywords.py
from keybert import KeyBERT
from loguru import logger

# Load the model once when the module is imported
model = KeyBERT()

def extract_tags(text: str, top_n: int = 5) -> list:
    try:
        keywords = model.extract_keywords(text, top_n=top_n, stop_words='english')
        extracted = [kw[0] for kw in keywords]  # Only return keyword strings
        logger.info(f"Extracted {len(extracted)} keywords: {extracted}")
        return extracted
    except Exception as e:
        logger.exception("Keyword extraction failed")
        raise RuntimeError(f"Keyword extraction failed: {e}")
