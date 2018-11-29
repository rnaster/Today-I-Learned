# BOJ - 5721
from sys import stdin, stdout, setrecursionlimit
from copy import deepcopy
read = lambda: stdin.readline().rstrip()
write = lambda x: stdout.write(str(x) + '\n')
setrecursionlimit(1000000)
MAP = None, None
m, n = None, None
def func(a, b, visit_):
    num = MAP[a][b]
    if a - 1 >= 0:
        for j in range(n):
            visit_[a-1][j] = 1
    for j in (-1, 0, 1):
        if 0 <= b + j < n:
            visit_[a][b+j] = 1
    if a + 1 < m:
        for j in range(n):
            visit_[a+1][j] = 1
    dp = 0
    for i in range(m):
        for j in range(n):
            if visit_[i][j] == 0:
                dp = max(dp, func(i, j, deepcopy(visit_)))
    return dp + num
# print(func(0, 0, [[0] * n for _ in range(m)]));exit()
while True:
    m, n = map(int, read().split())
    if m * n == 0: exit()
    MAP = []
    visit = [[0] * n for _ in range(m)]
    for _ in range(m):
        MAP.append(tuple(map(int, read().split())))
    ans = 0
    for i in range(m):
        for j in range(n):
            ans = max(ans, func(i, j, deepcopy(visit)));print(ans)
    write(ans);exit()
    # print(visit, '\n\n')
"""
5 5
1 8 2 1 9
1 7 3 5 2
1 2 10 3 10
8 4 7 9 1
7 1 3 1 6
4 4
10 1 1 10
1 1 1 1
1 1 1 1
10 1 1 10
2 4
9 10 2 7
5 1 1 5
0 0
"""