# Example 7: Encapsulation
class BankAccount:
    def __init__(self, name):
        self._balance = 0
        self.name = name
    def deposit(self, amount):
        self._balance += amount
    def withdraw(self, amount):
        self._balance -= amount
    def get_balance(self):
        return self._balance
    def __str__(self):
        return f"Name: {self.name} and Balance: Hidden"
# Example 8: Using encapsulation
grace = BankAccount("Grace")
grace.deposit(1000)
print(grace)
print(grace.get_balance()) # Output: 1000 billion
grace.withdraw(100) # Output: 100
grace.deposit(999) # output: 999
grace.withdraw(200) # output: 200
print(grace.get_balance())