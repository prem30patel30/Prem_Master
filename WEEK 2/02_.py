
item1=100
item2=200
item3=300

item1=float(input("Enter the price for item1:-"))
item2=float(input("Enter the price for item2:-"))
item3=float(input("Enter the price for item3:-"))
subtotal = item1 + item2 + item3
salestax= subtotal* 0.20
calculatetotal= subtotal + salestax

print("calculatestotal",calculatetotal)
