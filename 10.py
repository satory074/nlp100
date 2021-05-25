import pathlib

iptpath = pathlib.Path('in/hightemp.txt')

with iptpath.open() as f:
    lines = f.readlines()

print(len(lines))