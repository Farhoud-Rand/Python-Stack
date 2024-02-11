from User import User

# Create instances of the User class
guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
rand = User("Rand", "rand@gmail.com")

# Have users make deposits, withdrawals, and transfers
guido.make_deposit(1000).make_deposit(250).make_deposit(50).make_withdrawal(1000).display_user_balance() # Output= User: Guido van Rossum, Balance: $300
monty.make_deposit(250).make_deposit(550).make_withdrawal(100).make_withdrawal(250).display_user_balance() # Output= User: Monty Python, Balance: $450
rand.make_deposit(500).make_withdrawal(100).make_withdrawal(250).make_withdrawal(50).display_user_balance()# Output= User: User: Rand, Balance: $100

# Transfer money from guido to rand and display balances
guido.transfer_money(rand, 100).display_user_balance() # Output= User: Guido van Rossum, Balance: $200
rand.display_user_balance()# Output= User: Rand, Balance: $200

# Test display_account_info method
monty.account.display_account_info() # Output= Balance: $450 
guido.account.display_account_info() # Output= Balance: $200 
rand.account.display_account_info()  # Output= Balance: $200

# Test yield_interest method
monty.account.yield_interest()
rand.account.yield_interest()
monty.account.display_account_info() # Output= Balance: $459.0 
rand.account.display_account_info()  # Output= Balance: $204.0