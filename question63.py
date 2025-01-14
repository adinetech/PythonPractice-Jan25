## Encapsulation: Create a class with a private attribute _balance and provide get_balance() and set_balance() methods.

class Account:
    def __init__(self, balance):
        self._balance = balance

    def get_balance(self):
        return self._balance

    def set_balance(self, balance):
        self._balance = balance


account = Account(100)
print(account.get_balance())
account.set_balance(200)
print(account.get_balance())