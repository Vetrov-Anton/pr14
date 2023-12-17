x = input()
s = ''
w = int(input())
step = int(input())
with open(x, mode='r') as f:
    f.readline()
    for line in f:
        if line[0] == '>':
            break
        line = line.strip()
        s = s + line
out = 'out_GC-Scew' + x
with open(out, mode='w') as f:
    cum_scew = 0
    for i in range(0, len(s), step):
        y = s[i:i+w]
        if len(y) < w:
            break
        g = y.count('G')
        c = y.count('C')
        if g == 0 and c == 0:
            scew = 0
        else:
            scew = (g - c) / (g + c)
        cum_scew = cum_scew + scew
        print(f'{i}\t{scew:.3f}\t{cum_scew:.3f}', file=f)
