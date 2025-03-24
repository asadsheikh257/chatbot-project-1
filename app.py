from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from langchain_groq import ChatGroq
from langchain.schema import AIMessage, HumanMessage

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Set API Key (Make sure to load this securely in production)
GROQ_API_KEY = "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"

# Initialize LangChain Chat Model
chat_model = ChatGroq(
    api_key=GROQ_API_KEY,
    model_name="llama-3.3-70b-versatile"  # Set your preferred model
)

class ChatRequest(BaseModel):
    message: str

@app.post("/chat/")
async def chat(request: ChatRequest):
    try:
        # Call the LangChain chat model
        response = chat_model.invoke([HumanMessage(content=request.message)])
        
        # Extract and return response
        return {"response": response.content}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

