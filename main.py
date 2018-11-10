import argparse
from razmjena import Razmjena

if __name__ == 'main':
    p = argparse.ArgumentParser()
    p.add_argument("--test",action='store_true', default=False )
    args = p.parse_args()
    print(args)
    raz = Razmjena(test)


print("Hello world")