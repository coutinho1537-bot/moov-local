# backend/config.py
import os
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(dotenv_path=Path(__file__).parent / ".env")

# --- 채팅 클라이언트 — OpenAI 호환 API (로컬 버전: Gemini 기본, .env만 바꾸면 Ollama 등도 가능) ---
client = OpenAI(
    base_url=os.environ["LLM_BASE_URL"],
    api_key=os.environ["LLM_API_KEY"],
)

# 다른 파일(chat.py, rag.py)을 건드리지 않도록 기존 변수 이름을 그대로 쓴다
AZURE_OPENAI_DEPLOYMENT_NAME = os.environ["LLM_MODEL"]
AZURE_EMBEDDING_DEPLOYMENT_NAME = os.getenv("LLM_EMBEDDING_MODEL", "")
