# a class for SIM card accounts
class SIMCard:
    def __init__(self, phone_number, balance=0): #  Balance start with 0
        self.phone_number = phone_number
        self.balance = balance

# 1 function method
    def top_up(self, amount):
        self.balance += amount
        print(f"Balance topped up by {amount}. New balance: {self.balance}")

# 2 function method
    def make_call(self, duration):
        if self.balance >= duration:
            self.balance -= duration
            print(f"Call made for {duration} minutes. Remaining balance: {self.balance}")
        else:
            print("Insufficient balance")
            
# 3  function method
    def check_balance(self):
        print(f"Current balance: {self.balance}")

# main function to handle user input
def sim_card_system():
    print("Welcome to the SIM card system!")
    phone_number = input("Enter your phone number: ")
    sim_card = SIMCard(phone_number)
    
# condition start
    while True:
        print("\nSelect an option:")
        print("1. Top-up balance")
        print("2. Make a call")
        print("3. Check balance")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            amount = float(input("Enter top-up amount: "))
            sim_card.top_up(amount)
        elif choice == '2':
            duration = float(input("Enter call duration (in minutes): "))
            sim_card.make_call(duration)
        elif choice == '3':
            sim_card.check_balance()
        elif choice == '4':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid input")

sim_card_system()