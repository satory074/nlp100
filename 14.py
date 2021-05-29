import pathlib
import sys

iptpath = pathlib.Path('in/hightemp.txt')

def main(nrow:int):
    with iptpath.open() as f:
        lines = f.readlines()

    for l in lines[:nrow]:
        print(l.rstrip())

if __name__ == '__main__':
    nrow: int = int(sys.argv[1])
    main(nrow)