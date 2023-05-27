from fastapi import FastAPI, Request
from .db import engine, session_local

from .problem.api_models import Base
from .problem.api_models.factory import ModelCreator
from .problem.schema import RequestSchema


Base.metadata.create_all(
    bind=engine  # create tables for each model if not existing
)

app = FastAPI()
model_creator = ModelCreator()

@app.post("/phase-{phase_id}/prob-{prob_id}/predict")
async def recieve(phase_id: int, prob_id: int,
                  request_data: RequestSchema
                  ):
    session = session_local()
    api_model = model_creator.create_model(phase_id, prob_id)

    ''' TODO:
    - create asynchronous sqlalchemy session
    - apply asynchronous insertion'''
    
    for info in request_data['columns']:
        record = {
            request_data['rows'][idx]
            : info[idx]
            for idx in range(len(info))
        }
        session.add(
            api_model(
                **record,
                request_id = request_data['id']
                )
            )
        session.commit()

    return {
        "phase_id" : phase_id,
        "prob_id" : prob_id,
        'message': f'success: {len(request_data["rows"])} records added to db'
    }

