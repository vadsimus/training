class Dialog:
    def __init__(self):
        self.button = Button(self)
        self.checkbox = Checkbox()
    def button_pressed(self):
        self.checkbox.enable()


class Button:
    def __init__(self, mediator):
        self.mediator = mediator

    def pressed(self):
        self.mediator.button_pressed()


class Checkbox:
    def enable(self):
        print('checkbox is enabled')

d = Dialog()
d.button.pressed()