import json

from typing import List
from datetime import date

from models.expense import Expense
from repositories.expense_repository import ExpenseRepository


class JsonExpenseRepository(ExpenseRepository):

    def __init__(self, file_path :str = "expenses.json"):
        self.file_path = file_path

    

    def load_all(self) -> List[Expense]:
        try:
           
            with open(self.file_path, "r") as f:
               data = json.load(f)

            return [
                Expense(
                    amount=item["amount"],
                    category=item["category"],
                    description="N/A",
                    expense_date = date.fromisoformat(item["date"])
                )
                for item in data
            ]
        except FileNotFoundError:
            return []
        
 
    def save_all(self, expenses: List[Expense]) -> None:
        data = [
            {
                "category": e.category,
                "amount" : e.amount,
                "date" : e.expense_date.isoformat()
            }

            for e in expenses
        ]

        with open(self.file_path, "w") as f:
            json.dump(data, f, indent=4)