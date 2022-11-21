import uuid

def getRandomID():
    return uuid.uuid4().hex[:5]

class MyBankAccount:
    def __init__(self, amount=0):
        self.balance = amount
    def deposit(self, amount):
        self.balance = self.balance + amount
        msg = f"You deposited ${amount} in your account. Your current balance is ${self.balance}"
        f = open(f"finalProject/Transactions/Transaction #{getRandomID()}.txt", "w")
        f.write(msg)
        f.close()
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
            msg = f"You withdrew ${amount} from your account. Your current balance is ${self.balance}"
        else:
            msg = "You do not have enough money, lol"
        f = open(f"finalProject/Transactions/Transaction #{getRandomID()}.txt", "w")
        f.write(msg)
        f.close()

################################################

med = MyBankAccount(1200)
while True:
    ask = input("What do you want to do? ")
    if ask == "d":
        amount = input("How much? ")
        amount = int(amount)
        med.deposit(amount)
    elif ask == "w":
        amount = input("How much? ")
        amount = int(amount)
        med.withdraw(amount)
    else:
        print("Huh?")