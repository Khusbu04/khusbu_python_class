user_choice = input("""
1. Circle
2. Rectangle
3. Triangle
""")
if user_choice == "1":
    user_radius = float(input("Enter Radius"))
    result_area = 3.14 * user_radius ** 2
    result_perimeter = 2 * 3.14 * user_radius
    print(f"Area = {result_area}")
    print(f"Perimeter = {result_perimeter}")
elif user_choices == "2":
    user_length = float(input("Enter Length"))
    user_width = float(input("Enter Width"))
    result_area = user_length * user_width
    result_perimeter = 2 * (user_length + user_width)
    print(f"Area = {result_area}")
    print(f"Perimeter = {result_perimeter}")
elif user_choices == "3":
    user_base = float(input("Enter Base"))
    user_height = float(input("Enter Height"))
    result_area = 0.5 * user_base * user_height
    result_perimeter = user_base + user_height
    print(f"Area = {result_area}")
    print(f"Perimeter = {result_perimeter}")
else:
    print("Invalid Input")