d = {}
def g(x):
    out = '(task_3)' + x
    with open(x, mode='r') as f:
        for line in f:
            if line[0] == '>':
                y = line.strip()[1:]
                head = y.split()[0]
                d[head] = ''
            else:
                d[head] = d[head] + line.strip()
    with open(out, mode='w') as file:
        s = []
        for i in d.keys():
            z = d[i][-3] + d[i][-2] + d[i][-1]
            s.append(z)
        n = sorted(list(set(s)))
        for i in n:
            print(f'{i}\t{s.count(i)}', file=file)
g('1.txt')
g('2.txt')
g('3.txt')