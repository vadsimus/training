import random


class Originator:
    # _state = None

    def __init__(self, initial):
        self._state = initial

    def do_something(self):
        print('Do something important')
        a = [x for x in self._state]
        random.shuffle(a)
        self._state = ''.join(a)

    def save(self):
        return Memento(self._state)

    def restore(self, memento):
        self._state = memento.get_state()

    def print_state(self):
        print(f'Actual state: {self._state}')


class Memento:
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state


class Caretaker:
    def __init__(self, originator):
        self._originator = originator
        self._storage = []

    def backup(self):
        self._storage.append(self._originator.save())

    def retore(self):
        self._originator.restore(self._storage.pop())


if __name__ == '__main__':
    orig = Originator('Initinal State')
    caretaker = Caretaker(orig)
    caretaker.backup()
    orig.print_state()
    orig.do_something()
    caretaker.backup()
    orig.print_state()
    orig.do_something()
    orig.print_state()

    caretaker.retore()
    orig.print_state()
    caretaker.retore()
    orig.print_state()
