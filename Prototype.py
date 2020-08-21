import copy

class Product:
    def __init__(self, parameter, lst):
        self.parameter = parameter
        self.lst = lst


p=Product(1, [1, 2])
p2 = copy.copy(p)
print(f'{id(p)},  {id(p2)}')
p.lst = [9, 0]
p.lst.append(7)
print(p.parameter, p.lst)

print(p2.parameter, p2.lst)
