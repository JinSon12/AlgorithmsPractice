"""
더 복잡한 은행 설계 

OOP design 

복습 
함수 정리하기. 
다른 방법 생각해보기 

"""

from collections import deque

import sys
input = sys.stdin.readline


class Account:
    def __init__(self, name, transferLim, transferWin) -> None:
        self.name = name
        self.transferLim = transferLim
        self.transferWin = transferWin
        self.balance = 0
        self.history = deque([])
        self.transferCount = 0

    def addTrxn(self):
        self.history.append(1)

        if len(self.history) > 10:
            val = self.history.popleft()
            self.transferCount -= val

    def isFraud(self) -> bool:
        if sum(self.history) > self.transferLim:
            return True
        return False

    def deposit(self, amt, transfer):
        self.balance += amt

        if transfer:
            self.history.append(1)
            self.transferCount += 1
        else:
            self.history.append(0)

    def withdrawal(self, amt, transfer=False):
        self.balance -= amt

        if transfer:
            self.history.append(1)
            self.transferCount += 1
        else:
            self.history.append(0)


class Bank:
    def __init__(self) -> None:
        self.accounts = {}
        self.flagged = []
        self.trxnWindow = 0
        self.transferLim = 0
        self.trxn = deque([])

    def getTransferLim(self):
        return self.transferLim

    def printAccounts(self):
        for k, a in self.accounts.items():
            print("=====printing accounts=====")
            print("name :", a.name)
            print("balance :", a.balance)
            print("history :", a.history)
            print("transfer count :", a.transferCount)

    def printSuspiciousAccount(self):
        print()
        if len(self.flagged) == 0:
            print("EMPTY")
        else:
            print(*self.flagged)
        print()

    def addAccount(self, name, transferLim, transferWin):
        if name not in self.accounts:
            self.accounts[name] = Account(name, transferLim, transferWin)

    def checkFraud(self, name):
        if name in self.accounts:
            isFraud = self.accounts[name].isFraud()

            if isFraud:
                self.flagged.append(name)

    def inp(self):
        N = int(input())
        self.transferLim = int(input())
        self.trxnWindow = int(input())

        while True:
            line = list(input().strip().split(","))
            if line == [""]:
                break

            self.trxn.append(line)

            if line[0] == "transfer":
                self.addAccount(line[1], self.transferLim, self.trxnWindow)
                self.addAccount(line[2], self.transferLim, self.trxnWindow)
            else:
                self.addAccount(line[1], self.transferLim, self.trxnWindow)

        L = len(self.trxn)
        DEPOSIT = "deposit"
        WITHDRAW = "withdraw"
        TRANSFER = "transfer"

        for i in range(1, L+1):
            poppedlist = self.trxn.popleft()

            act = poppedlist[0]

            if act == TRANSFER:
                sender = poppedlist[1]
                receiver = poppedlist[2]
                amt = int(poppedlist[3])

                self.accounts[sender].withdrawal(amt, True)
                self.accounts[receiver].deposit(amt, True)

                self.checkFraud(sender)
                self.checkFraud(receiver)

            else:
                name = poppedlist[1]
                amt = poppedlist[2]

                if act == DEPOSIT:
                    self.accounts[name].deposit(int(amt), False)

                if act == WITHDRAW:
                    print(name, amt)
                    self.accounts[name].withdrawal(int(amt), False)

            if i % N == 0 or i == L:
                self.printAccounts()
                self.printSuspiciousAccount()


"""
TC 
3
4
5
deposit,1,100
withdraw,2,100
transfer,1,2,100
transfer,1,3,100
deposit,2,100


TC2 
5
3
5
deposit,1,200
transfer,1,2,200
deposit,2,200
transfer,2,1,200
transfer,1,3,100
transfer,1,2,100
transfer,3,2,100

"""
b = Bank()
b.inp()
