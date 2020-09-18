import random


def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g

    return inner


@coroutine
def average():
    count = 0
    summ = 0
    averg = None

    while True:
        try:
            x = yield averg
        except StopIteration:
            pass
        else:
            count += 1
            summ += x
            averg = round(summ / count, 2)


if __name__ == '__main__':
    outer = average()
    for _ in range(100):
        g = average()
        for i in range(100):
            x = random.randrange(100)
            g.send(x)
        outer.send(g.throw(StopIteration))
    print(outer.throw(StopIteration))
