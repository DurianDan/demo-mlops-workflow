from pydantic import BaseModel
from typing import List, Any, Dict, Union


class Prob1Table(BaseModel):
    job: str
    category: str
    amt: float
    zipcode: int
    latitude: float
    longitude: float
    city_pop: int
    merch_latitude: float
    merch_longitude: float
    age: float
    hour: int
    day: int
    month: int
    is_fraud: bool
    trans_freq: float
    recent_trans_freq: float
    time_since_last: float


class Prob2Table(BaseModel):
    work_year: int
    experience_level: str
    employment_type: str
    job_title: str
    salary: int
    salary_currency: str
    label: int
    employee_residence: str
    remote_ratio: float  # only int's in the prob1_train.parquet
    company_location: str
    company_size: str


class ToPredictSchema(BaseModel):
    """Data Scheme of the Request Body, that will be received by /predict/ route

    - `id` of the request
    - `rows` contains names of features
    - `columns` 2D array data
    """
    id: int
    rows: List[str]
    columns: List[List[Union[None, float]]]


class DonePredictSchema(BaseModel):
    """Data Scheme of the Response Body, that will be sent from /predict/ route

    - `id` of the corresponding request
    - `rows` contains names of features
    - `columns` 2D array data
    """
    id: int
    predictions: List[Union[None, float]]
