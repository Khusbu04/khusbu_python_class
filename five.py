user_choices = input("""
1. KM to Miles
2. Miles to KM
3. Centimeter to Inch
4. Inch to Centimeter
""")
if user_choices == "1":
    user_input = float(input("Enter KM"))
    result = user_input * 0.621371
    print(f"{user_input} KM = {result} Miles")
elif user_choices == "2":
    user_input = float(input("Enter Miles"))
    result = user_input * 1.60934
    print(f"{user_input} Miles = {result} KM")
elif user_choices == "3":
    user_input = float(input("Enter Centimeter"))
    result = user_input * 0.393701
    print(f"{user_input} Centimeter = {result} Inch")
elif user_choices == "4":
    user_input = float(input("Enter Inch"))
    result = user_input * 2.54
    print(f"{user_input} Inch = {result} Centimeter")
else:
    print("Invalid Input")