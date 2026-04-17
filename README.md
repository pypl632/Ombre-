Ombre

AI routing layer for inference.

---

What is Ombre?

Ombre is a lightweight AI routing layer that lets you use multiple AI models through a single API.

---

Quickstart

pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 3000

---

Endpoints

- GET / → check if running
- GET /health → health check
- POST /v1/infer → inference endpoint

---

Status

Early-stage project.
