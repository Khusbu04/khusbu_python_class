addition
def sum(*args):
    result = 0
    for number in args:
        result += number
    return result
def diff(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
print(sum(1,2,3,4,5))

multiplication

def mul(*args):
    result = 1
    for number in args:
        result *= number
    return result
def diff(a,b):
    return a-b
def sum(a,b):
    return a+b
def div(a,b):
    return a/b
print(mul(1,2,3,4,5))