"""
https://wikidocs.net/7037

파이썬 문제 300제

"""


import random


class Account:
    # 클래스 변수
    num_total_accounts = 0

    def __init__(self, name, balance) -> None:
        self.name = name
        self.balance = balance
        self.bank = "은행~"
        self.deposit_count = 0
        self.account_number = self._generate_account_num()
        self.trxn_count = 0
        self.log = []

        Account.num_total_accounts += 1

    def _generate_account_num(self) -> str:
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)         # 1 -> '1' -> '001'
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)

        return num1 + "-" + num2 + "-" + num3

    def deposit(self, amt):
        if amt < 1:
            print("must deposit more than 1")
            return

        self.balance += amt
        self.log.append(amt)
        self.trxn_count += 1

        if self.trxn_count % 5 == 0:
            self.balance *= 1.01

        print("deposit successful, current balance: ", self.balance)

    def withdraw(self, amt):
        if self.balance < amt:
            print("insufficient funds")
            return

        self.balance -= amt
        self.log.append(amt*-1)
        self.trxn_count += 1
        print("withdrawal successful, balance: ", self.balance)

    def printInfo(self):
        print(f'bank name: {self.bank}')
        print(f'account holder name: {self.name}')
        print(f'account number: {self.account_number}')
        print(f'balance : {self.balance}')

    def history(self):
        print("==== account log ====")
        for amt in self.log:
            print(amt)

    @classmethod
    def get_account_num(cls):
        print(cls.num_total_accounts)  # = Account.num_total_accounts


accounts = []
a1 = Account("개구리", 100)  # name, balance
a2 = Account("고양이", 10)  # name, balance
print("account count", Account.num_total_accounts)
a1.get_account_num()
a1.deposit(10)
a1.withdraw(10)
a1.printInfo()
accounts.append(a1)
accounts.append(a2)
a1.deposit(100)
a1.withdraw(10)
a1.history()

for acnt in accounts:
    if acnt.balance >= 100:
        print("====person with balance greater than 100====")
        acnt.printInfo()
