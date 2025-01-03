class NomoneyException(Exception):
    pass
class OutOfBudget(Exception):
    pass
balance = int(input("Enter a balance to withdraw: "))
try:
    if balance < 1000:
        raise NomoneyException("You have no money to withdraw")
    elif balance > 10000:
        raise OutOfBudget("You have reached your limit")
 except Exception as error:
        print((error))