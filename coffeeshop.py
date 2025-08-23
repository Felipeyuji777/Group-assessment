#test change
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
while True:
    print("1. View Menu")
    print("2. Place Order")
    print("3. Cancel Order")
    print("4. View Current Orders")
    print("5. Calculate Order Total")
    print("6. Complete Order")
    print("7. Show Total Income")

    option = int(input("Select an option (1/2/3/4/5/6/7): "))

    if option == 1:
        print("==== MENU ====")
        for item in menu:
            print(item)
    elif option == 2:
        items = input("Select your order: ")
        orders.append(items)
    elif option == 3:
        cancel = input("Cancel an order: ")
        orders.remove(cancel)
    elif option == 4:
        print(f"Your current orders:{orders}")

