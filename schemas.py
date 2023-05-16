from pydantic import BaseModel
from typing import List, Any, Dict, Union

class Prob1Table(BaseModel):
    


class ToPredictSchema(BaseModel):
    '''Data Scheme of the Request Body, that will be received by /predict/ route

    - `id` of the request
    - `rows` contains names of features
    - `columns` 2D array data
    '''
    id: int
    rows: List[str]
    columns: List[List[Union[None,float]]]


class DonePredictSchema(BaseModel):
    '''Data Scheme of the Response Body, that will be sent from /predict/ route

    - `id` of the corresponding request
    - `rows` contains names of features
    - `columns` 2D array data
    '''
    id: int
    predictions: List[List[Union[None,float]]]