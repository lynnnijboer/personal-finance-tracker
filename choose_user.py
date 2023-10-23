def choose_user(existing_users, current_user):
    if existing_users:
        option = int(input(f"What user would you like to see? Please enter number 1/{len(existing_users)}: "))
        for index, user in enumerate(existing_users):
            if option == index + 1:
                current_user = user
                balance = []
                for items in user.values():
                    print(f"User {items['user_name']} has been set.")
    return current_user