import tkinter as tk
from tkinter import messagebox
from datetime import date

from src.services.expense_service import ExpenseService
from src.repositories.json_expense_repository import JsonExpenseRepository
from src.models.expense import Expense

from typing import Optional


class ExpenseApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Expense Tracker")
        self.geometry("400x300")

        repo = JsonExpenseRepository()
        self.service = ExpenseService(repo)


        tk.Label(self, text="Category").pack()
        self.category_entry = tk.Entry(self)
        self.category_entry.pack()

        tk.Label(self, text="Amount").pack()
        self.amount_entry = tk.Entry(self)
        self.amount_entry.pack()

        tk.Label(self, text="Expenses").pack(pady=(10, 0))
        self.expense_listbox = tk.Listbox(self, width=50)
        self.expense_listbox.pack(pady=5)

        tk.Button(self, text="Add Expense", command=self.add_expense).pack(pady=10)
        tk.Button(self, text="Refresh List", command=self.refresh_expenses).pack(pady=5)
        tk.Button(self, text="Delete Selected Expense", command=self.delete_expense).pack(pady=5)
        tk.Button(self, text="Update Selected Expense", command=self.update_expense).pack(pady=5)
        tk.Button(self, text="Save Expenses", command=self.save_expenses).pack(pady=5)
        tk.Button(self, text="Load Expenses", command=self.load_expenses).pack(pady=5)
        self.refresh_expenses()






    def add_expense(self):
        try:
            category = self.category_entry.get().strip()
            amount = int(self.amount_entry.get())

            expense = Expense(
                amount=amount,
                category=category,
                description="N/A",
                expense_date=date.today()
            )

            self.service.add_expense(expense)
            messagebox.showinfo("Success", "Expense added successfully")

            self.category_entry.delete(0, tk.END)
            self.amount_entry.delete(0, tk.END)
            self.refresh_expenses()


        except Exception as e:
            messagebox.showerror("Error", str(e))


    def refresh_expenses(self):
        self.expense_listbox.delete(0, tk.END)

        expenses = self.service.get_all()
        for e in expenses:
            display = f"{e.category} | {e.amount} | {e.expense_date}"
            self.expense_listbox.insert(tk.END, display)




    def delete_expense(self):
        try:
            selected = self.expense_listbox.curselection()

            if not selected:
                messagebox.showwarning("Warning", "Please select an expense to delete")
                return

            index = selected[0]
            self.service.delete(index)

            messagebox.showinfo("Success", "Expense deleted successfully")
            self.refresh_expenses()

        except Exception as e:
            messagebox.showerror("Error", str(e))


    def update_expense(self):
        try:
            selected = self.expense_listbox.curselection()

            if not selected:
                messagebox.showwarning("Warning", "Please select an expense to update")
                return

            index = selected[0]
            expense = self.service.get_all()[index]

            # Simple update dialog using input boxes
            new_category = self.simple_input(
                "Update Category",
                "Enter new category (leave empty to keep same):"
            )

            new_amount = self.simple_input(
                "Update Amount",
                "Enter new amount (leave empty to keep same):"
            )

            if new_category:
                self.service.update_category(index, new_category)

            if new_amount:
                self.service.update_amount(index, int(new_amount))

            messagebox.showinfo("Success", "Expense updated successfully")
            self.refresh_expenses()

        except Exception as e:
            messagebox.showerror("Error", str(e))



    def simple_input(self, title: str, prompt: str) -> Optional[str]:
        popup = tk.Toplevel(self)
        popup.title(title)
        popup.geometry("300x120")

        tk.Label(popup, text=prompt).pack(pady=5)
        entry = tk.Entry(popup)
        entry.pack(pady=5)

        result: dict[str, Optional[str]] = {"value": None}

        def submit():
            result["value"] = entry.get().strip()
            popup.destroy()

        tk.Button(popup, text="Submit", command=submit).pack(pady=5)

        popup.grab_set()
        self.wait_window(popup)

        return result["value"]


    def save_expenses(self):
        try:
            self.service.save()
            messagebox.showinfo("Saved", "Expenses saved successfully")
        except Exception as e:
            messagebox.showerror("Error", str(e))


    def load_expenses(self):
        try:
            self.service.load()
            self.refresh_expenses()
            messagebox.showinfo("Loaded", "Expenses loaded successfully")
        except Exception as e:
            messagebox.showerror("Error", str(e))



if __name__ == "__main__":
    app = ExpenseApp()
    app.mainloop()
