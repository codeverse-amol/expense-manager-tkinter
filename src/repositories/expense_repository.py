from abc import ABC, abstractmethod
from typing import List
from src.models.expense import Expense



class ExpenseRepository(ABC):

    @abstractmethod
    def load_all(self) -> List[Expense]:

        pass

    @abstractmethod
    def save_all(self, expenses: List[Expense]) -> None:
        pass
