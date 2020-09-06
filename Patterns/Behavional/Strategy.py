class Product:
    def __init__(self, price, strategy):
        self.price = price
        self.strategy = strategy

    def get_price(self):
        return self.strategy.calculate(self.price)

    def set_strategy(self, strategy):
        self.strategy = strategy


class Strategy:
    def calculate(self, price):
        pass


class Holiday(Strategy):
    def calculate(self, price):
        return price - price * 0.2


class BlackFriday(Strategy):
    def calculate(self, price):
        return price / 2


s = Holiday()
p = Product(100, s)
print(p.get_price())
s = BlackFriday()
p.set_strategy(s)
print(p.get_price())