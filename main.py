import argparse
from razmjena import Burza
import basic

if __name__ == 'main':
    p = argparse.ArgumentParser()
    p.add_argument("--test",action='store_true', default=False )
    args = p.parse_args()
    print(args)
    raz = Burza(True)

def test():
    r = Burza(test)
    basic.run2(r)

print("Hello world")