class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            return f"Deposited: ${amount:.2f}"
        else:
            return "Deposit amount must be greater than zero."

    def withdraw(self, amount):
        if amount <= 0:
            return "Withdrawal amount must be greater than zero."
        elif amount > self.account_balance:
            return "Insufficient funds."
        else:
            self.account_balance -= amount
            return f"Withdrew: ${amount:.2f}"

    def display_balance(self):
        return f"Current Balance: ${self.account_balance:.2f}"
