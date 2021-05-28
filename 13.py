import pathlib

inputpath1 = pathlib.Path('out/col1.txt')
inputpath2 = pathlib.Path('out/col2.txt')
outputpath = pathlib.Path('out/13.txt')

with inputpath1.open() as f:
    lines1 = f.readlines()

with inputpath2.open() as f:
    lines2 = f.readlines()

output = []
for l1, l2 in zip(lines1, lines2):
    output.append(f"{l1.rstrip()}\t{l2.lstrip()}")

with outputpath.open(mode='w') as f:
    f.write(''.join(output))