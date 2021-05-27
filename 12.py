import pathlib

inputpath = pathlib.Path('in/hightemp.txt')
outputpath1 = pathlib.Path('out/col1.txt')
outputpath2 = pathlib.Path('out/col2.txt')

with inputpath.open() as f:
    lines = f.readlines()

output1 = []
output2 = []
for l in lines:
    sp = l.split('\t')
    output1.append(sp[0])
    output2.append(sp[1])

with outputpath1.open(mode='w') as f:
    f.write('\n'.join(output1))

with outputpath2.open(mode='w') as f:
    f.write('\n'.join(output2))