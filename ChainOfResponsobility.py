logins = {'admin': '123', 'Vasya': 'idufhal197wd', 'Oleg': 'qwe'}

class TargetObject:
    def access(self):
        print('Access granted')

class Handler:
    def handle(self, login, password):
        pass

class LoginCorrect(Handler):
    def handle(self, login: str, password):
        if any([login.startswith(char) for char in [' ', '/', '-']]):
            raise Exception
        for char in login:
            if char in [' ', '?', '`']:
                raise Exception
        LoginCheck().handle(login, password)

class LoginCheck(Handler):
    def handle(self, login, password):
        if login not in logins:
            raise Exception
        PasswordCheck().handle(login, password)

class PasswordCheck(Handler):
    def handle(self, login, password):
        if logins[login] == password:
            TargetObject().access()
            return
        raise Exception


LoginCorrect().handle('admin', '123')
try:
    LoginCorrect().handle('Oleg', '123')
except Exception:
    print('Access denied')

