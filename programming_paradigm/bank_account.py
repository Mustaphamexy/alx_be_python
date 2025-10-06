class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
            return False
        elif amount > self.account_balance:
            print("Insufficient funds.")
            return False
        else:
            self.account_balance -= amount
            return True

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")
