"""
Description :- CREATE A PYTHON PROGRAM FOR PASSENGER'S BASIC INFORMATION 
Author:- PREM
"""

def display_booking(id_counter):
    form_of_id = input("Enter the form of id : ")
    ID_number = input("Enter the ID number : ")
    Passenger_name = input("Enter the Passenger name : ")
    unique_id = id_counter + 20000
    print("Passenger's basic information")
    print("User name :", Passenger_name)
    print("User id :", unique_id)
    print("form_of_id :", form_of_id)
    return {"form_of_id": form_of_id, "Id_number": ID_number, "Passenger_name": Passenger_name, "unique_id": unique_id}

def requisition_total(passenger_info):
    total_amount = 0
    while True:
        item = input("Hello passenger enter the name of the item (or type 'done' to finish) :")
        if item.lower() == 'done' :
            break
        try:
            price = float(input(f"Enter the price of '{item}': $"))
            total_amount += price
        except ValueError:
            print("Invalid price. Please enter a numeric value for the price.")
    return total_amount , passenger_info
def requisition_approval(total_amount, passenger_info):
    if total_amount > 0:
        status = "approved"
    else:
        status = "pending"
    print(f"Category: {status}") 
        
def create_detailed_report(passenger_data, status, categorization):
    
    print("Detailed Report:")
    print("----------------")
    print(f"User's Name: {passenger_data['name']}")
    print(f"status : ${status:.2f}")
    print(f"Category: {categorization['category']}")
    print("----------------")
    return passenger_data,status
def  main_answer():
    u_id = id_counter + 1
    id_counter = u_id

    id_counter = 20000
    passenger_info = passenger_info(id_counter)
    total_amount = requisition_total(passenger_info)
    categorization = requisition_approval(total_amount, passenger_info)
    print(categorization)
main_answer()