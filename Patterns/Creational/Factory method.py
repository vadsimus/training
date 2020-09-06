class Dialog:
    def some_logic(self):
        pass

    def get_button(self):
        pass

class WindowsDialog(Dialog):
    def get_button(self):
        return WinowsButton()

class MacDialog(Dialog):
    def get_button(self):
        return MacButton()

class Button:
    pass

class WinowsButton(Button):
    def __str__(self):
        return 'windows button'

class MacButton(Button):
    def __str__(self):
        return 'mac button'

if input('win/mac') == 'win':
    dialog = WindowsDialog()
else:
    dialog = MacButton()

dialog.some_logic()
button = dialog.get_button()
print(button)

