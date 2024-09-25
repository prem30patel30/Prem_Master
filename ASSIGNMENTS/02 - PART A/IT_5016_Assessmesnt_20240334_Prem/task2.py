"""PROGRAM TO CALCULATE THE TOTAL COST OF SERVICE 
  AUTHOR:PREM 
"""

def ferry_service_total():
    items_list = []
    total_price = 0
    
    while True:
        item_name = input("Enter item name (or 'finish' to end): ")
        if item_name.lower() == 'finish':
            break
        try:
            item_price = float(input("Enter item price: $"))
            items_list.append((item_name, item_price))
            total_price += item_price
        except ValueError:
            print("Invalid Input. Please enter the numberic value")
            
    return items_list, total_price

def main():
    items_list, total_price = ferry_service_total()
    print("\nItems List:")
    if not items_list:
        print("No items added.")
    for item_name, item_price in items_list:
        print(f"{item_name}: ${item_price}")
    print(f"Total Price : ${total_price:.2f}")
    
main()