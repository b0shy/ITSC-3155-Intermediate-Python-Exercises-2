from BankAccount import BankAccount

# Create a new BankAccount instance
account = BankAccount("Wally", 1000)

# Deposit money
account.deposit(500)

# Withdraw money
account.withdraw(200)

# Get balance
print(account.get_balance())