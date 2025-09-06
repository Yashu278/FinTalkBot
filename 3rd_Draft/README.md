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


