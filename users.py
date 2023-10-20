def new_user_name_checker():
    while True:
        new_user_name = input("\nPlease enter your full name: ")
        for letter in new_user_name:
            if letter.isdigit():
                print("Your name can only contain letters.")
                correct_input = False
                break
            else:
                correct_input = True
        if correct_input:
            print(f"Thank you for registering, {new_user_name}!")
            break
    return new_user_name

def new_user_income_checker():
    while True:
        new_user_income = input("\nPlease enter your monthly income: ")
        for number in new_user_income:
            if not number.isdigit():
                print("Your income can only contain numbers.")
                correct_input = False
                break
            else:
                correct_input = True
        if correct_input:
            print(f"Monthly income of {new_user_income} recorded.")
            break

    return new_user_income

def create_new_user():
    users = { "user" : { "user_name" : [], "user_income" : [] } }

    new_user_name = new_user_name_checker()
    new_user_income = new_user_income_checker()
    users['user']['user_name'] = new_user_name
    users['user']['user_income'] = new_user_income

    return users