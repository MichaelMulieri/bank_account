
# class User():
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#         self.account = BankAccount(int_rate=0.02, balance = 0)

class BankAccount():
    def __init__(self, int_rate):
        self.int_rate = int_rate
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdrawal(self, amount):
        self.balance -= amount
        return self

    def display_acount_info(self):
        print(f"Balance: ${round(self.balance)}")

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
            return self
        else:
            print(f"You're balance must be more than 0 to earn interest")


account_one = BankAccount(0.03)
account_two = BankAccount(0.01)

account_one.deposit(700).deposit(500).deposit(150).withdrawal(100).yield_interest().display_acount_info()
account_two.deposit(300).deposit(500).withdrawal(25).withdrawal(50).withdrawal(70).withdrawal(40).yield_interest().display_acount_info()