class Base:
    def main_logic(self):
        self.part1()
        print('общее дело 1')
        self.part2()
        self.part3()

    def part1(self):
        print('база1')

    def part2(self):
        pass

    def part3(self):
        pass

class Logic1(Base):
    def part2(self):
        print('дело2')

    def part3(self):
        print('дело3')


class Logic2(Base):
    def part2(self):
        print('новое дело2')

    def part3(self):
        print('новое дело3')

Logic1().main_logic()
print()
Logic2().main_logic()
