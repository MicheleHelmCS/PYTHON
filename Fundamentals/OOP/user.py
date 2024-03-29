#Create a file with the User class, including the __init__ and make_deposit method
class User:
    def __init__(self, name):
        self.name = name
        self.account_balance = 0
    
    def make_deposit(self, amount):
        self.account_balance += amount
        return self

#Add a make_withdrawal method to the User class
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

#Add a display_user_balance method to the User class
    def display_user_balance(self, amount):
        self.account_balance -= amount
        return self

#BONUS: Add a transfer_money method
    def transfer_money(self, amount, user):
        self.account_balance -= amount
        user.account_balance += amount
        self.display_user_balance()
        user.display_user_balance()
        return self

#Create 3 instances of the User class
michele = User("Michele Helm")
chloe = User("Chloe")
mayra = User("Mayra")

#Have the first user make 3 deposits and 1 withdrawal and then display their balance
michele.make_deposit(1200)
michele.make_deposit(800)
michele.make_deposit(1000)
michele.make_withdrawal(2000)
michele.display_user_balance()
#Have the second user make 2 deposits and 2 withdrawals and then display their balance
chloe.make_deposit(500)
chloe.make_deposit(750)
chloe.make_withdrawal(250)
chloe.display_user_balance()
#Have the third user make 1 deposits and 3 withdrawals and then display their balance  
mayra.make_deposit(5000)
mayra.make_withdrawal(250)
mayra.make_withdrawal(100)
mayra.make_withdrawal(200)
mayra.display_user_balance()

#BONUS: Have the first user transfer money to the third user and then print both users' balances
michele.transfer_money(750, mayra)