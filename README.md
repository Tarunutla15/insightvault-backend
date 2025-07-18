# InsightVault 🧠
AI-powered text analyzer that summarizes content, extracts keywords, and detects sentiment — built using FastAPI, HuggingFace, KeyBERT, and Supabase.

## 🚀 Features

- 📚 **Summarization**: Uses HuggingFace/QLoRA or OpenAI models to generate concise summaries.
- 🏷️ **Keyword Extraction**: Extracts meaningful tags using KeyBERT or Sentence-BERT.
- 😊 **Sentiment Analysis**: Classifies sentiment (Positive, Neutral, Negative) using transformers.
- ⚡ **FastAPI Backend**: Lightweight and high-performance inference API.
- 🛢️ **Supabase DB**: Stores inputs, summaries, and predictions in a managed PostgreSQL database.
- 🐳 **Dockerized**: Easy to containerize and deploy.
- 🔍 **Phase 2 Ready**: Designed for DVC, GitHub Actions, and logging support.

## 🧱 Architecture Overview

1. **User Input**  
   - User sends raw text to the FastAPI `/analyze` endpoint.

2. **FastAPI Backend**
   - Receives request and runs:
     - `generate_summary()` → Summarization
     - `extract_tags()` → Keyword extraction
     - `analyze_sentiment()` → Sentiment classification

3. **Storage (Supabase)**
   - Saves the original text, summary, tags, and sentiment analysis to a PostgreSQL table.

4. **Response**
   - Returns the analysis as JSON to the frontend or any API consumer.

5. **Optional (Planned in Phase 2)**
   - Use DVC to version raw text and results.
   - Set up GitHub Actions for CI checks.
   - Add monitoring & structured logging for production readiness.

## Setup & Run Instructions
## 🛠️ Setup & Running Locally
```bash
### 1. Clone the Repository

git clone https://github.com/your-username/insightvault-backend.git
cd insightvault-backend

```bash
### 2. Create & Activate Virtual Environment
# For Windows
python -m venv venv
venv\Scripts\activate

# For Linux/macOS
python3 -m venv venv
source venv/bin/activate

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Create .env File
SUPABASE_DB_URL=postgresql://postgres:<password>@<host>:5432/postgres
SUPABASE_URL=https://<your-project>.supabase.co
SUPABASE_KEY=<your-supabase-api-key>
OPENAI_API_KEY=<your-openai-key>

### 5. Initialize Database
python init_db.py

### 6. Run the Server
uvicorn app:app --reload --port 8000
```
## 📡 API Usage

### 🔍 `/analyze` - Analyze Text

Performs summarization, keyword extraction, and sentiment analysis on input text.

**POST** `/analyze`

#### 🔸 Request Body (JSON)
```json
{
  "text": "Your full text input here"
}
```

🔸 Response Example
```json
{
  "summary": "Short summary of the input text...",
  "tags": ["keyword1", "keyword2", "keyword3"],
  "sentiment": "POSITIVE"
}
```

