class Bank:#blueprint of data
    def __init__(self): #init method or constructor
        self.balance = 500.00  # starting balance
        self.correct_pin = "1234"

    # Step 1: Check PIN
    def check_pin(self):3
        attempts = 3
        while attempts > 0:
            pin = input("Enter your 4-digit PIN: ")
            if pin == self.correct_pin:
                print("PIN accepted. Welcome to Humber Bank!")
                return True
            else:
                attempts -= 1
                print(f" Incorrect PIN. You have {attempts} attempt(s) left.\n")
        print(" Too many incorrect attempts. Exiting program.")
        return False

    # Step 2: Display Menu
    def display_menu(self):
        print("\nHumber Bank Main Menu ")
        print("1. Check Balance")
        print("2. Make a Withdrawal")
        print("3. Make a Deposit")
        print("4. Exit")

    # Step 3: Check Balance
    def check_balance(self):
        print(f"\n Your current balance is: ${self.balance:.2f}")

    # Step 4: Withdraw Money
    def withdraw(self):
        print(f"your account balance is:{self.balance}")
        try:
            amount = float(input("\nEnter amount to withdraw: $"))
            if amount <= 0:
                print(" Amount must be greater than zero.")
            elif amount > self.balance:
                print("Insufficient balance. Withdrawal declined.")
            else:
                self.balance -= amount
                print(f" Withdrawal successful. New balance: ${self.balance:.2f}")
        except ValueError:
            print(" Invalid input. Please enter a number.")

    # Step 5: Deposit Money
    def make_deposit(self):
        try:
            amount = float(input("\nEnter amount to deposit: $"))
            if amount <= 0:
                print(" Deposit amount must be positive.")
            else:
                self.balance += amount
                print(f" Deposit successful. New balance: ${self.balance:.2f}")
        except ValueError:
            print(" Invalid input. Please enter a number.")

    # Step 6: Main Terminal
    def main_terminal(self):
        print("💳 Welcome to Humber Bank Terminal 💳")
        if not self.check_pin():
            return

        while True:
            self.display_menu()
            choice = input("\nEnter your choice (1-4): ")

            if choice == "1":
                self.check_balance()
            elif choice == "2":
                self.withdraw()
            elif choice == "3":
                self.make_deposit()
            elif choice == "4":
                print("\n Thank you for using Humber Bank. Goodbye!")
                break
            else:
                print(" Invalid menu option. Please choose 1–4.")

            again = input("\nWould you like to perform another action? (y/n): ").lower()
            if again != "y":
                print("\n Thank you for using Humber Bank. Goodbye!")
                break


# Run the program
if __name__ == "__main__":
    bank = Bank()
    bank.main_terminal()
