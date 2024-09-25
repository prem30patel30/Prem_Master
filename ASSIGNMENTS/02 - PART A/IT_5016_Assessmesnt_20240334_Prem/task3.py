"""
PYTHON PROGRAM FOR MAKING APPROVAL DECISION
Author:- PREM
"""

def booking_approval(id_counter):
    form_of_id = input("Enter the form of id : ")
    ID_number = input("Enter the ID number : ")
    Passenger_name = input("Enter the Passenger name : ")
    unique_id = id_counter + 20000
    print("Passenger's basic information")
    print("User name :", Passenger_name)
    print("User id :", unique_id)
    print("form_of_id :", form_of_id)
    return {"form_of_id": form_of_id, "Id_number": ID_number, "Passenger_name": Passenger_name, "unique_id": unique_id}

def booking_total(passenger_info):
    total_amount = 0
    while True:
        item = input("Hello passenger enter the name of the item (or type 'finish' to finish) :")
        if item.lower() == 'finish' :
            break
        try:
            price = float(input(f"Enter the price of '{item}': $"))
            total_amount += price
        except ValueError:
            print("Invalid price. Please enter a numeric value for the price.")
    return total_amount , passenger_info
def booking_approval(total_amount, passenger_info):
    if total_amount > 0:
        status = "approved"
    else:
        status = "pending"
    print(f"Category: {status}") 
