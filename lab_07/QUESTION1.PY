class ATM:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited: {amount}")
            print(f"Deposited: {amount}")
        else:
            print("Invalid amount. Deposit should be greater than 0.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: {amount}")
            print(f"Withdrew: {amount}")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            print("Invalid amount. Withdrawal should be greater than 0.")

    def check_balance(self):
        print(f"Current balance: {self.balance}")

    def show_transaction_history(self):
        if not self.transaction_history:
            print("No transactions available.")
        else:
            print("Transaction History:")
            for transaction in self.transaction_history:
                print(transaction)

# Example usage:
atm = ATM("John Doe")

atm.deposit(500)
atm.withdraw(200)
atm.check_balance()
atm.show_transaction_history()

atm.withdraw(400)  # Insufficient funds
atm.check_balance()
