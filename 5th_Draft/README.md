## 5th Draft - AI Mode Enabled

New:
- AI Mode toggle in UI; backend calls OpenAI when `mode=ai`.
- Configure `OPENAI_API_KEY` and optional `OPENAI_MODEL` in environment.

Setup:
```bash
cd 5th_Draft
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt

# Set up environment variables
cp ../env.example .env
# Edit .env file with your actual API keys

python -m src.app
```

Docker Compose (with SQLite volume):
```bash
# Set up environment variables first
cp ../env.example .env
# Edit .env file with your actual API keys

docker compose up --build -d
```

UI:
- Toggle "AI Mode" next to Send to switch between rule-based and AI.
## FinTalkBot - 2nd Draft (Enhanced)

Improvements over 1st_Draft:
- Config via environment variables (`src/config.py`), optional `.env` support
- Robust requests with timeouts and user agent
- Logging level configurable via `LOG_LEVEL`
- Dockerfile with Gunicorn for production serving

### Setup (local)
1. Create and activate a venv (Python 3.13 recommended)
2. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
3. Optionally create `.env` (see keys in `src/config.py`)
4. Run:
   ```bash
   python -m src.app
   ```

### Run with Docker
```bash
docker build -t fintalkbot:latest .
docker run --rm -p 5000:5000 fintalkbot:latest
```

### Endpoints
- GET `/` renders chat UI
- POST `/chat` with JSON `{ "message": "..." }`
- GET `/health` health check


