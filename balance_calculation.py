def balance_calculation(current_user, option, balance):
    for key, values in current_user.items():
        user_income = float(values["user_income"])
        amount = input("Please enter a new income: ").replace(",", ".")
        amount = float(amount)
        description = input("What is the description? ")
        if option == 1:
            user_income += amount
            print(f"{amount} euro has been added to balance.")
        elif option == 2:
            user_income -= amount
            print(f"{amount} euro has been subtracted from balance.")
        values["user_income"] = user_income
        income_entry = (round(amount, 2), description)
        balance.append(income_entry)
    return user_income, balance
