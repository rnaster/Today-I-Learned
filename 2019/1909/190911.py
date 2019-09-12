# BOJ - 14499
n, m, x, y, _ = map(int, input().split())
arr = [[*map(int, input().split())] for _ in range(n)]
tp = map(int, input().split())
a, b, c, d, e = 1, 3, 2, 4, 5
dice = {i: 0 for i in range(1, 7)}
dd = {1: (0, 1), 2: (0, -1), 3: (-1, 0), 4: (1, 0)}
for t in tp:
    if -1 < x + dd[t][0] < n and -1 < y + dd[t][1] < m:
        if t == 1:
            a, d, b = b, a, 7 - a
        elif t == 2:
            a, d, b = d, 7 - a, a
        elif t == 3:
            a, c, e = c, 7 - a, a
        else:
            a, c, e = e, a, 7 - a
        x += dd[t][0]
        y += dd[t][1]
        if arr[x][y] > 0:
            dice[a] = arr[x][y]
            arr[x][y] = 0
        else:
            arr[x][y] = dice[a]
        print(dice[7-a])
"""
4 2 0 0 8
0 2
3 4
5 6
7 8
4 4 4 1 3 3 3 2


"""
exit()

# BOJ - 14502
from itertools import combinations
from copy import deepcopy as copy
n, m = map(int, input().split())
arr = [[*map(int, input().split())] for _ in range(n)]
d = {0: [], 1: [], 2: []}
for i in range(n):
    for j in range(m):
        d[arr[i][j]].append((i, j))
if len(d[0]) == 3: print(0); exit()
if len(d[2]) == 0: print(len(d[0])); exit()
ans = 0
def func(walls):
    global ans
    _arr = copy(arr)
    visit = [[0] * m for _ in range(n)]
    _ans = len(d[0]) - 3
    q = d[2][:]
    for a, b in walls:
        _arr[a][b] = 1
        visit[a][b] = 1
    for a, b in q:
        _arr[a][b] = 2
        visit[a][b] = 1
    for a, b in d[1]:
        visit[a][b] = 1
    while q:
        a, b = q.pop()
        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            if -1 < a + dx < n and -1 < b + dy < m and visit[a+dx][b+dy] < 1 and _arr[a+dx][b+dy] < 1:
                _arr[a+dx][b+dy] = 2
                visit[a+dx][b+dy] = 1
                q.append((a+dx, b+dy))
                _ans -= 1
    ans = max(ans, _ans)
for comb in combinations(d[0], 3):
    func(comb)
print(ans)
"""
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0

4 6
0 0 0 0 0 0
1 0 0 0 0 2
1 1 1 0 0 2
0 0 0 0 0 2
"""