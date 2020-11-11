from random import randrange

class BankAccount():
    routing_number =randrange(00000000,100000000)

    

    def __init__(self,full_name,):
        self.full_name = full_name
        self.account_number = randrange(00000000,100000000)
        self.balance = 0
    
    def deposit(self,amount):
        new_balance = amount + self.balance 
        self.balance = new_balance
        print(f'you complated your deposit of {amount}')

    def withdraw(self,amount):
        new_balance = self.balance - amount
        self.balance = new_balance
        return self.balance
    
    def get_balance(self,):
        print(f"your balance is :{self.balance}")
        return self.balance
    
    def add_intrest(self):
        intrest = self.balance * 0.00083
        new_balance = self.balance + intrest
        self.balance = new_balance
        return self.balance
    
    def print_receipt(self):
        print(self.full_name)
        print('account number:',self.account_number)
        print('routing number:',self.routing_number)
        print(self.balance)

Brent_BankAccount = BankAccount('Brent Shierk')
stephanie = BankAccount('Stephanie')

Brent_BankAccount.deposit(200)
Brent_BankAccount.withdraw(40)
Brent_BankAccount.get_balance()




    
    