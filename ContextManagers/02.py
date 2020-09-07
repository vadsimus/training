from datetime import datetime


class TimeCalc:
    def __init__(self):
        self.now = None


    def __enter__(self):
        self.now = datetime.now()
        return self.now

    def __exit__(self, exc_type, exc_val, exc_tb):
        now = datetime.now()
        print(now)
        print(now - self.now)


with TimeCalc() as g:
    print(g)
    inp = input('press something...')
    if inp == 'password':
        raise Exception


