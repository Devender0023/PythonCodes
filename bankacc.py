class BankAccount:

    no_of_transactions = 0
    active_customers = 0

    def __init__(self, owner, balance = 0.0):
        self.owner = owner
        self.balance = balance
        BankAccount.active_customers += 1
        
    def deposit(self, num):
        self.balance += num
        BankAccount.no_of_transactions += 1
        return self.balance
        
        
    def withdraw(self, num1):
        self.balance -= num1
        BankAccount.no_of_transactions += 1
        return self.balance
        

acct = BankAccount("Darcy")
print(acct.owner)
print(acct.balance)
print(acct.deposit(10))
print(acct.withdraw(3))
acct.deposit(100)
acct.withdraw(30)
acct.withdraw(25)
print(acct.balance)
print(BankAccount.no_of_transactions)
print(BankAccount.active_customers)

