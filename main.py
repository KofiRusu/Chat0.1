from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from model_setup import llama_model  # Ensure model_setup.py is corrected
# import torch
app = FastAPI()

class Message(BaseModel):
    user_id: str
    text: str

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/generate")
def generate(text: str):
    response = llama_model.generate_response(text)
    return {"response": response}

@app.post("/send_message")
async def send_message(message: Message):
    try:
        response = llama_model.generate_response(message.text)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
