from fastapi import FastAPI
from infer import run_inference

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Ombre is running"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/v1/infer")
def infer(prompt: str):
    return run_inference(prompt)
