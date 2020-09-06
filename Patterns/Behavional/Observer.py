class Shop:
    _subscribers = []

    def __init__(self, state):
        self.state = state

    def attach(self, observer):
        self._subscribers.append(observer)

    def deattach(self, observer):
        self._subscribers.remove(observer)

    def notify(self):
        for o in self._subscribers:
            o.update(self)

    def set_state(self, new_state):
        self.state = new_state

    def logic(self):
        print('some logic')
        if self.state == 20:
            self.notify()


class Observer:
    def update(self, shop):
        pass

class GoodClient(Observer):
    def update(self, shop):
        print(f'УЖе бегу на скидку {shop.state}')

class BadClient(Observer):
    def update(self, shop):
        print('надоел спам')
        shop.deattach(self)

c1 = GoodClient()
c2 = BadClient()

shop = Shop(10)
shop.attach(c1)
shop.attach(c2)
shop.logic()

shop.set_state(20)
shop.logic()
shop.logic()