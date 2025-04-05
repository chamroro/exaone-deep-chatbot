from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.chat import router  # ✅ chat.py의 router를 불러옴
import uvicorn

app = FastAPI()

# ✅ CORS 설정 추가
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ chat API 라우터 등록
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
