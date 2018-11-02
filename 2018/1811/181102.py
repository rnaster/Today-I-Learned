# BOJ - 6416
from sys import stdin, stdout
read = lambda: stdin.readline().rstrip()
write = lambda x: stdout.write(x)
k = 1
while True:
    d = {}; run = True; isTree = True; skip = False
    while run:
        tp = read().split('  ')
        if tp[0] == '': skip = True; break
        for t in tp:
            a, b = map(int, t.split())
            if a == -1 and b == -1: exit()
            elif a == 0 and b == 0: run = False
            else:
                key = d.keys()
                if a not in key: d[a] = 0
                if b not in key: d[b] = 1
                else: d[b] += 1
    for v in set(d.values()):
        if v > 1: isTree = False; break
    if isTree: isTree = False if list(d.values()).count(0) != 1 else True
    if d == {}: isTree = True
    if not skip:
        ans = 'Case %s is a tree.\n' if isTree else 'Case %s is not a tree.\n'
        ans = ans % k
        write(ans)
        k += 1
"""
6 8  5 3  5 2  6 4
5 6  0 0

8 1  7 3  6 2  8 9  7 5
7 4  7 8  7 6  0 0

3 8  6 8  6 4
5 3  5 6  5 2  0 0
-1 -1
"""