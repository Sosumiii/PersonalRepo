class BankAccount:
    def __init__(self, bal):
        self.balance = bal

    def getBalance(self):
        return self.balance
    
    def deposit(self, value):
        self.balance += value

    def withdraw(self, value):
        self.balance -= value

    def __str__(self):
        msg = f"the current balance is {self.getBalance()}"
        return msg