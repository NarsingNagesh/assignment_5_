class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance

    def withdrawal(self, amount):
        if self.balance >= amount:
            self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def getBalance(self):
        return self.balance
    
class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate

    def interestAmount(self):
        return (self.balance * self.interestRate) / 100
    
my_account = Account("Ashish", 2000)

print("Title : " , my_account.title)

print("balance : " , my_account.balance) 
    
my_account = SavingsAccount("Ashish", 2000, 5)

my_account.deposit(500)

print("after deposit : " , my_account.getBalance()) 

my_account.withdrawal(500)

print("after withdrawal : " , my_account.getBalance())

print("interst_amount : " , my_account.interestAmount()) 