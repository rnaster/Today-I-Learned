# BOJ - 2159
from sys import stdin, setrecursionlimit
setrecursionlimit(10000000)
read = lambda: stdin.readline().rstrip()
n = int(read())
dp = [[-1] * (100000+1) for _ in range(4)]
l = []
for _ in range(n+1):
    l.append(tuple(map(int, read().split())))
d = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}
def func(a, i, j):
    p, q = l[a][0] + d[i][0], l[a][1] + d[i][1]
    r, s = l[a+1][0] + d[j][0], l[a+1][1] + d[j][1]
    return abs(p-r) + abs(q-s)
def main(a, b):
    global dp, l
    if dp[a][b] != -1: return dp[a][b]
    if a == n:
        dp[a][b] = 0
        return 0
    else:
        temp = 10**10+1
        for i in range(4):
            temp = min(temp,
                       dp[a+1][i] + func(a, b, i)
                       if dp[a+1][i] != -1 else main(a+1, i) + func(a, b, i))
        dp[a][b] = temp
        return dp[a][b]
for i in range(4):
    main(1, i)
c = []
for i in range(4):
    p, q = l[1][0] + d[i][0], l[1][1] + d[i][1]
    c.append(dp[1][i]+abs(p-2)+abs(q-2))
print(min(c))
"""
3
2 2
3 6
6 7
7 3
"""