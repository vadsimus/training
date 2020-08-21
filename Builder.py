class Builder:
    def get_product(self):
        pass

    def produce_a(self):
        pass

    def produce_b(self):
        pass

    def produce_c(self):
        pass


class Builder1(Builder):
    def __init__(self):
        self._product = Product1()

    def get_product(self):
        return self._product

    def produce_a(self):
        self._product.add('Part_A1')
        return self


    def produce_b(self):
        self._product.add('Part_B1')
        return self
    def produce_c(self):
        self._product.add('Part_C1')
        return self
class Product1:
    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def list_parts(self):
        print(f'Product parts: {",".join(self.parts)}', end='')

class Director:
    def __init__(self, builder):
        self.builder = builder

    def get_minimal(self):
        self.builder.produce_a()

    def get_maximal(self):
        self.builder.produce_a()
        self.builder.produce_b()
        self.builder.produce_c()

if __name__ == '__main__':
    b = Builder1()
    Director(b).get_minimal()
    p = b.get_product()
    p.list_parts()
    print()
    b = Builder1()
    Director(b).get_maximal()
    b.get_product().list_parts()
    print()
    Builder1().produce_c().produce_a().get_product().list_parts()

