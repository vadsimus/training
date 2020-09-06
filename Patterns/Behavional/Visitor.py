class Forest:
    def accept(self, visitor):
        pass

class Bereza(Forest):
    def accept(self, visitor):
        visitor.call_from_bereza(self)

    def spilit(self):
        print('bereza spilena')

    def sok(self):
        print('sok')

class Elka(Forest):
    def accept(self, visitor):
        visitor.call_from_elka(self)

    def naryadit(self):
        print('elka naryazhena')

    def shishki(self):
        print('mnogo shishok')

class Visitor:
    def call_from_bereza(self, bereza):
        pass

    def call_from_elka(self, elka):
        pass


class NewYear(Visitor):
    def call_from_bereza(self, bereza):
        bereza.spilit()

    def call_from_elka(self, elka):
        elka.naryadit()

class Summer(Visitor):
    def call_from_bereza(self, bereza):
        bereza.sok()

    def call_from_elka(self, elka):
        elka.shishki()

forest = [Bereza(), Elka(), Bereza(), Bereza(), Elka()]
visitor = NewYear()
for tree in forest:
    tree.accept(visitor)
print()
visitor = Summer()
for tree in forest:
    tree.accept(visitor)
