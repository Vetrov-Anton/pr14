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
        s = ''
        for i in d.keys():
            s = s + d[i]
        v = 0
        for k in L:
            c = 0
            for j in range(2, len(s), 3):
                if s[j-2:j+1] == k:
                    c = c + 1
            v = v + c
            print(f'{k}\t{c}', file=file)
        print(f'Leu codons\t{v}', file=file)
        print(f'All codons\t{len(s)//3}', file=file)
        print(f'Leu/All\t{v/(len(s)//3)}', file=file)




g('1.txt')
g('2.txt')
g('3.txt')