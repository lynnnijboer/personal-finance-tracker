def print_existing_users(existing_users):
    if existing_users:
        print("\n[Users]")
        for index, user in enumerate(existing_users):
            print(f"{index + 1}: ", end="")
            for user_key, user_value in user.items():
                print(f"{user_value['user_name']}")
    else:
        print("There are no users made yet!")
    return existing_users
