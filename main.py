from expense_manager import (
    load_expenses,
    add_expense,
    view_expenses,
    search_expenses,
    delete_expense,
    calculate_total
)

from utils import (
    get_valid_amount,
    get_valid_category,
    get_valid_description
)


def show_menu():
    print("\n================================")
    print("       EXPENSE TRACKER CLI")
    print("================================")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Search Expenses")
    print("4. Delete Expense")
    print("5. Show Total Expenses")
    print("6. Exit")
    print("================================")


def pause():
    input("\nPress Enter to return to the menu...")


def main():
    expenses = load_expenses()

    while True:
        show_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            print("\n--- ADD EXPENSE ---")

            amount = get_valid_amount()
            category = get_valid_category()
            description = get_valid_description()

            add_expense(
                expenses,
                amount,
                category,
                description
            )

            pause()

        elif choice == "2":
            print("\n--- VIEW EXPENSES ---")

            view_expenses(expenses)

            pause()

        elif choice == "3":
            print("\n--- SEARCH EXPENSES ---")

            keyword = input("Enter search keyword: ").strip()

            if keyword:
                search_expenses(expenses, keyword)
            else:
                print("Search keyword cannot be empty.")

            pause()

        elif choice == "4":
            print("\n--- DELETE EXPENSE ---")

            try:
                expense_id = int(input("Enter expense ID: "))
                delete_expense(expenses, expense_id)

            except ValueError:
                print("Invalid ID. Please enter a number.")

            pause()

        elif choice == "5":
            print("\n--- TOTAL EXPENSES ---")

            calculate_total(expenses)

            pause()

        elif choice == "6":
            print("\nThank you for using Expense Tracker!")
            print("Goodbye!")
            break

        else:
            print("\nInvalid choice. Please select 1-6.")
            pause()


if __name__ == "__main__":
    main()