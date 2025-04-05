# 🧠 EXAONE Deep Chat

AI 챗봇 웹앱 프로젝트입니다.  
LG AI Research의 LLM인 [EXAONE-Deep](https://huggingface.co/collections/LGAI-EXAONE/exaone-deep-67d119918816ec6efa79a4aa)을 기반으로 사용자의 입력에 자연어 응답을 생성합니다.

---

## 📦 기술 스택

### 🧩 Frontend
- [Next.js 15](https://nextjs.org/)
- TypeScript
- Tailwind CSS
- React

### 🚀 Backend
- FastAPI
- HuggingFace Transformers
- EXAONE-Deep 모델 API 호출

---

## 🗂️ 폴더 구조

```
exaone-deep-chat/
│
├── backend/               # FastAPI 서버
│   ├── routes/            # 라우터 (예: chat.py)
│   ├── server.py          # FastAPI 앱 실행
│   └── requirements.txt   # 백엔드 의존성
│
├── frontend/              # Next.js 앱
│   ├── src/
│   │   ├── app/           # Next.js app router
│   │   │   ├── layout.tsx
│   │   │   ├── page.tsx
│   │   │   └── styles/
│   │   │       └── globals.css
│   │   ├── components/    # UI 컴포넌트 (ChatBox, Message)
│   │   └── utils/         # API 유틸 함수 (api.ts)
│   ├── tailwind.config.js
│   ├── postcss.config.js
│   └── package.json
│
└── README.md              # 📘 프로젝트 설명
```

---

## ⚙️ 설치 및 실행 방법

### 1. 프로젝트 클론
```bash
git clone https://github.com/your-id/exaone-deep-chat.git
cd exaone-deep-chat
```

### 2. 백엔드 설정 및 실행
```bash
cd backend
pip install -r requirements.txt
uvicorn server:app --reload
```

### 3. 프론트엔드 설정 및 실행
```bash
cd ../frontend
npm install

# Turbopack 문제 해결을 위해 Webpack으로 실행
NEXT_LEGACY_TURBOPACK=true npm run dev
```

### 4. 접속
```
http://localhost:3000
```

---

## 🤖 사용된 모델

- **Model**: [`LGAI-EXAONE/EXAONE-Deep-2.4B`](https://huggingface.co/LGAI-EXAONE/EXAONE-Deep-2.4B)
- **Pipeline**: `text-generation`
- **Language**: Korean + English

---

## 📝 주요 기능

- 사용자 입력 실시간 전송
- FastAPI 서버에서 Hugging Face 모델 호출
- 자연어 응답 생성 및 표시
- Tailwind를 활용한 UI (커스터마이징 가능)

---

## 💡 참고 사항

- EXAONE-Deep-32B는 너무 커서 Inference API에서 직접 실행 불가능합니다. 2.4B 모델을 사용하는 것을 추천합니다.
- CORS 문제 해결을 위해 FastAPI에 CORS 설정을 추가해야 합니다.
- 프론트엔드에서 Turbopack이 Tailwind와 충돌할 경우 `NEXT_LEGACY_TURBOPACK=true` 플래그를 사용합니다.

---