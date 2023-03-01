class Account:

    def __init__(self, title, balance):
        self.title = title
        self.balance = balance


class SavingsAccount(Account):

    def __init__(self, title, balance, interestRate):
        super().__init__(title, balance)
        self.interestRate = interestRate
        

# my_account = Account("Ashish", 5000)
# print(my_account.title) 
# print(my_account.balance) 

my_savings_account = SavingsAccount("Ashish", 5000, 5)
print("Title : " , my_savings_account.title) 
print("balance_amount : " , my_savings_account.balance)
print("interest_rate : " , my_savings_account.interestRate) 