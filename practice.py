# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# import requests
# from fastapi.middleware.cors import CORSMiddleware

# app = FastAPI()

# # Add CORS middleware
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Set API Key
# GROQ_API_KEY = "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"
# API_URL = "https://api.groq.com/openai/v1/chat/completions"

# class ChatRequest(BaseModel):
#     message: str

# @app.post("/chat/")
# async def chat(request: ChatRequest):
#     headers = {"Authorization": f"Bearer {GROQ_API_KEY}"}
#     payload = {
#         "model": "llama-3.3-70b-versatile",  # Updated model name
#         "messages": [{"role": "user", "content": request.message}],
#         "temperature": 0.7,
#         "max_tokens": 500
#     }
    
#     try:
#         response = requests.post(API_URL, json=payload, headers=headers, timeout=10)
#         response.raise_for_status()
#         return response.json()
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))