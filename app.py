from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MISTRAL_API_KEY = "xOVtRdmGCF2hkjxzpWIs3GWCBqr3bgZS"
MISTRAL_API_URL = "https://api.mistral.ai/v1/chat/completions"

class ChatRequest(BaseModel):
    message: str

@app.post("/chat/")
async def chat(request: ChatRequest):
    headers = {"Authorization": f"Bearer {MISTRAL_API_KEY}"}
    payload = {
        "model": "mistral-tiny",  # Updated model name
        "messages": [{"role": "user", "content": request.message}],
        "temperature": 0.7,
        "max_tokens": 200
    }
    
    try:
        response = requests.post(MISTRAL_API_URL, json=payload, headers=headers, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))