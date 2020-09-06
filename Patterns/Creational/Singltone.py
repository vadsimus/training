# class Singltone:
#     _product = None
#
#     @classmethod
#     def get_item(cls):
#         if not cls._product:
#             cls._product = cls()
#         return cls._product
#
#
# if __name__ == '__main__':
#     o1 = Singltone.get_item()
#     print(o1)
#     o2 = Singltone.get_item()
#     print(o2)
#     o3 = Singltone()
#     print(o3)


def singleton(class_):
    instances = {}
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance

@singleton
class MyClass:
    pass

m = MyClass()
m1 = MyClass()

print(id(m))
print(id(m1))
