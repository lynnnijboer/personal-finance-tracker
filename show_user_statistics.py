def show_user_statistics(current_user, balance):
    if current_user:
        print("\n[User statistics]")

        for key, values in current_user.items():
            print(f"Name: {values['user_name']}")
            print(f"Income: {values['user_income']} euro")
        if balance:
            print("\n[User incomes and expenses]")
            for items in balance:
                print(f"{items[0]} euro ({items[1]})")
    else:
        print("No user has been selected.")