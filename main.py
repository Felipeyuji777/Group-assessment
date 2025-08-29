import classes

#define MenuItems:
Coffee = classes.menuItem(1, "Coffee", 15000)
Toast = classes.menuItem(2, "Toast", 5)
Sandwich = classes.menuItem(3, "Sandwich", 7)
Salad = classes.menuItem(4, "Salad", 6)
Juice = classes.menuItem(5, "Juice", 3)
Soup = classes.menuItem(6, "Soup", 4)
Cake = classes.menuItem(7, "Cake", 5)


#define functions

while True:
    print("Please choose an option:")
    print("(1). View Menu")
    print("(2). Place an order")
    print("(3). View active orders")
    print("(3). View order history")
    print("(4). exit program")

    userInput = int(input("please choose an option (1-4)"))


    #view menu
    if(userInput == 1):
        for item in classes.menu:
            print(item.name, item.price)
    
    #make a new order
    elif(userInput == 2):
        userOrder = classes.order(len(classes.activeOrders) + 1)
        while True:
            
            print("type the id of the item that youd like to order:")
            userInputOrderId = int(input())
            
            #temp value, gets changed to true if menuitem is found
            found = False

            #iterate through classes.menu to find itemMenu id
            for item in classes.menu:
                if userInputOrderId == item.itemId:
                    #add item to list in order
                    userOrder.addItem(item)
                    print(f"ordered {item.name}")
                    found = True
                    break
                
            if not found:
                print("please input valid item id")
                continue


            more = input("Would you like to order another item? (y/n): ").strip().lower()
            if more != "y":
                break
             



    #show active orders   
    elif(userInput == 3):
        for order in classes.activeOrders:
            print(f"--- orderId: {order.orderId} - {order.orderCost()} ---")
            for item in order.items:

                print(item.name, item.price)

    elif(userInput == 4):
        print("type the id of the order youd like to cancel:")
        userInputId = int(input())
        
        for order in classes.activeOrders:
            if userInputId == order.orderId:
                order.cancel()    
                break


    else:
        print("please try again!")

