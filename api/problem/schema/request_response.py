from pydantic import BaseModel, validator
from typing import List, Any, Dict, Union
from json import loads


class RequestSchema(BaseModel):
    """Data Scheme of the Request Body, that will be received by /predict/ route

    - `id` of the request
    - `rows` contains names of features
    - `columns` 2D array data
    """
    id: int
    rows: List[str]
    columns: List[List[Union[None, float]]]


class ResponseSchema(BaseModel):
    """Data Scheme of the Response Body, that will be sent from /predict/ route

    - `id` of the corresponding request
    - `rows` contains names of features
    - `columns` 2D array data
    """
    id: int
    predictions: List[Union[None, float]]

