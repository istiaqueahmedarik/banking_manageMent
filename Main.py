from Bank import Bank
from User import User
from Admin import Admin

bank = Bank()


def main():
    while (1):
        print("Welcome!")
        print("1. Admin")
        print("2. User")
        print("3. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            admin = Admin("", "", "")
            while (1):
                if (admin.loggedIn == True):
                    print("Welcome!")
                    print("1. Toggle Loan Feature")
                    print("2. Check Total Balance")
                    print("3. Check Total Loan")
                    print("4. Exit")
                    choice = int(input("Enter your choice: "))
                    if choice == 1:
                        bank.toggleLoanFeature(admin)
                    elif choice == 2:
                        print("Total Balance:", str(
                            bank.GetTotalBalance(admin)))
                    elif choice == 3:
                        print("Total Loan:", str(bank.getTotalLoan(admin)))
                    elif choice == 4:
                        print("Thank you for using our service!")
                        exit()
                    else:
                        print("Invalid choice!")
                else:
                    print("1. Create Admin")
                    print("2. Login")
                    print("3. Exit")
                    choice = int(input("Enter your choice: "))
                    if choice == 1:
                        secret = input("Enter secret key: ")
                        if (secret != "ARIK"):
                            print("You are not allowed to create admin!")
                            continue
                        name = input("Enter your name: ")
                        password = input("Enter your password: ")
                        bank.createAdmin(admin, name, password, 1)
                        admin.setName(name)
                        admin.setPassword(password)

                    elif choice == 2:
                        admin.name = input("Enter your name: ")
                        admin.password = input("Enter your password: ")
                        if (bank.LoginAdmin(admin.name, admin.password) != None):
                            admin.loggedIn = True
                        else:
                            print("Invalid username or password!")
                    elif choice == 3:
                        print("Thank you for using our service!")
                        exit()
                    else:
                        print("Invalid choice!")
        elif choice == 2:
            user = User("", "", "")
            while (1):
                if (user.loggedIn == True):
                    print("Welcome!")
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. Transfer")
                    print("4. Check Balance")
                    print("5. Take Loan")
                    print("6. Check Transaction History")
                    print("7. Exit")
                    choice = int(input("Enter your choice: "))
                    if choice == 1:
                        amount = int(input("Enter amount to deposit: "))
                        bank.deposit(user, amount)
                        print("Your current balance is",
                              str(bank.check_balance(user)))
                    elif choice == 2:
                        amount = int(input("Enter amount to withdraw: "))
                        bank.withdraw(user, amount)
                    elif choice == 3:
                        amount = int(input("Enter amount to transfer: "))
                        account = int(
                            input("Enter account number to transfer: "))
                        bank.transfer(user, amount, account)
                    elif choice == 4:
                        print("Your current balance(Main Deposit:", str(bank.check_balance(
                            user))+")\n(Loan Deposit:", str(bank.check_loan(user))+")")
                    elif choice == 5:
                        amount = int(input("Enter amount to take loan: "))
                        bank.TakeLoan(user, amount)
                    elif choice == 6:
                        bank.check_transaction(user)
                    elif choice == 7:
                        print("Thank you for using our service!")
                        break
                    else:
                        print("Invalid choice!")
                else:
                    print("1. Create Account")
                    print("2. Login")
                    print("3. Exit")
                    choice = int(input("Enter your choice: "))
                    if choice == 1:
                        name = input("Enter your name: ")
                        password = input("Enter your password: ")
                        bank.createUser(user, name, password, 0)
                        user.setName(name)
                        user.setPassword(password)

                    elif choice == 2:
                        user.name = input("Enter your name: ")
                        user.password = input("Enter your password: ")
                        if (bank.LoginUser(user.name, user.password) != None):
                            user.loggedIn = True
                        else:
                            print("Invalid username or password!")
                    elif choice == 3:
                        print("Thank you for using our service!")
                        break
                    else:
                        print("Invalid choice!")

        elif choice == 3:
            print("Thank you for using our service!")
            exit()
        else:
            print("Invalid choice!")
        main()


if __name__ == "__main__":
    main()
