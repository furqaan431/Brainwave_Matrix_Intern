class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        print(f"Your current balance is: ₹{self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully!")
            self.check_balance()
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"₹{amount} withdrawn successfully!")
                self.check_balance()
            else:
                print("Insufficient balance for withdrawal.")
        else:
            print("Withdrawal amount must be greater than zero.")

    def exit(self):
        print("Thank you for using our ATM. Goodbye!")
        return False

def atm_interface():
    atm = ATM(balance=10000)  # Initial balance
    while True:
        print("\n==== Welcome to the ATM ====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        
        choice = input("Please select an option (1/2/3/4): ")

        if choice == '1':
            atm.check_balance()
        elif choice == '2':
            amount = float(input("Enter amount to deposit: ₹"))
            atm.deposit(amount)
        elif choice == '3':
            amount = float(input("Enter amount to withdraw: ₹"))
            atm.withdraw(amount)
        elif choice == '4':
            if not atm.exit():
                break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    atm_interface()
