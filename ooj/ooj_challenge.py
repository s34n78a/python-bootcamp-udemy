class Account:

    def __init__(self, name, amount):
        self.name = name
        self.balance = amount
    
    def __str__(self):
        return f'Account owner:\t {self.name}\nAccount balance: ${self.balance}'

    def deposit(self, new_deposit):
        self.balance += new_deposit
        print('Deposit Accepted')

    def withdraw(self, new_withdraw):
        if self.balance >= new_withdraw:
            self.balance -= new_withdraw
            print('Withdrawal Accepted')
        else:
            print('Funds Unavailable!')

acct1 = Account('Jose',100)
print(acct1)
print(acct1.name)
print(acct1.balance)
acct1.deposit(50)
acct1.withdraw(75)
acct1.withdraw(500)