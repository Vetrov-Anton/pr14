x = input()
d = {}
a = ['TGA', 'TAA', 'TAG']
with open(x, mode='r') as f:
    for line in f:
        if line[0] == '>':
            head = line.strip()[1:]
            d[head] = ''
        else:
            d[head] = d[head] + line.strip()
h = 'out(task2)' + x
with open(h, mode='w') as f:
    for i in d.keys():
        for j in range(2, len(d[i])-2, 3):
            if d[i][j-2:j+1] in a:
                print(i, file=f)
                break