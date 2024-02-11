class BankAccount:
    def __init__(self, int_rate, balance=0):  # Add a default value for balance: 0
        self.int_rate = int_rate
        self.balance = balance

    # deposit(self, amount) - increases the account balance by the given amount
    def deposit(self, amount):
        self.balance += amount

    # withdraw(self, amount) - decreases the account balance by the given amount if there are sufficient funds;
    # if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5

    # display_account_info(self) - print to the console: eg. "Balance: $100"
    def display_account_info(self):
        print("Balance: $" + str(self.balance))

    # yield_interest(self) - increases the account balance by the current balance * the interest rate
    # (as long as the balance is positive)
    def yield_interest(self):
        if (self.balance > 0):
            self.balance = self.balance + self.balance * self.int_rate
