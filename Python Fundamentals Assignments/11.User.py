class User:                                     # Declare a class and give it name User
    def __init__(self, name, email_address):    # Constructor with 2 parameters
        self.name = name			           
        self.email = email_address		
        self.account_balance = 0		

    # Adding the deposit method to increases the user account balance by the passed amount
    def make_deposit(self, amount):	
    	self.account_balance += amount
    
    # Adding the make_withdrawal method to decrease the user's balance by the amount specified
    def make_withdrawal(self, amount):
        self.account_balance -= amount

    # Adding the display_user_balance method to print the user's name and account balance to the terminal
    # eg. "User: Guido van Rossum, Balance: $150"
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")

    # Adding the transfer_money method to decrease the user's balance by the amount and add that amount to other other_user's balance
    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)

# Create 3 instances of the User class
guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
rand = User("Rand", "rand@gmail.com")

# Have the first user make 3 deposits and 1 withdrawal and then display their balance
guido.make_deposit(1000)
guido.make_deposit(250)
guido.make_deposit(50)
guido.make_withdrawal(1000)
guido.display_user_balance()

# Have the second user make 2 deposits and 2 withdrawals and then display their balance
monty.make_deposit(250)
monty.make_deposit(50)
monty.make_withdrawal(100)
monty.make_withdrawal(250)
monty.display_user_balance()

# Have the third user make 1 deposits and 3 withdrawals and then display their balance
rand.make_deposit(500)
rand.make_withdrawal(100)
rand.make_withdrawal(250)
rand.make_withdrawal(50)
rand.display_user_balance()

# Add a transfer_money method; have the first user transfer money to the third user and then print both users' balances
guido.transfer_money(amount=100, other_user=rand)
guido.display_user_balance()
rand.display_user_balance()

