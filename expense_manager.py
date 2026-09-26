# import json

# FILE_NAME = "expenses.json"


# def load_expenses():
#     try:
#         with open(FILE_NAME, "r") as file:
#             return json.load(file)

#     except (FileNotFoundError, json.JSONDecodeError):
#         return []


# def save_expenses(expenses):
#     with open(FILE_NAME, "w") as file:
#         json.dump(expenses, file, indent=4)


# def add_expense(expenses, amount, category, description):
#     expense = {
#         "id": len(expenses) + 1,
#         "amount": amount,
#         "category": category,
#         "description": description
#     }

#     expenses.append(expense)
#     save_expenses(expenses)

#     print("\nExpense added successfully!")


# def view_expenses(expenses):
#     if not expenses:
#         print("\nNo expenses found.")
#         return

#     print("\n========== EXPENSES ==========")

#     for expense in expenses:
#         print(f"ID: {expense['id']}")
#         print(f"Amount: ₹{expense['amount']:.2f}")
#         print(f"Category: {expense['category']}")
#         print(f"Description: {expense['description']}")
#         print("------------------------------")


# def search_expenses(expenses, keyword):
#     results = []

#     for expense in expenses:
#         if (keyword.lower() in expense["category"].lower()
#                 or keyword.lower() in expense["description"].lower()):
#             results.append(expense)

#     if not results:
#         print("\nNo matching expenses found.")
#         return

#     print("\n========== SEARCH RESULTS ==========")

#     for expense in results:
#         print(f"ID: {expense['id']}")
#         print(f"Amount: ₹{expense['amount']:.2f}")
#         print(f"Category: {expense['category']}")
#         print(f"Description: {expense['description']}")
#         print("------------------------------")


# def delete_expense(expenses, expense_id):
#     for expense in expenses:
#         if expense["id"] == expense_id:
#             expenses.remove(expense)
#             save_expenses(expenses)

#             print("\nExpense deleted successfully!")
#             return

#     print("\nExpense ID not found.")


# def calculate_total(expenses):
#     total = sum(expense["amount"] for expense in expenses)

#     print(f"\nTotal Expenses: ₹{total:.2f}")



import json

FILE_NAME = "expenses.json"


def load_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense(expenses, amount, category, description):
    # Generate a unique ID
    if expenses:
        new_id = max(expense["id"] for expense in expenses) + 1
    else:
        new_id = 1

    expense = {
        "id": new_id,
        "amount": amount,
        "category": category,
        "description": description
    }

    expenses.append(expense)
    save_expenses(expenses)

    print("\nExpense added successfully!")


def view_expenses(expenses):
    if not expenses:
        print("\nNo expenses found.")
        return

    print("\n========== EXPENSES ==========")

    for expense in expenses:
        print(f"ID: {expense['id']}")
        print(f"Amount: ₹{expense['amount']:.2f}")
        print(f"Category: {expense['category']}")
        print(f"Description: {expense['description']}")
        print("------------------------------")


def search_expenses(expenses, keyword):
    results = []

    for expense in expenses:
        if (
            keyword.lower() in expense["category"].lower()
            or keyword.lower() in expense["description"].lower()
        ):
            results.append(expense)

    if not results:
        print("\nNo matching expenses found.")
        return

    print("\n========== SEARCH RESULTS ==========")

    for expense in results:
        print(f"ID: {expense['id']}")
        print(f"Amount: ₹{expense['amount']:.2f}")
        print(f"Category: {expense['category']}")
        print(f"Description: {expense['description']}")
        print("------------------------------")


def delete_expense(expenses, expense_id):
    for expense in expenses:
        if expense["id"] == expense_id:
            expenses.remove(expense)
            save_expenses(expenses)

            print("\nExpense deleted successfully!")
            return

    print("\nExpense ID not found.")


def calculate_total(expenses):
    total = sum(expense["amount"] for expense in expenses)

    print(f"\nTotal Expenses: ₹{total:.2f}")

