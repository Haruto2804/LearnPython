item = input("What item would you like to purchase?: ")
price = float(input(f"What is the price of {item}?: "))
quantity = int (input(f"How many {item}s would you like to purchase?: "))
total = price * quantity
print(f"Your item is {item} and the total cost is: ${total:.2f}")