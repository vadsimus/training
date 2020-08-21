class Component:
    def operation(self):
        print('Component operation')


class C1(Component):
    def __init__(self, mark):
        self.mark = mark


class Decorator:
    def __init__(self, comp):
        self.component = comp

    def operation(self):
        return self.component.operation()


class DecoratorA(Decorator):
    def operation(self):
        print('Some useful action before')
        super().operation()


class DecoratorB(Decorator):
    def operation(self):
        super().operation()
        print('Some useful actions after')


component = C1(1)
component.operation()
print(component.mark)
print('----------------')
component = C1(2)
DecoratorA(DecoratorB(DecoratorA(component))).operation()
print(component.mark)
