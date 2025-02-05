from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
from fastapi.middleware.cors import CORSMiddleware
import os

# Initialize FastAPI app
app = FastAPI()

# Configure CORS (allow frontend to communicate with backend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to specific frontend origins for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Set your Gorq API Key
gorq_api_key = "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"
GORQ_API_URL = "https://api.gorq.com/chat"

# Define request model
class ChatRequest(BaseModel):
    message: str

# Chatbot API endpoint
@app.post("/chat/")
def chat(request: ChatRequest):
    try:
        headers = {"Authorization": f"Bearer {gorq_api_key}", "Content-Type": "application/json"}
        data = {"message": request.message}
        response = requests.post(GORQ_API_URL, json=data, headers=headers)
        response.raise_for_status()
        reply = response.json().get("response", "No response from Gorq API")
        return {"response": reply}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Root endpoint
def read_root():
    return {"message": "Chatbot backend is running!"}
