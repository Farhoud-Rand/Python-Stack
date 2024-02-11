from User import User

# Create instances of the User class
guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
rand = User("Rand", "rand@gmail.com")

guido.adding_account("account1")
monty.adding_account("account1",0.05)
rand.adding_account("account1")
rand.adding_account("account2")

# Have users make deposits, withdrawals, and transfers
guido.make_deposit(account_name="account1", amount=1000).make_deposit(account_name="account1",amount=250).make_deposit(account_name="account1",amount=50).make_withdrawal(account_name="account1",amount=1000).display_user_balance() # account1 --> balance: $300
monty.make_deposit(account_name="account1", amount=250).make_deposit(account_name="account1",amount=550).make_withdrawal(account_name="account1",amount=100).make_withdrawal(account_name="account1",amount=250).display_user_balance() # account1 --> balance: $450
rand.make_deposit(account_name="account2",amount=100).make_deposit(account_name="account3", amount=500).make_deposit(account_name="account1", amount=1500).make_withdrawal(account_name="account1",amount=100).make_withdrawal(account_name="account5",amount=250).make_withdrawal(account_name="account1",amount=50).display_user_balance()# account1 --> balance: $1350, account2 --> balance: $100

# Transfer money from rand account1 to rand account2 and display balances
rand.transfer_money(other_user= rand, amount=50,my_account="account1", other_account="account2").display_user_balance()# account1 --> balance: $1300, account2 --> balance: $150
rand.transfer_money(other_user= guido, amount=50,my_account="account1", other_account="account2").display_user_balance()# Error in transfer operation: please enter a valid account names

# Test display_account_info method
monty.accounts["account1"].display_account_info() # Output= Balance: $450
guido.accounts["account1"].display_account_info() # Output= Balance: $300
rand.accounts["account1"].display_account_info()  # Output= Balance: $1300
rand.accounts["account2"].display_account_info()  # Output= Balance: $150

# Test yield_interest method
monty.accounts["account1"].yield_interest()
rand.accounts["account1"].yield_interest()
monty.display_user_balance() # account1 --> balance: $472.5
rand.display_user_balance()  # account1 --> balance: $1326.0, account2 --> balance: $150