from itertools import *
x = input() #таблица с координатами
y = input() #полная последовательность генома
with open(x, mode='r') as f:
    I = []
    for line in f:
        if ('..' in line) and ('CDS' in line) and (not('complement' in line)) and (not('join' in line)):
            I.append(line[10:].strip())
    J = []
    for i in I:
        j = int(i.split('..')[0])
        J.append(j)
with open(y, mode='r') as g:
    s = ''
    g.readline()
    for line in g:
        s = s + line.strip()
with open('out_6', mode='w') as h:
    for k in product('ATGC', repeat=6):
        k = ''.join(list(k))
        n = 0
        for j in J:
            v = s[j-21:j]
            q = v.count(k)
            n = n + q
        print(f'{k}\t{n}', file=h)








