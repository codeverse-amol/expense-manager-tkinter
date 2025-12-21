from typing import List
from datetime import date

from models.expense import Expense
from repositories.expense_repository import ExpenseRepository
from validators.expense_validator import ExpenseValidator





class ExpenseService:
    
    def __init__(self, repository: ExpenseRepository):
        self._repo = repository
        self._validator = ExpenseValidator()
        self._expenses: List[Expense] = self._repo.load_all()

    # Add expense
    def add_expense(self, expense: Expense) -> None:
        self._validator.validate(expense)
        self._expenses.append(expense)

    # Save expenses
    def save(self) -> None:
        self._repo.save_all(self._expenses)

    # Load expenses
    def load(self) -> None:
        self._expenses = self._repo.load_all()

    # Get all expenses
    def get_all(self) -> List[Expense]:
        return list(self._expenses)
    
    # Get total amount
    def get_total(self) -> float:
        return sum(e.amount for e in self._expenses)
    
    # Total per category
    def get_total_per_category(self) -> dict[str, float]:
        totals: dict[str, float] = {}
        for e in self._expenses:
            totals[e.category] = totals.get(e.category, 0) + e.amount

        return totals


    # Search
    def find_by_category(self, category: str) -> List[Expense]:
        return [e for e in self._expenses if e.category == category]


    def find_by_date(self, search_date: date) -> List[Expense]:
        return [e for e in self._expenses if e.expense_date == search_date]
    
    # Delete
    def delete(self, index: int) -> Expense:
        return self._expenses.pop(index)

    # Update
    def update_category(self, index: int, category: str) -> None:
        self._expenses[index].category = category

    def update_amount(self, index: int, amount: float) -> None:
        self._expenses[index].amount = amount

    def update_date(self, index: int, new_date: date) -> None:
        self._expenses[index].expense_date = new_date


