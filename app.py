from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from summarizer import generate_summary
from keywords import extract_tags
from sentiment import analyze_sentiment
from db import SessionLocal
from models import Insight
from dotenv import load_dotenv
from supabase import create_client
import os
load_dotenv()

app = FastAPI()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
class AnalyzeRequest(BaseModel):
    text: str



@app.post("/analyze")
async def analyze_text(payload: AnalyzeRequest):
    text = payload.text.strip()
    if not text:
        raise HTTPException(status_code=400, detail="Text input cannot be empty.")

    try:
        summary = generate_summary(text)
        tags = extract_tags(text)
        sentiment = analyze_sentiment(text)

        # Save to DB
        db = SessionLocal()
        new_entry = Insight(
            input_text=text,
            summary=summary,
            tags=",".join(tags),
            sentiment=sentiment
        )
        db.add(new_entry)
        db.commit()
        db.close()

        return {
            "summary": summary,
            "tags": tags,
            "sentiment": sentiment
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
@app.get("/history")
async def get_history():
    try:
        db = SessionLocal()
        results = db.query(Insight).order_by(Insight.created_at.desc()).limit(10).all()
        db.close()

        return [
            {
                "input_text": i.input_text,
                "summary": i.summary,
                "tags": i.tags.split(","),
                "sentiment": i.sentiment,
                "created_at": i.created_at.isoformat()
            }
            for i in results
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
