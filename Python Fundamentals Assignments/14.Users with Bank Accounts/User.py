# We have a User class and a BankAccount class, and the user has a bank account
# So there is a has a relationship (association) between the user and the bank account
# What this means is that, instead of keeping track of a balance directly in the User class,
# we'll encapsulate all the bank account information and associate a user with a specific instance of a Bank Account.

from BankAccount import BankAccount
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0) # Create an instance of BankAccount for each user


    # Adding the deposit method to increases the user account balance by the passed amount
    def make_deposit(self, amount):	
        self.account.deposit(amount)
        return self
    
    # Adding the make_withdrawal method to decrease the user's balance by the amount specified
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    # Adding the display_user_balance method to print the user's name and account balance to the terminal
    # eg. "User: Guido van Rossum, Balance: $150"
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account.balance}")
        return self

    # Adding the transfer_money method to decrease the user's balance by the amount and add that amount to other other_user's balance
    def transfer_money(self, other_user, amount):
        self.account.withdraw(amount)
        other_user.account.deposit(amount)
        return self