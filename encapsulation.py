class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}, New Balance: {self.__balance}")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}, New Balance: {self.__balance}")
        else:
            print("Insufficient balance or invalid amount")


account = BankAccount()
account.deposit(14560)
account.withdraw(3009)
