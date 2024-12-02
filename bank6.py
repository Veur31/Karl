import random
class Bankaccount():
    x = random.randint(1000,2000)
    def __init__(self, first_name, last_name, password, balance = 0):
        self.account_number = str(Bankaccount.x)
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} into account {self.account_number} Current balance: {self.balance}")
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount} from account {self.account_number} Current balance{self.balance}")
    def check_balance(self):
        print(f"Account number {self.account_number}. Balance: {self.balance}")   
    def change_password(self, new_password):
        self.password = new_password
        print("password change successfully")
def create_account():
    fname = input("Enter your first name: ")
    lname = input("Enter your last name: ")
    password = input("Enter your password: ")
    return Bankaccount(fname, lname, password)
def main():
    acc = {}
    while True:
        print("\nBanking System Menu: ") 
        print("1. Open an account") 
        print("2. Deposit") 
        print("3. Withdraw") 
        print("4. Balance Inquiry") 
        print("5. Change password") 
        print("6. Exit")  
        choice = input("Enter your choice: ")  

        if choice == "1":
            ac = create_account()
            acc[ac.account_number] = ac
            acc[ac.password] = ac
            print(f"Your account made successfully {ac.account_number}")
        elif choice == "2":
            user = input("Enter your account number: ")
            password = input("Enter your password: ")
            if user and password in acc:
                amount = int(input("Enter amount to deposit: "))
                acc[user].deposit(amount)
        elif choice == "3":
            account_user = input("Enter your account number: ")
            password1 = input("Enter password")
            if account_user and password1 in acc:
                amount1 = int(input("Enter amount to withdraw: "))
                acc[account_user].withdraw(amount1)
            else:
                print("Accoung invalid")
        elif choice == "4":
            account_user1 = input("Enter account number: ")
            password2 = input("Enter password: ")
            if account_user1 and password2 in acc:
                acc[account_user1].check_balance()
            else:
                print("Invalid account number")
        elif choice == "5":
            account_user2 = input("Enter account number: ")
            if account_user2 in acc:
                password3 = input('Enter new password: ')
                password4 = input("Enter current password: ")
                if password4 == acc[account_user2].password:
                    acc[account_user2].change_password(password3)
                else:
                    print("Password is incorrent")
            else:
                print("Invalid account number: ")
        elif choice =="6":
            print("Thank you for using our bank!")
            break
        else:
            print("Invalid choice")

if __name__ =="__main__":
    main()

        