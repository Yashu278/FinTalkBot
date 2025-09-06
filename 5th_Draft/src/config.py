import os

try:
    # Optional: load .env if python-dotenv is installed
    from dotenv import load_dotenv  # type: ignore
    load_dotenv()
except Exception:
    pass


def _get_bool(name: str, default: bool) -> bool:
    value = os.getenv(name)
    if value is None:
        return default
    return value.lower() in {"1", "true", "yes", "on"}


# Application
DEBUG: bool = _get_bool("FLASK_DEBUG", True)
PORT: int = int(os.getenv("PORT", "5000"))
HOST: str = os.getenv("HOST", "0.0.0.0")

# Logging
LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO").upper()
LOG_FILE: str | None = os.getenv("LOG_FILE")

# Data fetching
NEWS_QUERY: str = os.getenv("NEWS_QUERY", "stock market")
REQUEST_TIMEOUT_SECS: float = float(os.getenv("REQUEST_TIMEOUT_SECS", "10"))
USER_AGENT: str = os.getenv(
    "USER_AGENT",
    "FinTalkBot/1.0 (+https://example.com) Python-requests",
)

# Sessions
SECRET_KEY: str = os.getenv("SECRET_KEY", "dev-secret-change-me")

# AI/LLM
AI_PROVIDER: str = os.getenv("AI_PROVIDER", "openai").lower()  # openai | gemini
OPENAI_API_KEY: str | None = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL: str = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
GEMINI_API_KEY: str | None = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL: str = os.getenv("GEMINI_MODEL", "gemini-1.5-flash")


