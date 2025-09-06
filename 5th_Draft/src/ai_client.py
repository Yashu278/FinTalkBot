from typing import List, Tuple
from . import config

try:
    from openai import OpenAI  # type: ignore
except Exception:
    OpenAI = None  # type: ignore

try:
    import google.generativeai as genai  # type: ignore
except Exception:
    genai = None  # type: ignore


def _reply_openai(messages: List[Tuple[str, str]]) -> str:
    if OpenAI is None or not config.OPENAI_API_KEY:
        return "AI mode is not configured. Please set OPENAI_API_KEY."
    client = OpenAI(api_key=config.OPENAI_API_KEY)
    sdk_messages = [{"role": role, "content": content} for role, content in messages]
    chat = client.chat.completions.create(
        model=config.OPENAI_MODEL,
        messages=sdk_messages,
        temperature=0.3,
        max_tokens=500,
    )
    return chat.choices[0].message.content or ""


def _reply_gemini(messages: List[Tuple[str, str]]) -> str:
    if genai is None or not config.GEMINI_API_KEY:
        return "AI mode is not configured. Please set GEMINI_API_KEY."
    genai.configure(api_key=config.GEMINI_API_KEY)
    model = genai.GenerativeModel(config.GEMINI_MODEL)
    # Flatten messages into a single prompt with role tags
    parts = []
    for role, content in messages:
        if role == "system":
            parts.append(f"System: {content}")
        elif role == "assistant":
            parts.append(f"Assistant: {content}")
        else:
            parts.append(f"User: {content}")
    prompt = "\n".join(parts)
    resp = model.generate_content(prompt)
    return getattr(resp, "text", None) or (resp.candidates[0].content.parts[0].text if getattr(resp, "candidates", None) else "")


def generate_ai_reply(messages: List[Tuple[str, str]]) -> str:
    """
    messages: list of (role, content), role in {system,user,assistant}
    Returns assistant reply text via configured provider.
    """
    try:
        provider = (config.AI_PROVIDER or "openai").lower()
        if provider == "gemini":
            return _reply_gemini(messages)
        return _reply_openai(messages)
    except Exception as e:
        return f"AI error: {e}"


