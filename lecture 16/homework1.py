class BankAccount:
    def __init__(self, account_number, account_holder, initial_balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance
    def deposit_money(self, amount):
        self.balance += int(amount)
    def withdraw_money(self, amount):
        if amount <= self.balance:
            self.balance -= int(amount)
        else:
            print(f"{self.account_holder} Does Not Enough Money")



person1 = BankAccount(1234, "person1", 20)
person2 = BankAccount(4444, "person2")

person1.withdraw_money(300)

person2.deposit_money(1000)
person2.withdraw_money(400)
print(person2.balance)




