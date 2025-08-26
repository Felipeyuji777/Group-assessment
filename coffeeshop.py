orders = []
total_income = 0.0
menu = [
    {"name": "Americano", "price": 30000},
    {"name": "Latte", "price": 55000},
    {"name": "Cappuccino", "price": 55000},
    {"name": "Phin sữa đá", "price": 30000},
    {"name": "Phin đen đá", "price": 30000}
]

print("Welcome to BUV Beans and Leaves!")
print("1. View Menu")
print("2. Place Order")
print("3. Cancel Order")
print("4. View Current Orders")
print("5. Calculate Order Total")
print("6. Complete Order")
print("7. Show Total Income")
print("8. Exit")

while True:
    option = int(input("Select an option (1/2/3/4/5/6/7/8): "))

    if option == 1:
        print("==== MENU ====")
        for item in menu:
            print(f"{item['name']} - {item['price']} VND")

    elif option == 2:
        items = input("Select your order: ")
        found = None
        for item in menu:
            if item["name"].lower() == items.lower():  # case-insensitive
                found = item
                break
        if found:
            orders.append(found)  # store dict
            print(f"{found['name']} added!")
        else:
            print("Item not found in menu.")

    elif option == 3:
        cancel = input("Cancel an order: ")
        removed = False
        for order in orders:
            if order["name"].lower() == cancel.lower():
                orders.remove(order)
                print(f"{cancel} removed.")
                removed = True
                break
        if not removed:
            print(f"{cancel} not found in your orders.")

    elif option == 4:
        if not orders:
            print("No current orders.")
        else:
            print("Your current orders:")
            for order in orders:
                print(f"- {order['name']} ({order['price']} VND)")

    elif option == 5:
        if not orders:
            print("No orders yet.")
        else:
            total = sum(item["price"] for item in orders)
            print(f"Your total is: {total} VND")

    elif option == 6:
        if not orders:
            print("No order to complete.")
        else:
            total = sum(item["price"] for item in orders)
            total_income += total
            print(f"Order completed! You paid {total} VND")
            orders.clear()

    elif option == 7:
        print(f"Total income so far: {total_income} VND")
    elif option == 8:
        print("Thanks for using our service!")
        break
    else:
        print("Invalid option, please try again.")

