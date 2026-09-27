# app.py — Vercel 배포용 진입점 (로컬 실행에는 쓰이지 않음, 로컬은 기존대로 front에서 npm run dev)
# backend/main.py의 FastAPI 앱을 그대로 불러오고, 화면 파일(front/public)을 같은 주소에서 제공한다.
import sys
from pathlib import Path

from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

ROOT = Path(__file__).parent
sys.path.insert(0, str(ROOT / "backend"))  # backend 안의 모듈들이 서로를 이름으로 import하므로 경로 추가

from main import app  # noqa: E402  (backend/main.py)

PUBLIC = ROOT / "front" / "public"


@app.get("/", include_in_schema=False)
def home():
    # 로컬 front/server.mjs와 같게 첫 화면은 moov.html
    return FileResponse(PUBLIC / "moov.html")


# /api/... 경로는 위에서 등록된 백엔드가 먼저 처리하고, 나머지는 front/public 파일을 제공
app.mount("/", StaticFiles(directory=PUBLIC, html=True), name="front")
