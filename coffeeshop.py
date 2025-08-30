menu = [
    {"name": "Americano", "price": 30000},
    {"name": "Latte", "price": 55000},
    {"name": "Cappuccino", "price": 55000},
    {"name": "Phin sữa đá", "price": 30000},
    {"name": "Phin đen đá", "price": 30000}
]

orders = []
total_income = 0.0

discount_threshold = 100000
discount_rate = 0.1

print("Welcome to BUV Beans and Leaves!")
print("Now we have a special discount: 10% off for orders over 100,000 VND.")
print("1. View Menu")
print("2. Place Order")
print("3. Cancel Order")
print("4. View Current Orders")
print("5. Calculate Order Total")
print("6. Complete Order")
print("7. Show Total Income")
print("8. Exit")

while True:
    option = int(input("Select an option (1-8): "))
    if option == 1:
        print("\n--- Menu ---")
        for idx, item in enumerate(menu, 1):
            print(f"{idx}. {item['name']}: {item['price']} VND")
        print("------------\n")
    elif option == 2:
        item_name = input("Enter the name of the item to order: ")
        found = next((item for item in menu if item["name"].lower() == item_name.lower()), None)
        if found:
            orders.append(found)
            print(f"{found['name']} added to your order.")
        else:
            print("Item not found in menu.")
    elif option == 3:
        item_name = input("Enter the name of the item to cancel: ")
        found = next((item for item in orders if item["name"].lower() == item_name.lower()), None)
        if found:
            orders.remove(found)
            print(f"{found['name']} removed from your order.")
        else:
            print("Item not found in your current orders.")
    elif option == 4:
        if not orders:
            print("No current orders.")
        else:
            print("\n--- Current Orders ---")
            for idx, order in enumerate(orders, 1):
                print(f"{idx}. {order['name']}: {order['price']} VND")
            print("----------------------\n")
    elif option == 5:
        if not orders:
            print("No items in your order.")
        else:
            total = sum(item['price'] for item in orders)
            discount = 0
            if total >= discount_threshold:
                discount = total * discount_rate
                total -= discount
                print(f"You received a discount of 10%!")
            print(f"Now the total order amount is: {total} VND")
    elif option == 6:
        if not orders:
            print("No items to complete order.")
        else:
            total = sum(item['price'] for item in orders)
            discount = 0
            if total >= discount_threshold:
                discount = total * discount_rate
                total -= discount
            total_income += total
            print(f"Order completed. Total amount: {total} VND")
            orders.clear()
    elif option == 7:
        print(f"Total income so far: {total_income} VND")
    elif option == 8:
        print("Exiting the system. Thanks for visiting BUV Beans and Leaves!")
        break