from datetime import date

class Expense:

    def __init__(self, amount:float, category:str, description:str, expense_date:date):
        self.amount = amount
        self.category = category
        self.description = description
        self.expense_date = expense_date

    
    def __repr__(self):
        return (
            f"Expense(amount={self.amount}, "
            f"category='{self.category}', "
            f"description='{self.description}', "
            f"expense_date={self.expense_date})"
        )
        