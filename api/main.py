from fastapi import FastAPI, Request

from db import engine
import models
from schemas import ToPredictSchema, DonePredictSchema

models.Base.metadata.create_all(
    bind= engine # create tables for each model if not existing
    )

app = FastAPI()

@app.post("/phase-{phase_id}/prob-{prob_id}/predict")
async def recieve( phase_id:int, prob_id:int, request:Request):
    body = await request.json()
    records_to_predict = [
        ToPredictSchema(**rec)
        for rec in body
    ]
    pass
