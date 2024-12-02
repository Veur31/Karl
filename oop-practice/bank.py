import random
class Account:
    def __init__(self, account_number, balance = 0):
        self.account_number = account_number
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"You withdrew this amount: {amount}. New balance: {self.balance}")
                
        else:
            print("Insuffiecient balance")

def main():
    accounts = {}

    while True:
        print("1. Create account")
        print("2. Check balance")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Exit")

        choice = int(input("Enter a number: "))

        if choice == 1:
            account_number = random.randint(1999,9999)
            initial_balance = float(input("Enter initial balance: "))
            accounts[account_number] = Account(account_number, initial_balance)
            print(f"This will now be your account number: {account_number}")
        elif choice == 2 :
            account_number = int(input("Enter account number: "))
            account = accounts.get(account_number)
            if account:
                print("Balance: ", account.balance)
            else:
                print("Account not found")
        elif choice == 3:
             account_number = int(input("Enter account number: "))
             account = accounts.get(account_number)
             if account:
                 amount = float(input("Enter money to deposit: "))
                 account.deposit(amount)
                 print(f"Deposited amount: {amount}")
                 print(f"New balance: {account.balance}")
             else:
                 print("Account not found")
        elif choice == 4:
             account_number = int(input("Enter account number: "))
             account = accounts.get(account_number)
             if account:
                 amount = int(input("Enter amount to withdrew: "))
                 account.withdraw(amount)
           
             else:
                 print("No account found")
        elif choice == 5:
            print("Thank you for using our banking system: ")
            break
        else:
            print("Invalid option")

            
            
if __name__ == "__main__":
    main()



        



        