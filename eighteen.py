def print_result(*args, **kwargs):
    print(args)
    print(kwargs)
    result =0
    for number in args:
        result += number
    print(f"My full name is {kwargs['first_name']} {kwargs['last_name']} and total marks = {result}")
print_result(10,20,30,40,50, first_name="Khusbu", last_name="Singh")

def print_result(*args, **kwargs):
    print(args)
    print(kwargs)
    result =0
    for number in args:
        result += number
    print(f"My full name is {kwargs['name']} {kwargs['phone_number']}")
print_result(phone_number= 9820906148, name="Khusbu")