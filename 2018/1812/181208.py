# BOJ - 14503
from sys import stdin
read = lambda: stdin.readline().rstrip()
n, m = map(int, read().split())
cache = []
x, y, d = map(int, read().split())
for _ in range(n):
    cache.append(list(read().split()))
ans = 1
cache[x][y] = '2'
while True:
    go = False
    i = None
    for i in range(d+4, d, -1):
        i %= 4
        if i == 0:
            if cache[x][y-1] == '0': go = True; y += -1;break
        elif i == 1:
            if cache[x-1][y] == '0': go = True; x += -1;break
        elif i == 2:
            if cache[x][y+1] == '0': go = True; y += 1;break
        else:
            if cache[x+1][y] == '0': go = True; x += 1;break
    d = i
    if go:
        cache[x][y] = '2'
        ans += 1
    else:
        back = False
        if d == 0:
            if cache[x+1][y] != '1': back = True;x += 1
        elif d == 1:
            if cache[x][y-1] != '1': back = True;y += -1
        elif d == 2:
            if cache[x-1][y] != '1': back = True;x += -1
        else:
            if cache[x][y+1] != '1': back = True;y += 1
        if not back:
            print(ans)
            # print(*cache, sep='\n')
            # print(x, y)
            exit()
    print(x, y)
"""
3 3
1 1 0
1 1 1
1 0 1
1 1 1

11 10
7 4 0
1 1 1 1 1 1 1 1 1 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 1 1 1 1 0 1
1 0 0 1 1 0 0 0 0 1
1 0 1 1 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1
"""