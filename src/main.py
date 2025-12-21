from datetime import date

from models.expense import Expense
from services.expense_service import ExpenseService
from repositories.json_expense_repository import JsonExpenseRepository


# -------------------------
# Dependency wiring
# -------------------------
repo = JsonExpenseRepository()
service = ExpenseService(repo)


# -------------------------
# Main Expense Tracker Logic
# -------------------------
def expense_tracker(n: int) -> None:
    try:
        match n:
            # -------------------------
            # 1. Add Expense
            # -------------------------
            case 1:
                try:
                    category = input("Enter the category: ").strip()
                    amount = int(input("Enter the amount: "))

                    expense = Expense(
                        amount=amount,
                        category=category,
                        description="N/A",
                        expense_date=date.today()
                    )

                    service.add_expense(expense)
                    print("✅ Expense added successfully!\n")

                except ValueError as e:
                    print(f"❌ {e}")

            # -------------------------
            # 2. Show Total per Category
            # -------------------------
            case 2:
                totals = service.get_total_per_category()

                if not totals:
                    print("❌ No expenses found.\n")
                    return

                print(f"{'No':<5}{'Category':<15}{'Total Amount':<15}")
                print("-" * 35)

                for i, (cat, amt) in enumerate(totals.items(), start=1):
                    print(f"{i:<5}{cat:<15}{amt:<15}")

            # -------------------------
            # 3. Show Total Expenses
            # -------------------------
            case 3:
                expenses = service.get_all()

                if not expenses:
                    print("❌ No expenses found.\n")
                    return

                print(f"{'No':<5}{'Category':<15}{'Amount':<10}{'Date'}")
                print("-" * 40)

                for i, e in enumerate(expenses, start=1):
                    print(f"{i:<5}{e.category:<15}{e.amount:<10}{e.expense_date}")

                print("-" * 40)
                print(f"Total: {service.get_total()}")

            # -------------------------
            # 4. Delete Expense
            # -------------------------
            case 4:
                expenses = service.get_all()

                if not expenses:
                    print("❌ No expenses to delete.\n")
                    return

                for i, e in enumerate(expenses, start=1):
                    print(f"{i}. {e}")

                index = int(input("\nEnter index to delete: "))
                service.delete(index - 1)
                print("🗑 Expense deleted successfully\n")

            # -------------------------
            # 5. Update Expense
            # -------------------------
            case 5:
                expenses = service.get_all()

                if not expenses:
                    print("❌ No expenses to update.\n")
                    return

                for i, e in enumerate(expenses, start=1):
                    print(f"{i}. {e}")

                index = int(input("\nEnter index: ")) - 1

                print("1. category")
                print("2. amount")
                print("3. date")

                choice = input("Enter choice: ")

                if choice == "1":
                    service.update_category(index, input("New category: ").strip())

                elif choice == "2":
                    service.update_amount(index, int(input("New amount: ")))

                elif choice == "3":
                    service.update_date(
                        index,
                        date.fromisoformat(input("New date (YYYY-MM-DD): "))
                    )
                else:
                    print("❌ Invalid choice.")
                    return

                print("✅ Expense updated\n")

            # -------------------------
            # 6. Search by category
            # -------------------------
            case 6:
                category = input("Enter category: ")
                matches = service.find_by_category(category)

                if not matches:
                    print("❌ No matching expenses found.\n")
                    return

                for i, e in enumerate(matches, start=1):
                    print(f"{i}. {e.category} : {e.amount} on {e.expense_date}")

            # -------------------------
            # 7. Search by date
            # -------------------------
            case 7:
                search_date = date.fromisoformat(
                    input("Enter date (YYYY-MM-DD): ")
                )
                matches = service.find_by_date(search_date)

                if not matches:
                    print("❌ No matching expenses found.\n")
                    return

                for i, e in enumerate(matches, start=1):
                    print(f"{i}. {e.category} : {e.amount}")

            # -------------------------
            # 8. Save Expenses
            # -------------------------
            case 8:
                service.save()
                print("💾 Expenses saved successfully\n")

            # -------------------------
            # 9. Load Expenses
            # -------------------------
            case 9:
                service.load()
                print("📂 Expenses loaded successfully\n")

            case _:
                print("❌ Invalid option")

    except Exception as e:
        print("Error:", e)


# -------------------------
# Program Start
# -------------------------
print("=================================")
print("----- Expense Tracker -----")
print("=================================")

while True:
    try:
        print("=================================")
        print("     📘 Expense Tracker Menu")
        print("=================================")
        print("1. ➕  Add Expense")
        print("2. 📊  Show Total per Category")
        print("3. 💰  Show Total Expenses")
        print("4. 🗑️   Delete Expense")
        print("5. ✏️   Update Expense")
        print("6. 🔎  Search by Category")
        print("7. 📅  Search by Date")
        print("8. 💾  Save Expenses")
        print("9. 📂  Load Expenses")
        print("0. 🚪  Exit")
        print("=================================")

        n = int(input("Enter choice: "))
        print()

        if n == 0:
            print("Exiting Expense Tracker. Goodbye!")
            print("-" * 40)
            break

        expense_tracker(n)

    except Exception as e:
        print("Error:", e)
