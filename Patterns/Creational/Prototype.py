# import copy
#
# class Product:
#     def __init__(self, parameter, lst):
#         self.parameter = parameter
#         self.lst = lst
#
#
# p=Product(1, [1, 2])
# p2 = copy.copy(p)
# print(f'{id(p)},  {id(p2)}')
# p.lst = [9, 0]
# p.lst.append(7)
# print(p.parameter, p.lst)
#
# print(p2.parameter, p2.lst)

class Product:
    def __init__(self, parameter1, parameter2):
        self.par1 = parameter1
        self.par2 = parameter2

    def get_copy(self):
        return Product(self.par1, self.par2)

    def __str__(self):
        return f"p1={self.par1}, p2={self.par2}"

p1 = Product(100, '123')
p2 = p1.get_copy()

print(p1)
print(p2)


