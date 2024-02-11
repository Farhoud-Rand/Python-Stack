# We have a User class and a BankAccount class, and the user has a bank account
# So there is a has a relationship (association) between the user and the bank account
# What this means is that, instead of keeping track of a balance directly in the User class,
# we'll encapsulate all the bank account information and associate a user with a specific instance of a Bank Account.

from BankAccount import BankAccount
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = {}  # Create a dictionary of accounts

    # Adding the adding_account method to add new account for the user accounts
    def adding_account(self, account_name, int_rate=0.02):
        self.accounts[account_name] = BankAccount(int_rate)
        return self

    # Adding the deposit method to increases the user account balance by the passed amount
    def make_deposit(self, amount, account_name):
        if account_name in self.accounts:
            self.accounts[account_name].deposit(amount)
        else:
            print(f"Error in deposit operation: this account \"{account_name}\" is not a valid account name please try again")
        return self

    # Adding the make_withdrawal method to decrease the user's balance by the amount specified
    def make_withdrawal(self, amount, account_name):
        if account_name in self.accounts:
            self.accounts[account_name].withdraw(amount)
        else:
            print(f"Error in make withdrawal operation: this account \"{account_name}\" is not a valid account name please try again")
        return self

    # Adding the display_user_balance method to print the user's name and account balance to the terminal
    # eg. "User: Guido van Rossum, Balance: $150"
    def display_user_balance(self):
        print(f"\nUser {self.name} Account/s:")
        for account in self.accounts:
            print(f"\t Account_name:{account} \t\t Balance: ${self.accounts[account].balance}")
        return self

    # Adding the transfer_money method to decrease the user's balance by the amount and add that amount to other other_user's balance
    def transfer_money(self, other_user, amount, my_account, other_account):
        if (my_account in self.accounts) and (other_account in other_user.accounts):
            self.accounts[my_account].withdraw(amount)
            other_user.accounts[other_account].deposit(amount)
        else:
            print(f"Error in transfer operation: please enter a valid account names")
        return self