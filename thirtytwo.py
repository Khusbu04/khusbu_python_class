def factorial(n):
    if n == 0:
        return 1 # Base case
    return n * factorial(n - 1)
print(factorial(5)) # ouptput: 120