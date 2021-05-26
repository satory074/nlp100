import pathlib

iptpath = pathlib.Path('in/hightemp.txt')

with iptpath.open() as f:
    lines = f.readlines()

for l in lines:
    print(l.replace('\t', ' '), end='')