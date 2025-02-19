class Stock:
    def __init__(self, name):
        self.name = name
        self.price = 0
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def set_price(self, new_price):
        self.price = new_price
        self.notify_observers()

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.name, self.price)

class Investor:
    def __init__(self, name):
        self.name = name

    def update(self, stock_name, price):
        print(f"{self.name} received alert: {stock_name} new price is {price}")

# Testing
apple = Stock("Apple")
investor1 = Investor("Alice")
investor2 = Investor("Bob")

apple.add_observer(investor1)
apple.add_observer(investor2)

apple.set_price(150)  
# Output:
# Alice received alert: Apple new price is 150
# Bob received alert: Apple new price is 150

apple.remove_observer(investor1)

apple.set_price(200)  
# Output:
# Bob received alert: Apple new price is 200