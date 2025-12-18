from typing import List
from models.expense import Expense
from validators.expense_validator import ExpenseValidator






# Expense Tracker (Basic)

# Create a program where the user can:

# Add an expense (amount + category)
# View all expenses
# View total amount spent
# Store data in a list of dictionaries.



import json

from datetime import date

lst: List[Expense] = []      # list of objects
category_totals = {}


# -------------------------
# Load expenses at startup
# -------------------------
def load_expenses():
    global lst

    try:
        with open("expenses.json", "r") as f:
            data = json.load(f)

        lst = [
            Expense(
                amount=item["amount"],
                category=item["category"],
                description="N/A",
                expense_date=date.fromisoformat(item["date"])
            )
            for item in data
        ]

        print("Loaded expenses from file.\n")

    except FileNotFoundError:
        print("📁 No existing file found. Starting fresh.\n")



# -------------------------
# Save expenses
# -------------------------

def save_expenses():

    temp = []
    for exp in lst:
        temp.append({
            "category": exp.category,
            "amount": exp.amount,
            "date": exp.expense_date.isoformat()
        })

    with open("expenses.json", "w") as f:
        json.dump(temp, f, indent=4)

    print("💾 Saved to expenses.json\n")



# -------------------------
# Main Expense Tracker Logic
# -------------------------

def expense_tracker(n):
    try:
        match n:
            # -------------------------
            # 1. Add Expense
            # -------------------------
            case 1:

                try:
                    category = input("Enter the category: ").strip()
                    amount = int(input("Enter the amount: "))

                    validator = ExpenseValidator()

                    expense = Expense(
                        amount = amount,
                        category = category,
                        description = "N/A",         # temporary
                        expense_date = date.today()
                        )

                    validator.validate(expense)
                    lst.append(expense)

                    print("✅ Expense added successfully!\n")
                except ValueError as e:
                    print(f"❌ {e}")
            # -------------------------
            # 2. Show Total per Category
            # -------------------------
            case 2:
                
                category_totals.clear()

                for expense in lst:
                    cat = expense.category
                    amt = expense.amount

                    if cat in category_totals:
                        category_totals[cat] += amt
                    else:
                        category_totals[cat] = amt
                
                print(f"{'No':<5}{'Category':<15}{'Total Amount':<15}")
                print("-" * 35)
                for index, (cat, amt) in enumerate(category_totals.items(), start=1):
                    print(f"{index:<5}{cat:<15}{amt:<15}")

                print()

            # -------------------------
            # 3. Show Total Expense
            # -------------------------
            case 3:
                try:

                    print(f"{'No':<5}{'Category':<15}{'Amount':<10}{'Date'}")
                    print("-" * 40)
                    for i, expense in enumerate(lst, start=1):
                        print(f"{i:<5}{expense.category:<15}{expense.amount:<10}{expense.expense_date}")   
                    print("-" * 40) #-------------------------------------------------  

                    total = 0
                    total = sum(e.amount for e in lst)
                    print(f"Total: {total}")

                except ValueError:
                    print("Invalid input!")

                except TypeError:
                    print("Wrong inputs!!")

            # -------------------------
            # 4. Delete Expense
            # -------------------------
            case 4:
                if not lst:
                    print("❌ No expenses to delete.\n")
                    return

                print("\n📌 Expenses:")
                for i, exp in enumerate(lst, start=1):
                    print(f"{i}. {exp}")

                index = int(input("\nEnter index to delete: "))

                if index < 1 or index > len(lst):
                    print("❌ Invalid index.\n")
                else:
                    deleted = lst.pop(index - 1)
                    print(f"🗑 Deleted: {deleted}\n")

                    
            # -------------------------
            # 5. Update Expense
            # -------------------------
            case 5:
                print("All Expenses:")

                # Show all expenses with indexes
                for i, expense in enumerate(lst, start=1):
                    print(f"{i}. {expense}")

                try:
                    # Step 1: Ask which expense to update
                    index = int(input("\nEnter index of the expense you want to update: "))

                    if index < 1 or index > len(lst):
                        print("❌ Invalid index")
                        return

                    expense = lst[index - 1]   # Expense object

                    # Step 2: Ask which field to update
                    print("\nWhat do you want to update?")
                    print("1. category")
                    print("2. amount")
                    print("3. date")

                    choice = input("Enter choice: ")

                    if choice == "1":
                        new_value = input("Enter new category: ").strip()
                        expense.category = new_value

                    elif choice == "2":
                        new_value = int(input("Enter new amount: "))
                        expense.amount = new_value

                    elif choice == "3":
                        new_value_raw = input("Enter new date (YYYY-MM-DD): ")
                        expense.expense_date = date.fromisoformat(new_value_raw)

                    else:
                        print("❌ Invalid choice.")
                        return

                    print("✅ Updated Successfully\n")
                    print("Updated expense:", expense)

                except ValueError as e:
                    print(f"❌ {e}")


            # -------------------------
            # 6. Search by category
            # ------------------------
            case 6:

                try:

                    choice = input("Enter category: ")
                    matches = [item for item in lst if item.category == choice]

                    if matches:
                        for i, item in enumerate(matches, start=1):
                            print(f"{i}. {item.category} : {item.amount} on {item.expense_date}")

                    else:
                        raise KeyError(f"'{choice}' not found in expenses.")

                except ValueError:
                    print("❌ Invalid category!!")
                
                except KeyError as e:
                    print("Error: ", e)

            # -------------------------
            # 7. Search by date
            # -------------------------
            case 7:

                d = input("Enter a date (YYYY-MM-DD): ")
                    
                search_date = date.fromisoformat(d)
                result = [item for item in lst if item.expense_date == search_date]


                if result:
                    print(f"📌 Expenses found on {d} are: ")
                    for i, item in enumerate(result, start=1):
                        print(f"{i}. {item.category} : {item.amount}")
                else:
                    print(f"❌ No expenses found on {d}") 


            # -------------------------
            # 8. Save All Expenses
            # -------------------------
            case 8:
                save_expenses()
            # -------------------------
            # 9. Load from File
            # -------------------------
            case 9:
                load_expenses()
            # -------------------------
            # 0. Exit   
            # -------------------------


    except Exception as e:
        print("Error:", e)



# -------------------------
# Program Start
# -------------------------

load_expenses()
print("=================================")
print("----- Expense Tracker-----")
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
        expense_tracker(n)

    except Exception as e:
        print("Error:", e)

    if n == 0: # type: ignore
        print("Exiting Expense Tracker. Goodbye!")
        print("-" * 40) #------------------------------------------------- 
        break

