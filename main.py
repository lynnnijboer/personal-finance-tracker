from balance_calculation import *
from users import *
from existing_users import *
from show_user_statistics import *
from choose_user import *

INPUT_ERROR_MSG = "Incorrect input. Please try again.\n"
FIRST_MENU_TEXT = """
Please select an option:
1. New User 
2. Choose user
3. Show user statistics
4. Add income or expense
"""


def first_menu():
    users = None
    current_user = None
    existing_users = []
    balance = []
    while True:
        try:
            print(FIRST_MENU_TEXT)
            menu_choice = int(input("Which option do you choose: "))
            if menu_choice == 1:
                users = create_new_user()
                existing_users.append(users)
                continue
            elif menu_choice == 2:
                print_existing_users(existing_users)
                current_user = choose_user(existing_users, current_user)
                continue
            elif menu_choice == 3:
                show_user_statistics(current_user, balance)
                continue
            elif menu_choice == 4:
                if current_user:
                    print("1. Add income")
                    print("2. Add expense")
                    while True:
                        option = int(input("Please choose 1 or 2: "))
                        if option == 1:
                            user_income, incomes = balance_calculation(current_user, option, balance)
                            break
                        elif option == 2:
                            user_income, expenses = balance_calculation(current_user, option, balance)
                            break
                        else:
                            print(INPUT_ERROR_MSG)
                            continue
                    continue
                else:
                    print("No user has been selected.")
                    continue
            else:
                print(INPUT_ERROR_MSG)
                continue
        except ValueError:
            print(INPUT_ERROR_MSG)
        else:
            break
    return users


def main():
    print("**Welcome to the Personal Finance Tracker**\n")
    first_menu_tuple = (first_menu())  


main()
