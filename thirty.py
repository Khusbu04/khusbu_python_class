def natural_number():
    n =  1
    while True:
        yield n
        n += 1
# Example usage:
gen = natural_number()
for _ in range(10): # Print the first 10 natural numbers
    print(next(gen))