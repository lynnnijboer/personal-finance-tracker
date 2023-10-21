def print_existing_users(existing_users):
    if existing_users:
        for index, user in enumerate(existing_users):
            print(f"[User {index + 1}]")
            for user_key, user_value in user.items():
                print(f"Name: {user_value['user_name']}")
                print(f"Income: {user_value['user_income']} euro")
            print("")
    else:
        print("There are no users made yet!")
    return existing_users