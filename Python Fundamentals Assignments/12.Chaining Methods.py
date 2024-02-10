# The aim of chaining is reduce code scope.
# In order to do it, each method must return self.
# By returning self, if we recall how functions work, each method call will now be equal to the instance that called it.
class User:                                     # Declare a class and give it name User
    def __init__(self, name, email_address):    # Constructor with 2 parameters
        self.name = name			           
        self.email = email_address		
        self.account_balance = 0		

    # Adding the deposit method to increases the user account balance by the passed amount
    def make_deposit(self, amount):
        self.account_balance += amount
        return self 
    
    # Adding the make_withdrawal method to decrease the user's balance by the amount specified
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    
    # Adding the display_user_balance method to print the user's name and account balance to the terminal
    # eg. "User: Guido van Rossum, Balance: $150"
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")
        return self
    
    # Adding the transfer_money method to decrease the user's balance by the amount and add that amount to other other_user's balance
    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        return self

# Create 3 instances of the User class
guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
rand = User("Rand", "rand@gmail.com")

# Have the first user make 3 deposits and 1 withdrawal and then display their balance
guido.make_deposit(1000).make_deposit(250).make_deposit(50).make_withdrawal(1000).display_user_balance()

# Have the second user make 2 deposits and 2 withdrawals and then display their balance
monty.make_deposit(250).make_deposit(50).make_withdrawal(100).make_withdrawal(250).display_user_balance()

# Have the third user make 1 deposits and 3 withdrawals and then display their balance
rand.make_deposit(500).make_withdrawal(100).make_withdrawal(250).make_withdrawal(50).display_user_balance()

# Add a transfer_money method; have the first user transfer money to the third user and then print both users' balances
guido.transfer_money(amount=100, other_user=rand).display_user_balance()
rand.display_user_balance()