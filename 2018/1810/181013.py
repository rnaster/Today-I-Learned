# BOJ - 1193
def BOJ1193():
    import math
    n = int(input())
    r = math.sqrt(2 * n + 1/4) - 1/2
    r = int(r) if r == int(r) else int(r) + 1
    c = int(n - r * (r-1) / 2)
    a, b = r+1-c, c
    if r % 2 == 0: print(str(b)+'/'+str(a))
    else: print(str(a)+'/'+str(b))

# BOJ - 11049
from sys import stdin
read = lambda : stdin.readline().rstrip()
n = int(read())
coord = [[0 for _ in range(n)] for _ in range(n)]
dp = [[10**10 for _ in range(n)] for _ in range(n)]
for i in range(n):
    coord[i][i] = tuple(map(int, read().split()))
    dp[i][i] = 0
c = 0
for i in range(n-1, 0, -1):
    c += 1
    for r in range(i):
        x, y = r, r + c
        for a, b in zip(range(1, c+1), range(c, 0, -1)):
            e, f = coord[x][y-b]
            _, g = coord[x + a][y]
            dp[x][y] = min(dp[x][y], dp[x+a][y] + dp[x][y-b] + e * f * g)
        p, _ = coord[x][y-1]
        _, q = coord[x+1][y]
        coord[x][y] = (p, q)
print(dp[0][-1])
"""
3
5 3
3 2
2 6
"""