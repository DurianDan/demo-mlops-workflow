from fastapi import FastAPI, Request
from db import engine

from problem.api_models import Base
from problem.api_models.factory import ModelCreator
from problem.schema import RequestSchema


Base.metadata.create_all(
    bind=engine  # create tables for each model if not existing
)

app = FastAPI()
model_creator = ModelCreator()

@app.post("/phase-{phase_id}/prob-{prob_id}/predict")
async def recieve(phase_id: int, prob_id: int, request_data: RequestSchema):
    api_model = model_creator.create_model(phase_id, prob_id)
    instance = api_model(request_data.row)