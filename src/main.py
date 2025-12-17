# 3. Expense Tracker (Basic)

# Create a program where the user can:

# Add an expense (amount + category)
# View all expenses
# View total amount spent
# Store data in a list of dictionaries.



import json

from datetime import date

lst = []        # list of dictionaries
category_totals = {}


# -------------------------
# Load expenses at startup
# -------------------------
def load_expenses():
    global lst

    try:
        with open("expenses.json", "r") as f:
            lst = json.load(f)

        print("Loaded expenses from file.\n")
        print("📌 Expenses:")
        for i, exp in enumerate(lst, start=1):
            print(f"{i}. {exp}")

    except FileNotFoundError:
        print("📁 No existing file found. Starting fresh.\n")


# -------------------------
# Save expenses
# -------------------------

def save_expenses():
    # convert date object → string
    temp = []
    for exp in lst:
        temp.append({
            "category": exp["category"],
            "amount": exp["amount"],
            "date": exp["date"]

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
                while True:

                    category = input("Enter the category: ").strip()
                    amount = int(input("Enter the amount: "))
 
                    if not category:
                        raise ValueError("Category cannot be empty.")
                    
                    if amount > 0:
                        lst.append({"category": category, "amount": amount, "date": date.today().isoformat()})
                   
                    elif amount < 0:
                        raise ValueError("Amount cannot be negative.")
                    else:
                        print("Invalid input!")

                    print("✅ Expense added successfully!\n")

                    ask = input("Do you add more expenses? (y/n) ").lower()
                    if ask != "y":
                        break

            # -------------------------
            # 2. Show Total per Category
            # -------------------------
            case 2:
                
                category_totals.clear()

                for expense in lst:
                    cat = expense["category"]
                    amt = expense["amount"]

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
                        print(f"{i:<5}{expense['category']:<15}{expense['amount']:<10}{expense['date']}")   
                    print("-" * 40) #-------------------------------------------------  

                    total = 0
                    total = sum(e["amount"] for e in lst)
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

                # Step 1: Ask which dictionary (expense) to update
                index = int(input("\nEnter index of the expense you want to update: "))

                if index < 1 or index > len(lst):
                    print("Invalid index")
                else:
                    d = lst[index-1]     # this is the dictionary to update

                    # Step 2: Ask which field to update
                    print("\nWhat do you want to update?")
                    print("1. category")
                    print("2. amount")
                    print("3. date")

                    choice = input("Enter choice: ")

                    key_map = {
                        "1": "category",
                        "2": "amount",
                        "3": "date"
                    }

                    if choice in key_map:
                        key = key_map[choice]

                        if key == "amount":
                            new_value = int(input(f"Enter new value for '{key}': "))

                        elif key == "date":
                            new_value_raw = input(f"Enter new value for '{key}'(YYYY-MM-DD): ")
                            
                            try:
                                new_value = date.fromisoformat(new_value_raw).isoformat()
                            except:
                                print("Invalid date format. Use YYYY-MM-DD.")
                                return
                            
                        else:     
                            new_value = input(f"Enter new value for '{key}': ")

                        d[key] = new_value   # updates the SAME object inside list

                        print("✅ Updated Successfully\n")
                        print("Updated expense:", d)
         
                    else:
                        print("❌ Invalid choice.\n")

            # -------------------------
            # 6. Search by category
            # ------------------------
            case 6:

                try:

                    choice = input("Enter category: ")
                    matches = [item for item in lst if item["category"] == choice]

                    if matches:
                        for i, item in enumerate(matches, start=1):
                            print(f"{i}. {item['category']} : {item['amount']} on {item['date']}")

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
                    
                result = [item for item in lst if item["date"] == d]
                    
                if result:
                    print(f"📌 Expenses found on {d} are: ")
                    for i, item in enumerate(result, start=1):
                        print(f"{i}. {item['category']} : {item['amount']}")
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

    if n == 0:
        print("Exiting Expense Tracker. Goodbye!")
        print("-" * 40) #------------------------------------------------- 
        break

