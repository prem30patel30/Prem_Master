"""
    PROGRAM WHICH IS TO GATHER INFORMATION FROM USER
    AUTHOR : PREM
"""

def customerBooking(id_counter):
    
    print(f"Enter the Printing Booking Information")   
    form_of_id = input("Enter the form of id : ")
    ID_number = input("Enter the ID number : ")
    Passenger_name = input("Enter the passenger name : ")
    
    u_id = id_counter + 1
    id_counter = u_id
    
    print(f"Printing Booking Information")
    print(f"form_of_id : {form_of_id}")
    print(f"ID_number : {ID_number}")
    print(f"Passenger_Name : {Passenger_name}")
    print(f"Unique ID : {u_id}")
    

def main():
    id_counter = 20000
    customerBooking(id_counter)
main()