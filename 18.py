import pathlib
import sys
import numpy as np

iptpath = pathlib.Path('in/hightemp.txt')

def main():
    with iptpath.open() as f:
        lines = f.readlines()

    lines.sort(key=lambda l: float(l.split('\t')[2]), reverse=True)

    for l in lines:
        print(l.rstrip())

if __name__ == '__main__':
    main()