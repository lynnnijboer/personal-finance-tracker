from balance_calculation import *
from users import *
from existing_users import *

INPUT_ERROR_MSG = "Incorrect input. Please try again.\n"
FIRST_MENU_TEXT = '''
Please select an option:
1. New User 
2. Choose user
3. Show user statistics
4. Add income or expense
'''

def first_menu():
# new user - ask for income, user info
# existing user - menu 2 - select user account - menu 3 - browse respective data
    users = None
    current_user = None
    existing_users = []
    balance = []
    while True:
        try:
            print(FIRST_MENU_TEXT)
            menu_choice = int(input('Which option do you choose: '))
            if menu_choice == 1:
                users = create_new_user()
                existing_users.append(users)
                continue
                
            elif menu_choice == 2:
                print_existing_users(existing_users)
                if existing_users:
                    option = int(input(f"What user would you like to see? Please enter number 1/{len(existing_users)}: "))
                    for index, user in enumerate(existing_users):
                        if option == index + 1:
                            current_user = user
                            for items in user.values():
                                print(f"User {items['user_name']} has been set.")
                continue

            elif menu_choice == 3:
                if current_user:
                    print("\n[User statistics]")
                    for key, values in current_user.items():
                        print(f"Name: {values['user_name']}")
                        print(f"Income: {values['user_income']} euro")
                    if balance:
                        print("\n[User incomes and expenses]")
                        for items in balance:
                            print(f"{items[0]} euro ({items[1]})")
                    continue
                else:
                    print("No user has been selected.")
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

        except ValueError:
            print(INPUT_ERROR_MSG)
        else:
            break
    #returns new user data if 1 and existing user name for menu 2 -> need to check return to proceed
    return users #+ existing user return


def main():
    print("**Welcome to the Personal Finance Tracker**\n")
    first_menu_tuple = first_menu() #tuple used to check returns and append new user data or enter menu2 for existing user
    
main()
