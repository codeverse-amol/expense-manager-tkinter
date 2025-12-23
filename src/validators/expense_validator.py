from datetime import date
from src.models.expense import Expense

class ExpenseValidator:

    def validate(self, expense: Expense) -> None:
        self._validate_amount(expense.amount)
        self._validate_category(expense.category)
        self._validate_description(expense.description)
        self._validate_date(expense.expense_date)

    def _validate_amount(self, amount:float) -> None:
        if amount <= 0:
            raise ValueError("Amount must be greater than zero")
    
    
    def _validate_category(self, category:str) -> None:
        if not category or not category.strip():
            raise ValueError("Category cannot be empty.")
    
    
    def _validate_description(self, description:str) -> None:
        if not description or not description.strip():
            raise ValueError("Description cannot be empty.")
    
    
    def _validate_date(self, expense_date: date) -> None:
        if not isinstance(expense_date, date):
            raise ValueError("Invalid expense date")
    
    

