from functools import reduce

class Order:
    def get_price(self):
        pass


class Product(Order):
    def __init__(self, price) -> None:
        self.price = price

    def get_price(self):
        return self.price

class Box(Order):
    def __init__(self, order_list):
        self.order_list = order_list

    def get_price(self):
        return sum([order.get_price() for order in self.order_list])


if __name__ == '__main__':
    print('Let start')
    pr1 = Product(1)
    pr2 = Product(2)
    pr3 = Product(3)
    pr4 = Product(4)
    box = Box([pr1, Box([pr2, Box([pr3, pr4])])])
    print(box.get_price())

    print(
        Box([
            Product(100),
            Box([
                Product(1000),
                Product(1000),
                Box([
                    Product(1)
                ])
            ])
        ]).get_price()
    )


