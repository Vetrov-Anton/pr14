def g(x):
    d = {}
    L = ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG']
    out = '(task_4)' + x
    with open(x, mode='r') as f:
        for line in f:
            if line[0] == '>':
                y = line.strip()[1:]
                head = y.split()[0]
                d[head] = ''
            else:
                d[head] = d[head] + line.strip()
    with open(out, mode='w') as file:
        for k in L:
            v = 0
            for i in d.keys():
                c = 0
                for j in range(2, len(d[i]), 3):
                    if d[i][j-2:j+1] == k:
                        c = c + 1
                v = v + c
            print(f'{k}\t{v}', file=file)




g('1.txt')
g('2.txt')
g('3.txt')
