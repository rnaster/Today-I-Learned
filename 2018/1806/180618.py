# BOJ - 5721
import sys
read = lambda: sys.stdin.readline().rstrip()
def func(s, x, y):
    print(s, x, y, '***')
    global m, n, grid
    ans_ = grid[x][y]
    s.remove((x, y))
    if len(s) == 0: return ans_
    for i in range(m):
        if (i, y) in s:
            s.remove((i, y))
    for j in range(n):
        if (x, j) in s:
            s.remove((x, j))
    print(len(s), s)
    for c, d in s:
        ans_ = max(ans_, func(s, c, d))
    return ans_
while True:
    m, n = map(int, read().split())
    if m * n == 0: sys.exit()
    grid = [tuple(map(int, read().split())) for _ in range(m)]
    ans = 1
    set_ = {(i, j) for i in range(m) for j in range(n)}
    for a, b in set_:
        ans = max(ans, func(set_, a, b))
    print(ans)

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