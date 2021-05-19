from threading import *

def a():
    print(f'A func')
    c = Thread(target=b)
    c.start()
    c.join()
    print(c.value())
def b():
    print(f'B func')
    return 2*2
a()