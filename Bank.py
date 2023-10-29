from User import User
from Admin import Admin
import time


class Bank:
    totalBalance = 0
    totalLoan = 0

    def __init__(self):
        self.user_list = []
        self.admin_list = []
        self.loan_list = []
        self.loan_feature = True
        self.AcNo = []
        self.Deposits = {}
        self.Loans = {}
        self.Transactions = {}
        self.HasUser = {}
        self.HasAdmin = {}

    def toggleLoanFeature(self, user):
        if user.power == 1:
            self.loan_feature = not self.loan_feature
            print("Loan feature is now", self.loan_feature)
        else:
            print("You don't have permission to do this.")

    def createAdmin(self, name, password, account):
        self.admin_list.append(Admin(name, password, account))

    def createUser(self, new_user, name, password, account):
        if (name in self.HasUser.keys()):
            print("User already exists!")
            return
        if (self.AcNo == []):
            account = 1
        else:
            account = self.AcNo[-1] + 1
        print("Your account number is", account)
        new_user.account = account
        self.user_list.append(new_user)
        self.Deposits[account] = 0
        self.Loans[account] = 0
        self.AcNo.append(account)
        if new_user.account not in self.Transactions:
            self.Transactions[new_user.account] = []

        self.Transactions[new_user.account] = [
            self.Transactions[new_user.account]]
        self.Transactions[account] = [
            "Account Created at Time"+str(time.time())]
        self.HasUser[name] = True
        return account

    def totalLoan(self, user):
        if user.power == 1:
            return self.totalLoan
        else:
            return -1

    def getTotalLoan(self, user):
        if user.power == 1:
            return self.totalLoan
        else:
            return -1

    def TakeLoan(self, user, amount):
        if (self.loan_feature == False):
            print("Loan feature is disabled!")
            return -1
        if (amount <= self.Deposits[user.account]*2):
            self.Loans[user.account] = amount
            self.totalLoan += amount
            self.totalBalance -= amount
            self.Transactions[user.account].append("Loan taken of " +
                                                   str(amount)+"at Time"+str(time.time()))
            return 1
        else:
            print("Insufficient balance or take less loan!")
            return 0

    def deposit(self, user, amount):
        print(user.account, user.name, user.password, user.power)
        self.Transactions[user.account] .append("Deposit added of " +
                                                str(amount)+"at Time"+str(time.time()))
        self.Deposits[user.account] += amount
        self.totalBalance += amount

    def check_balance(self, user):
        return self.Deposits[user.account]

    def check_loan(self, user):
        return self.Loans[user.account]

    def withdraw(self, user, amount):
        if (self.Deposits[user.account] >= amount and self.totalBalance < amount):
            print("Bank is in bankrupt!")
            return -1
        if self.Deposits[user.account] >= amount:
            self.Transactions[user.account].append("Withdrawn of " +
                                                   str(amount)+"at Time"+str(time.time()))
            self.Deposits[user.account] -= amount
            self.totalBalance -= amount
            return 1
        else:
            print("Insufficient balance!")
            return 0

    def transfer(self, user, amount, account):
        if (self.Deposits[user.account] >= amount and self.totalBalance < amount):
            print("Bank is in bankrupt!")
            return -1
        if self.Deposits[user.account] >= amount:
            self.Transactions[user.account].append("Transfered of " +
                                                   str(amount)+"at Time"+str(time.time()) +
                                                   "to "+str(account)+" account")
            self.Deposits[user.account] -= amount
            self.Deposits[account] += amount
            return 1
        else:
            print("Insufficient balance!")
            return 0

    def check_transaction(self, user):
        for transaction in self.Transactions[user.account]:
            print(transaction)

    def GetTotalBalance(self, user):
        print(user.name, user.password, user.power)
        if user.power == 1:
            return self.totalBalance
        else:
            return -1

    def LoginAdmin(self, name, password):
        for admin in self.admin_list:
            if admin.name == name and admin.password == password:
                return admin
        return None

    def LoginUser(self, name, password):
        for user in self.user_list:
            if user.name == name and user.password == password:
                return user
        return None

    def createAdmin(self, admin, name, password, power):
        if (name in self.HasAdmin.keys()):
            print("Admin already exists!")
            return
        if (admin.power == 1):
            self.admin_list.append(Admin(name, password, power))
            self.HasAdmin[name] = True
        else:
            print("You don't have permission to do this.")
