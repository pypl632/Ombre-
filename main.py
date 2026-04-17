from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from infer import run_inference

app = FastAPI(title="Ombre API")

# Request model
class InferenceRequest(BaseModel):
    prompt: str


@app.get("/")
def root():
    return {"message": "Ombre API is running"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/infer")
def infer(request: InferenceRequest):
    try:
        result = run_inference(request.prompt)
        return {
            "success": True,
            "response": result
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
