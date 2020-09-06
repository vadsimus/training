from collections.abc import Iterator, Iterable
import random
import copy

class SimpleIterator(Iterator):
    # _position: int = None

    def __init__(self, collection):
        self.collection = collection
        self._position = 0

    def __next__(self):
        try:
            value = self.collection[self._position]
            self._position += 1
        except IndexError:
            raise StopIteration()
        return value


class OddIterator:
    # _position: int = None

    def __init__(self, collection):
        self.collection = collection
        self._position = 0

    def __next__(self):
        try:
            value = self.collection[self._position]
            self._position += 2
        except IndexError:
            raise StopIteration()
        return value

    def __iter__(self):
        return self


class RevIterator:
    # _position: int = None

    def __init__(self, collection):
        self.collection = collection
        self._position = -1

    def __next__(self):
        try:
            value = self.collection[self._position]
            self._position -= 1
        except IndexError:
            raise StopIteration()
        return value

    def __iter__(self):
        return self


class RandomIterator:
    _position: int = None

    def __init__(self, collection):
        new_collection = copy.copy(collection)
        random.shuffle(new_collection)

        self.collection = new_collection
        self._position = 0

    def __next__(self):
        try:
            value = self.collection[self._position]
            self._position += 1
        except IndexError:
            raise StopIteration()
        return value

    def __iter__(self):
        return self


class Collection:
    def __init__(self, collection, itr):
        self._collection = collection
        self._itr = itr

    def __iter__(self):
        return self._itr(self._collection)


c = ['one', 'two', 'three', 'four', 'five']
c1 = Collection(c, SimpleIterator)
c2 = Collection(c, OddIterator)
c3 = Collection(c, RevIterator)
c4 = Collection(c, RandomIterator)

print(','.join(c))
print(','.join(c2))
print(','.join(c3))
print(','.join(c4))
print(','.join(c1))
