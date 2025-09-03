# Define list with our menu items
menu = [
    {"name": "Americano", "price": 30000},
    {"name": "Latte", "price": 55000},
    {"name": "Cappuccino", "price": 55000},
    {"name": "Phin sua da", "price": 30000},
    {"name": "Phin den da", "price": 30000}
]


# List that keeps track of our orders
orders = []

# Total income for the shop
total_income = 0.0

# How much a customer needs to buy for to get discount
discount_threshold = 100000

# Discount as decimal
discount_rate = 0.1

# Print user options
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
    try:
        # Temp value that captures user input
        option = int(input("Select an option (1-8): "))
    except ValueError: # Handle non-integer input
        print("Invalid input. Please enter a number between 1 and 8.")
        continue

    if option not in range(1, 9):
        print("Invalid option. Please select a number between 1 and 8.")
        continue

    # View Menu
    if option == 1:
        print("\n--- Menu ---")
        
        # Iterate through menu[] and print each value
        for idx, item in enumerate(menu, 1):
            print(f"{idx}. {item['name']}: {item['price']} VND")
        print("------------\n")
    
    # Place order 
    elif option == 2:
        #capture user input
        item_name = input("Enter the name of the item to order: ")
        
        # Search for userinput in menu
        found = next((item for item in menu if item["name"].lower() == item_name.lower()), None)
        if found:
            orders.append(found)
            print(f"{found['name']} added to your order.")
        else:
            print("Item not found in menu.")
    
    # Cancel an order
    elif option == 3:
        #capture user input
        item_name = input("Enter the name of the item to cancel: ")
        
        # Search for userinput in menu
        found = next((item for item in orders if item["name"].lower() == item_name.lower()), None)
        if found:
            orders.remove(found)
            print(f"{found['name']} removed from your order.")
        else:
            print("Item not found in your current orders.")
    
    # View current orders
    elif option == 4:
        if not orders:
            print("No current orders.")
        
        # Iterate through orders[] and print name and price
        else:
            print("\n--- Current Orders ---")
            for idx, order in enumerate(orders, 1):
                print(f"{idx}. {order['name']}: {order['price']} VND")
            print("----------------------\n")
    
    # Calculate order total
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
    
    # Complete an order
    elif option == 6:
        if not orders:
            print("No items to complete order.")
        else:
            total = sum(item['price'] for item in orders)
            discount = 0

            # Apply discount
            if total >= discount_threshold:
                discount = total * discount_rate
                total -= discount
            total_income += total
            print(f"Order completed. Total amount: {total} VND")
            orders.clear()
    
    # Show total income
    elif option == 7:
        print(f"Total income so far: {total_income} VND")
    
    # Quit program
    elif option == 8:
        print("Exiting the system. Thanks for visiting BUV Beans and Leaves!")
        break

