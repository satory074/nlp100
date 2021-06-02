import pathlib
import sys
import numpy as np

iptpath = pathlib.Path('in/hightemp.txt')

def main():
    with iptpath.open() as f:
        lines = f.readlines()

    lines = [l.split()[0] for l in lines]
    print(set(lines))

if __name__ == '__main__':
    main()