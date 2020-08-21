class Figure:
    def __init__(self, color):
        self.color = color


class Sqare(Figure):
    def square_function(self):
        print('Squre do something')


class Triangle(Figure):
    def triangle_function(self):
        print('Triange do something')
        self.color.all_colors()


class Color:
    def all_colors(self):
        print('Color some')


class Red(Color):
    def some_red_function(self):
        print('Color Red')


class Blue(Color):
    def some_blue_function(self):
        print('Color Blue')


if __name__ == '__main__':
    blue_triangle = Triangle(Blue())
    blue_triangle.triangle_function()
    print()
    blue_triangle.color.some_blue_function()
    print()
    red_sqare = Sqare(Red())
    red_sqare.square_function()
    red_sqare.color.some_red_function()
