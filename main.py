from balance_calculation import *
from users import *
from existing_users import *

INPUT_ERROR_MSG = "Incorrect input. Please try again.\n"
FIRST_MENU_TEXT = '''
Please select an option:
1. New User 
2. Existing User
3. Show user statistics
'''

def first_menu():
# new user - ask for income, user info
# existing user - menu 2 - select user account - menu 3 - browse respective data
    users = None
    existing_users = []

    print(FIRST_MENU_TEXT)
    while True:
        try:
            menu_choice = int(input('Which option do you choose: '))
            print(FIRST_MENU_TEXT)
            if menu_choice == 1:
                users = create_new_user()
                existing_users.append(users)
                continue
                
            elif menu_choice == 2:
                print_existing_users(existing_users)
                option = int(input(f"What user do you want to see? Please enter number 1 - {len(existing_users)}: "))
                for index, user in enumerate(existing_users):
                    if option == index + 1:
                        current_user = user
                        for items in user.values():
                            print(f"User {items['user_name']} has been set.")
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
