#takes user input
item_name = input("Enter item name: ")
item_price = input("Enter item price: ")
item_quantity = input("Enter quantity: ")

#converting variables to right data types
price = float(item_price)
quantity = int(item_quantity)

#calculation
total_bill = price * quantity

#prints bill
print(f"Total Bill for {item_name} = {total_bill:.2f}")
