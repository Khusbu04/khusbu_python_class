print("Hello world")
if 5 > 2:
    print("5 is greater")
    print("2 is smaller")
x=5
y= "Hello World"
print(id(x))
print(id(y))
print(type(x))
print(type(y)) # type check
# mero python class notes
mail = """
multi
Line
string
"""
print(mail)

d = 7.5
print(type(d))

e = int(d)
print(type(e))

a = 3
b = "2"

if a > int(b):
    print("a is greater")

    a = 1
    A = 4

    age = 8 
    age = 10 # different variables

    myObject = 5 # Camel Case
    MyObject = 5 # Pascal Case
    my_object = 5 # Snake Case

    x,y,z = "Orange", "Banana", "Mango"
    print(x)
    print(z)
    print(y)

x,y,z = ["Orange", "Bananna", "Mango"]
print(x)
print(y)
print(z)

a = True
b = False
print(a and b)
print(a or b)
print(not b)

boy_age = 19
boy_country = "Nepal"
if boy_age > 18 and boy_country =="Nepal":
    print("Boy can give licence exam in Nepal")

first_number  =  float(input("Enter your first number : "))
second_number = float(input("Enter your second number : "))

# first_number = int(first_number)
print("Addition = ", first_number + second_number)

first_number = float(input("Enter your first number : "))
second_number = float(input("Enter yout second number : "))

#first_number = int(first_number)
print("substraction = ", first_number + second_number)

x = "What's your name?"
print(x)

for x in "banana":
  print(x)

a = "Hello world !"
print("length ===", len(a))

txt = "The best things in life are free!"
print("free" in txt)

b = "Hello, World!"
print(b[2:5])

print(b.upper())
print(b.lower())
print(b.capitalize())

b = "Hello     "
print(b.strip())

b = "Hello, World!"
print(b.replace("WORLD", "Khusbu"))

z = b.split(",")
print(z)

print("Hello World")

name = input("Enter your name")

print("You have entered your name = " + name) # string concant
print(f"YOU have entered your name = {name}") # format string
print("You have entered your name = %s" % (name)) # Modulus string

user_choice = input("""
            Please choose you option
               + for Addition
               - for Subtraction
               
                   """)
if user_choice == "+":
    print("Addition = ", first_number + second_number)
elif user_choice == "-":
    print("Subtraction = ", first_number - second_number)
else:
    print("Invalid choice")