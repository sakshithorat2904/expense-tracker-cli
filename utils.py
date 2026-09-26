# def get_valid_amount():
#     while True:
#         try:
#             amount = float(input("Enter amount: "))

#             if amount <= 0:
#                 print("Amount must be greater than 0.")
#             else:
#                 return amount

#         except ValueError:
#             print("Invalid amount. Please enter a number.")


# def get_valid_category():
#     while True:
#         category = input("Enter category: ").strip()

#         if category:
#             return category

#         print("Category cannot be empty.")


# def get_valid_description():
#     while True:
#         description = input("Enter description: ").strip()

#         if description:
#             return description

#         print("Description cannot be empty.")

def get_valid_amount():
    while True:
        try:
            amount = float(input("Enter amount: "))

            if amount <= 0:
                print("Amount must be greater than 0.")
            else:
                return amount

        except ValueError:
            print("Invalid amount. Please enter a number.")


def get_valid_category():
    while True:
        category = input("Enter category: ").strip()

        if category:
            return category

        print("Category cannot be empty.")


def get_valid_description():
    while True:
        description = input("Enter description: ").strip()

        if description:
            return description

        print("Description cannot be empty.")