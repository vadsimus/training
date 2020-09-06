class MyMath:
    def __init__(self, init=0):
        self.value = init

    def exp(self, v):
        self.value = self.value ** v
        return self.value


    def add(self, v):
        self.value = self.value + v
        return self.value


class Command:
    def __init__(self, target, v):
        self.target = target
        self.v = v

    def execute(self):
        return self.target(self.v)

m = MyMath(2)
commands = [
    Command(m.exp, 3),
    Command(m.exp, 2),
    Command(m.add, 1),
    Command(m.exp, 2)
]
for command in commands:
    print(m.value)
    command.execute()
print(m.value)
