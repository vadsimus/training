from abc import ABC


class AbstractFactory(ABC):
    def create_product_a(self):
        pass

    def create_product_b(self):
        pass


class Factory1(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA1()

    def create_product_b(self):
        return ConcreteProductB1()


class Factory2(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA2()

    def create_product_b(self):
        return ConcreteProductB2()


class AbstractProductA:
    def useful_function_a(self):
        pass


class ConcreteProductA1(AbstractProductA):
    def useful_function_a(self):
        return 'The result of useful function A1'


class ConcreteProductA2(AbstractProductA):
    def useful_function_a(self):
        return 'The result of useful function A2'


class AbstractProductB:
    def useful_function_b(self):
        pass


class ConcreteProductB1(AbstractProductB):
    def useful_function_b(self):
        return 'The result of useful function B1'


class ConcreteProductB2(AbstractProductB):
    def useful_function_b(self):
        return 'The result of useful function B2'


def client_code(factory: AbstractFactory):
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    print(f'{product_a.useful_function_a()}')
    print(f'{product_b.useful_function_b()}')


if __name__ == '__main__':
    client_code(Factory1())
    print('\n')
    client_code(Factory2())
