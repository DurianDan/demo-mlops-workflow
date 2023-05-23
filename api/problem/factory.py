from abc import ABC, abstractmethod
from typing import Any, List, Union, Dict
from pydantic import BaseModel


class ProblemRowInfo(ABC):
    @abstractmethod
    def values_to_predict(self) -> Dict[str, Union[int, float, None, str]]:
        pass


class ProblemRowData(ABC):
    pass


class ProblemRow(ProblemRowInfo, ProblemRowData):
    pass


class ProblemUnsolved(BaseModel):
    """Data Scheme of the Request Body, that will be received by `/predict/` route

    - `id` of the request
    - `rows` contains names of features
    - `columns` 2D array data
    """
    id: int
    rows: List[str]
    columns: List[List[Union[None, float, int, bool, str]]]


class ProblemSolved(BaseModel):
    """Data Scheme of the Response Body, that will be sent from /predict/ route

    - `id` of the corresponding request
    - `predictions` 2D array data
    """
    id: int
    predictions: List[Union[None, float]]



class ProblemCreator:
    
    def create_problem(phase_id: int, prob_id: int ) -> Problem:

class PhaseID
