import os

import mlflow
from fastapi import FastAPI
from pydantic import BaseModel

MODEL_URI = os.environ.get("MODEL_URI", "models:/complaint-router@champion")

router = mlflow.sklearn.load_model(MODEL_URI)
model_id = mlflow.models.Model.load(MODEL_URI).model_id

app = FastAPI()


class Complaint(BaseModel):
    text: str


class Route(BaseModel):
    team: str
    confidence: float
    model_id: str


@app.post("/route")
def route(complaint: Complaint) -> Route:
    probabilities = router.predict_proba([complaint.text])[0]
    best = probabilities.argmax()
    return Route(
        team=router.classes_[best],
        confidence=round(float(probabilities[best]), 3),
        model_id=model_id,
    )


@app.get("/health")
def health():
    return {"status": "ok", "model_id": model_id}