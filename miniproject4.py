#Bank Management System Project
 
class Account():
    def __init__(self,name="",password="",balance=0):
        self.name=name
        self.password=password
        self.balance=balance

    def create_account(self):
        print("----Welcome to Python Bank---- ")
        self.name=input("Enter your name:")
        self.password=input("Enter your password:")
        print("Account created successfully!")

    def login(self):
        print("----Login----") 
        name_input=input("Enter your name:")
        password_input=input("Enter your password:")
        if name_input==self.name and password_input==self.password:
            print("Login successfull")
            return True
        else:
            print("Invalid credentials.please enter the right credentials")
            return False

    def exitApp(self):
        print("Bye!")
        print(" ")

    def deposit(self):
        amount=float(input("Enter the deposit amount:"))
        if amount>0:
            self.balance+=amount
            print(f"{amount} deposited.New Balance:{self.balance}")
        else:
            print("Amount must be positive")

    def withdraw(self):
        amount=float(input("Enter the withdrawal amount:"))
        if amount>0 and amount<=self.balance:
            self.balance-=amount
            print(f"{amount} withdrawn.New Balance:{self.balance}") 
        else:
            print("Insufficient funds or invalid amount.")

    def check_balance(self):
        print(f"Your current balance is {self.balance}")

    def logout(self):
        print("you logged off successfully")
        exit()

acc=Account()

while True:
    print("----Welcome to Python Bank----")
    print("1.Credit Account")
    print("2.Login")
    print("3.Exit")
    choice=int(input("Enter your choice (1-3):"))
    
    if choice==1:
        acc.create_account()
    elif choice==2:
        if acc.login():
            while True:
                print("1.Deposit")
                print("2.Withdraw")
                print("3.Check Balance")
                print("4.Logout")
                ch=int(input("Enter your choice (1-4):"))

                if ch==1:
                    acc.deposit()
                elif ch==2:
                    acc.withdraw()
                elif ch==3:
                    acc.check_balance()
                elif ch==4:
                    acc.logout()
                else:
                    print("Invalid option.Please enter between 1-4.")
    elif choice==3:
        acc.exitApp()
        break
    else:
        print("Invalid option please enter between(1-3)")