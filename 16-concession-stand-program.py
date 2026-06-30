# concession stand program
# Khai báo Menu bằng Dictionary trong Python
menu = {
    "popcorn": 4.50,
    "pizza": 5.00,
    "hotdog": 3.50,
    "fries": 2.50,
    "chips": 1.50,
    "soda": 2.00,
    "water": 1.00,
    "candy": 1.75,
}
cart = []
total = 0
print("--------------- MENU ---------------")
for item, price in menu.items():
    # Tên món (căn trái, rộng 20 ký tự, lấp đầy bằng dấu .) + Giá tiền
    print(f"{item.capitalize():.<20}${price:.2f}")
while True:
    food = input("Select an item (q to quit): ")
    if food.lower() == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
        total += menu[food]
        print(f"{food.capitalize()} added to cart. Total: ${total:.2f}")
    else:
        print("Item not found in menu. Please try again.")
print(f"Your total price is ${total}")
