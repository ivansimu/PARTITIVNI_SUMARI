import argparse
from razmjena import Burza
import basic

if __name__ == 'main':
    prod()

def prod():
    r = Burza(False)
    basic.run2(r)


def test():
    r = Burza(True)
    basic.run2(r)

print("Hello world")