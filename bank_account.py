

class BankAccount():

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdrawal(self, amount):
        self.balance -= amount
        return self

    def display_acount_info(self):
        return f"Balance: ${round(self.balance)}"

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
            return self
        else:
            print(f"You're balance must be more than 0 to earn interest")

class User():
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = {"checking": BankAccount(int_rate=0.02, balance = 0),
                        "savings": BankAccount(int_rate=0.02, balance= 0)}
    
    def displayUserBalance(self):
        print(f"User: {self.name} Checking Balance: {self.account['checking'].display_acount_info()}")
        print(f"User: {self.name} Savings Balance: {self.account['savings'].display_acount_info()}")
        return self



joe = User('Joe', 'Joemail')

joe.account['checking'].deposit(300)
joe.account['savings'].deposit(700)

joe.displayUserBalance()







