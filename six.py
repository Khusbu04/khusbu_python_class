user_choices = input("""
1. Simple Interest
2. Compound Interest
""")
if user_choices == "1":
    user_principal = float(input("Enter Principal"))
    user_rate = float(input("Enter Rate"))
    user_time = float(input("Enter Time"))
    result = (user_principal * user_rate * user_time) / 100
    print(f"Simple Interest = {result}")
elif user_choices == "2":
    user_principal = float(input("Enter Principal"))
    user_rate = float(input("Enter Rate"))
    user_time = float(input("Enter Time"))
    result = user_principal * (1 + (user_rate / 100)) ** user_time
    print(f"Compound Interest = {result}")
else:
    print("Invalid Input")