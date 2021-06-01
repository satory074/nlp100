import pathlib
import sys
import numpy as np

iptpath = pathlib.Path('in/hightemp.txt')

def main(n:int):
    with iptpath.open() as f:
        lines = f.readlines()

    for l in np.array_split(lines, n):
        for l_ in l:
            print(l_.rstrip())
        else:
            print()

if __name__ == '__main__':
    n: int = int(sys.argv[1])
    main(n)