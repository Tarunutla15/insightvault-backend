# keywords.py
from keybert import KeyBERT

# Load the model once when the module is imported
model = KeyBERT()

def extract_tags(text: str, top_n: int = 5) -> list:
    try:
        keywords = model.extract_keywords(text, top_n=top_n, stop_words='english')
        return [kw[0] for kw in keywords]  # Only return keyword strings
    except Exception as e:
        raise RuntimeError(f"Keyword extraction failed: {e}")
