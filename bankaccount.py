class BankAccount:
    def __init__(self, account_number, balance, account_holder, _transaction_history):
        self.account_number = account_number
        self.balance = balance
        self.account_holder = account_holder
        self._transaction_history = []

    def deposit(self, amount):
        self._transaction_history.append("Deposit:")
        self.balance = amount

    def withdraw(self, amount):
        self._transaction_history.append("Withdraw:")
        if amount > 0:
            if amount <= self.balance:
                self.balance = amount - 50
            else:
                print("No money")
        else:
            print("Insufficient funds")

    def display_balance(self):
        print("Your balance:", self.balance)

    def get_transaction_history(self):
        return self._transaction_history



acc1 = BankAccount(1, 0, "Meow", [])
acc2 = BankAccount(1, 0, "Woof", [])
acc1.deposit(75)
acc2.deposit(200)

acc1.withdraw(100)
acc2.withdraw(45)

acc1.display_balance()
acc2.display_balance()

print(acc1.get_transaction_history())
print(acc2.get_transaction_history())