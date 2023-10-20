from balance_calculation import *
from users import *

INPUT_ERROR_MSG = "Incorrect input. Please try again.\n"
FIRST_MENU_TEXT = '''
Please select an option:
 1. New User 
 2. Existing User
 3. ?
'''

def first_menu():
# new user - ask for income, user info
# existing user - menu 2 - select user account - menu 3 - browse respective data
    print(FIRST_MENU_TEXT)
    while True:
        try:
            menu_choice = int(input('Which option do you choose: '))
            if menu_choice == 1:
                users = create_new_user()
                print(FIRST_MENU_TEXT)
                continue
            elif menu_choice == 2:
                pass
            else:
                print(INPUT_ERROR_MSG)
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
