from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Ombre is running"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/v1/infer")
def infer():
    return {"response": "Ombre working"}
