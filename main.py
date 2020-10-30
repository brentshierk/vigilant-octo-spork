class BankAccount:
    def __init__(self,full_name,account_number,routing_number,balance):
        self.full_name = full_name
        self.account_number = account_number
        self.routing_number =routing_number
        self.balance = balance
    
    def deposit(self,amount,balance):
        pass

    def withdraw(self,amount,balance):
        pass
    
    def get_balance(self,balance):
        print('your balance is :')
        return balance
    
    def add_intrest(self,balance):
        pass
    
    def print_receipt(self,):
        pass
    
    