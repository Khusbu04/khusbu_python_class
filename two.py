first_temperature = float(input("Enter celsius : "))
farhrenheit = (first_temperature* 9/5)+32
second_length = float(input("Enter meter : "))
kilometer= second_lenght/1000
third_currency = float(input("enter currency: "))
user_choice = input("""
            Please choose you a option
                t for temerature 
                l for length 
                c for currency 
    
                """)
if user_choice == " t ":
    print("temerture = ", fahrenheit)
elif user_choice == "l":
    print("length = ", meter)
else:
    print("Invalid choice")