# Prem_Master

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
SOLID Principles:

AS PER SIMCARD CODE, I HAVE APPLIED THE SOLID PRINCIPLES BY THIS CODE. WHICH IS AS FOLLOWS:

S — Single-Responsibility Principle (SRP) :

Three methods are available in the SIMCard class: top_up, make_call, and check_balance. Each method has its own responsibility, which is to perform a certain SIM card account related action. The sim_card_system function is responsible for taking user input, creating a SIMCard object and controlling the program flow.

O - Open-Closed Principle (OCP) :

new methods can be added to the SIMCard class without changing the existing code, it is open for extension. However it has limited options and would need to be modified to add new features, the sim_card_system function is not extensible.

L - Liskov Substitution Principle (LSP):

The SIMCard class is a base class, the SIMCard object is a derived class. The SIMCard class has a method called top_up which is not available in the SIMCard object.we create a new version of a class, it should work the same way as the original class. We didn't create any new versions of classes in this code, so this principle doesn't apply.

I - Interface Segregation Principle (ISP) :

we shouldn't force our code to use features it doesn't need. We didn't define any interfaces in this code, so this principle doesn't apply.

D - Dependency Inversion Principle (DIP) :

The sim_card_system function depends on the SIMCard class which is a low level module. To apply the DIP we could define an abstraction (interface or abstract class) that the sim_card_system function depends on and have the SIMCard class implement that abstraction. This would decouple the high level module from the low level module.
