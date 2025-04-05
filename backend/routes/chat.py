from fastapi import APIRouter, HTTPException  # ✅ APIRouter import 추가
from pydantic import BaseModel
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

router = APIRouter()  # ✅ APIRouter 인스턴스 생성

# ✅ ChatRequest 모델 정의 (사용자의 입력을 받을 데이터 구조)
class ChatRequest(BaseModel):
    prompt: str

# 모델 로드
MODEL_NAME = "LGAI-EXAONE/EXAONE-Deep-2.4B"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, trust_remote_code=True)

device = "mps" if torch.backends.mps.is_available() else "cpu"
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, trust_remote_code=True)
model.to(device)

@router.post("/chat")
async def chat(request: ChatRequest):
    print(f"📩 Received prompt: {request.prompt}")

    try:
        # ✅ 모델이 자연스럽게 답할 수 있도록 프롬프트 정리
        prompt = f"User: {request.prompt}\nAI:"

        inputs = tokenizer(prompt, return_tensors="pt").to(device)
        print("🛠 Generating response...")

        output = model.generate(
            **inputs, 
            max_length=100,
            temperature=1.0,
            top_k=50,
            top_p=0.9,
            do_sample=True,
            repetition_penalty=1.2,
        )

        response = tokenizer.decode(output[0], skip_special_tokens=True)
        
        # ✅ AI의 응답 부분만 추출
        if "AI:" in response:
            response = response.split("AI:")[-1].strip()

        print(f"✅ Generated response: {response}")  
        return {"response": response}

    except Exception as e:
        print(f"❌ Error during response generation: {e}")
        return {"error": "Failed to generate response"}
