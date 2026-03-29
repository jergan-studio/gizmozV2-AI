from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from transformers import GPT2LMHeadModel, GPT2Tokenizer

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load fine-tuned model
tokenizer = GPT2Tokenizer.from_pretrained("./gizmoz_model")
model = GPT2LMHeadModel.from_pretrained("./gizmoz_model")

class Prompt(BaseModel):
    prompt: str

@app.post("/api/generate")
async def generate_code(prompt: Prompt):
    inputs = tokenizer(prompt.prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_length=150)
    code = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return {"output": code}
