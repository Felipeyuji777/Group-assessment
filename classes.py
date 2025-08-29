#make list for classes
menu = []
activeOrders = []
completedOrders = []
totalIncome = 0

class menuItem:
    def __init__(self, itemId, name, price):
        self.itemId = itemId
        self.name = name
        self.price = price
        
        #append menuItem to menu[] on construction
        menu.append(self)

class order:
    def __init__(self, orderId):
        self.orderId = orderId
        self.items = []

        #append to activeOrders on construction
        activeOrders.append(self)

    def addItem(self, item):
        self.items.append(item)

    def cancel(self):
        activeOrders.remove(self)

    def orderCost(self):
        orderPrice = 0
        for item in self.items:
            orderPrice += item.price

        return orderPrice


    def complete(self):
        completedOrders.append(self)
        activeOrders.remove(self)
