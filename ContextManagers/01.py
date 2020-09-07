from contextlib import contextmanager


@contextmanager
def processor():
    print('--> start processing')
    try:
        yield
    finally:
        print('<-- stop processing')



with processor():
    print(':: processing')
    raise Exception
