class Account:
    def __init__(self, name, initial):
        self.name = name
        self.balance = initial
        self.fees = 0
        print("%s's initial balance: £%d\n" % (self.name, self.balance))

    def deposit(self, funds):
        self.balance += funds
        if self.balance < 0:
            print("%s's new balance after deposit of £%d: (£%d)\n" % (self.name, funds, self.balance*-1))
        else:
            print("%s's new balance after deposit of £%d: £%d\n" % (self.name, funds, self.balance))

    def withdraw(self, funds):
        self.balance -= funds
        if self.balance < 0:
            self.balance -= 10
            self.fees += 10
            print("Additional fee of £10 incurred for overdraft\n")
        print("%s's new balance after withdraw of £%d: £%d\n" % (self.name, funds, self.balance))

    def get_balance(self):
        print("%s's balance is: £%d\n" % (self.name, self.balance))

    def get_fees(self):
        print("%s's account has incurred £%d in fees since it was opened\n" % (self.name, self.fees))


alice = Account("Alice", 100)
alice.deposit(20)
alice.withdraw(50)
alice.deposit(57)
alice.withdraw(200)
alice.withdraw(10)
alice.deposit(500)
alice.get_balance()
alice.get_fees()

bob = Account("Bob", 200)
bob.withdraw(250)
bob.deposit(50)
bob.deposit(50)
bob.deposit(50)
bob.deposit(100)
bob.get_balance()
bob.get_fees()