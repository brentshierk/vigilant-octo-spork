class BankAccount:
    balance = 0

    def __init__(self,full_name,account_number,routing_number,balance):
        self.full_name = full_name
        self.account_number = account_number
        self.routing_number =routing_number
        self.balance = 0
    
    def deposit(self,amount,balance):
        new_balance = amount + balance 
        self.balance = new_balance
        print(f'you complated your deposit of {amount}')

    def withdraw(self,balance,amount):
        new_balance = balance - amount
        balance = new_balance
    
    def get_balance(self,balance):
        print('your balance is :')
        return balance
    
    def add_intrest(self,balance):
        print('poop')
    
    def print_receipt(self):
        print(Brent_BankAccount.full_name)
        print('account number:',Brent_BankAccount.account_number)
        print('routing number:',Brent_BankAccount.routing_number)
        print(Brent_BankAccount.balance)

Brent_BankAccount = BankAccount('Brent Shierk', 1111,1212,0)

Brent_BankAccount.deposit(20,0)
print(Brent_BankAccount.deposit(20,0))
Brent_BankAccount.print_receipt()
Brent_BankAccount.withdraw(Brent_BankAccount.balance,100)
print(Brent_BankAccount.balance)




    
    