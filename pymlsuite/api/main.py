import logging
from fastapi import FastAPI
from pydantic import BaseModel

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="PyMLSuite API", description="Machine Learning API for model inference."
)


class RequestModel(BaseModel):
    age: int
    income: float


@app.post("/predict")
def predict(data: RequestModel):
    logger.info(f"Received prediction request: {data}")
    return {"prediction": "example_result"}


@app.get("/")
def read_root():
    return {"message": "Welcome to PyMLSuite!"}
