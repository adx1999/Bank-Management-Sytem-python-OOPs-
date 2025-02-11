import datetime

class BankAccount:
    def __init__(self, account_number, name, balance=0.0):
        self.account_number = account_number
        self.name = name
        self.balance = balance
        self.transactions = []  # Stores transaction history
        self.add_transaction("Account created", balance)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.add_transaction("Deposit", amount)
            print(f"₹{amount} deposited successfully. New balance: ₹{self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.add_transaction("Withdrawal", -amount)
            print(f"₹{amount} withdrawn successfully. New balance: ₹{self.balance}")
        else:
            print("Insufficient funds or invalid amount.")

    def check_balance(self):
        print(f"Account Balance: ₹{self.balance}")

    def add_transaction(self, transaction_type, amount):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.transactions.append(f"{timestamp} - {transaction_type}: ₹{amount}")

    def show_transaction_history(self):
        print("\nTransaction History:")
        for transaction in self.transactions:
            print(transaction)

# Bank Management System Interface
def main():
    print("Welcome to the Bank Management System\n")
    
    account_number = input("Enter Account Number: ")
    name = input("Enter Account Holder Name: ")
    initial_balance = float(input("Enter Initial Balance: "))

    account = BankAccount(account_number, name, initial_balance)

    while True:
        print("\nOptions:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Transaction History")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)
        elif choice == "3":
            account.check_balance()
        elif choice == "4":
            account.show_transaction_history()
        elif choice == "5":
            print("Thank you for using our Bank Management System!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
