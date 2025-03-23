import uvicorn
from app import app  # Ensure you are importing FastAPI app correctly

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
