import collections as cl
import pathlib
import sys
import numpy as np

iptpath = pathlib.Path('in/hightemp.txt')

def main():
    with iptpath.open() as f:
        lines = f.readlines()

    lines = [l.split()[0] for l in lines]

    cl_ = cl.Counter(lines)
    for k, v in cl_.most_common():
        print(k, v)

if __name__ == '__main__':
    main()