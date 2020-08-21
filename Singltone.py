class Singltone:
    _product = None

    @classmethod
    def get_item(cls):
        if not cls._product:
            cls._product = cls()
        return cls._product


if __name__ == '__main__':
    o1 = Singltone.get_item()
    print(o1)
    o2 = Singltone.get_item()
    print(o2)
    o3 = Singltone()
    print(o3)
