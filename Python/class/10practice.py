class Account:
    bank_name = "Nabil Bank"
    address = "Lazimpat"

    def __init__(self, balance, account_num):
        self.balance = balance
        self.account_num = account_num

    def credit(self, amount):
        self.balance = self.balance + amount

    def debit(self, amount):
        self.balance = self.balance - amount

    def show_balance(self):
        print(f"Your current balance is Rs {self.balance}.")


A1 = Account(1000, 1234)
A2 = Account(2000, 2345)

A1.credit(100)
A2.credit(200)
A1.show_balance()
A2.show_balance()
