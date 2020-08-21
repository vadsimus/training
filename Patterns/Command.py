class MyMath:
    def __init__(self, init=0):
        self.value = init

    def cube(self):
        return self.value ** 3

    def square(self):
        return self.value ** 2


class Command:
    def __init__(self, target):
        self.target = target

    def execute(self):
        return self.target()


commands = [
    Command(MyMath(2).square),
    Command(MyMath(3).cube),
    Command(MyMath(4).square)
]
for command in commands:
    print(command.execute())
