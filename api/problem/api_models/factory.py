from abc import ABC, abstractmethod
from api.problem.api_models.base import Base
from .phase1 import Prob1Table, Prob2Table
from .base import ProblemBase


class AbstractModelCreator(ABC):
    @abstractmethod
    def __init__(self, prob_id) -> None:
        pass

    @abstractmethod
    def get_model(self) -> Base:
        pass


class Phase1ModelCreator(AbstractModelCreator):
    def __init__(self, prob_id) -> None:
        self.prob_id = prob_id
        self.problems_dict = {
            1: Prob1Table,
            2: Prob2Table
        }

    def get_model(self) -> Base:
        return self.problems_dict[ self.prob_id ]


class Phase2ModelCreator(AbstractModelCreator):
    def __init__(self, prob_id) -> None:
        self.prob_id = prob_id
        self.problems_dict = {
            1: Prob1Table,
            2: Prob2Table
        }

    def get_model(self) -> Base:
        return self.problems_dict[ self.prob_id ]


class Phase3ModelCreator(AbstractModelCreator):
    def __init__(self, prob_id) -> None:
        self.prob_id = prob_id
        self.problems_dict = {
            1: Prob1Table,
            2: Prob2Table
        }

    def get_model(self) -> Base:
        return self.problems_dict[ self.prob_id ]


class ModelCreator():
    def __init__(self) -> None:
        self.creators_idx = {
            1: Phase1ModelCreator,
            2: Phase2ModelCreator,
            3: Phase3ModelCreator,
        }
    
    def get_creator(self, phase_id: int) -> AbstractModelCreator: 
        return self.creators_idx[ phase_id ]
    
    def create_model(self, phase_id: int, prob_id: int) -> Base:
        return self.get_creator(phase_id).get_model(prob_id)