
def deposit(balance, amount):
    if amount > 0:
        balance += amount
        print("Deposit successful!")
    else:
        print("Invalid amount!")

    return balance


def withdraw(balance, amount):
    if amount <= 0:
        print("Invalid amount!")

    elif amount > balance:
        print("Insufficient balance!")

    else:
        balance -= amount
        print("Withdrawal successful!")

    return balance


def check_balance(balance):
    print("Current Balance: Rs.", balance)


balance = 1000

balance = deposit(balance, 500)

check_balance(balance)

balance = withdraw(balance, 300)

check_balance(balance)
