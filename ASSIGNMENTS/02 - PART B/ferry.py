"""
PROGRAM TO DEVELOP A REQUISITION SYSTEM PROTOTYPE
AUTHOR: PREM
TASK 1
"""

class BookingSystem:
    def __init__(self):
        self.booking_id_counter = 1
        self.booking = []

    def customer_info(self, ID_Number, Name, Status):
        return {"ID_Number": ID_Number, "Name": Name, "Status": Status}
 
    def ferry_service_details(self, items):
        total = sum(item["cost"] for item in items)
        return {"total": total, "items": items}
    
    def booking_approval(self, total):
        if total >= 0:
            return {"status": "approved"}
        else:
            return {"status": "pending"}

    def display_booking_info(self):
        for booking in self.booking:
            print(f"Name: {booking['user_info']['Name']}")
            print(f"Unique ID: {booking['id']}")
            print(f"Total: ${booking['total']:.2f}")
            print(f"Status: {booking['status']}")
            if booking["status"] == "approved":
                print("Approval")
            print("")

    def booking_statistic(self):
        total_bookings = len(self.booking)
        approved_bookings = sum(1 for booking in self.booking if booking["status"] == "approved")
        pending_bookings = sum(1 for booking in self.booking if booking["status"] == "pending")
        not_approved_bookings = sum(1 for booking in self.booking if booking["status"] == "not approved")

        print(f"Total number of bookings submitted: {total_bookings}")
        print(f"Total number of approved bookings: {approved_bookings}")
        print(f"Total number of pending bookings: {pending_bookings}")
        print(f"Total number of not approved bookings: {not_approved_bookings}")

    def update_booking_status(self, ID_Number, status):
        for booking in self.booking:
            if booking["user_info"]["ID_Number"] == ID_Number:
                booking["status"] = status
                return True
        return False

def main():
    booking_system = BookingSystem()

    while True:
        print("1. Submit Booking")
        print("2. Respond to Booking")
        print("3. Display Booking")
        print("4. Booking Statistics")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            ID_Number = input("Enter your ID Number: ")
            Name = input("Enter your Name: ")
            Status = input("Enter your Status: ")
            items = []
            while True:
                item_name = input("Enter item name (or 'done' to finish): ")
                if item_name.lower() == "done":
                    break
                item_cost = float(input("Enter item cost: "))
                items.append({"name": item_name, "cost": item_cost})

            customer_info = booking_system.customer_info(ID_Number, Name, Status)
            request_details = booking_system.ferry_service_details(items)
            total = request_details["total"]
            approval_response = booking_system.booking_approval(total)
            booking_system.booking.append({
                "id": booking_system.booking_id_counter,
                "user_info": customer_info,
                "total": total,
                "items": items,
                "status": approval_response["status"]
            })
            booking_system.booking_id_counter += 1
            print("Booking submitted successfully!")

        elif choice == "2":
            ID_Number = input("Enter ID Number: ")
            status = input("Enter response (approved/not approved): ")
            if booking_system.update_booking_status(ID_Number, status):
                print("Booking status updated successfully!")
            else:
                print("Booking ID not found.")

        elif choice == "3":
            booking_system.display_booking_info()

        elif choice == "4":
            booking_system.booking_statistic()

        elif choice == "5":
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
