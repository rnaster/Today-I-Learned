# BOJ - 2186
import sys
sys.setrecursionlimit(1000000)
n, m, k = map(int, input().split())
arr = [input() for _ in range(n)]
w = input()
dp = [[[-1] * m for _ in range(n)] for _ in range(len(w))]
def dist(a, b):
    for i in range(1, k+1):
        yield a+i, b
        yield a-i, b
        yield a, b+i
        yield a, b-i
def func(a, b, c):
    if c == len(w)-1:
        dp[c][a][b] = 1
        return 1
    val = 0
    for aa, bb in dist(a, b):
        if -1 < aa < n and -1 < bb < m and arr[aa][bb] == w[c+1]:
            val += dp[c+1][aa][bb] if dp[c+1][aa][bb] > -1 else func(aa, bb, c+1)
    dp[c][a][b] = val
    return val
ans = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == w[0]:
            ans += func(i, j, 0)
print(ans)
"""
4 4 1
KAKT
XEAS
YRWU
ZBQP
BREAK

4 4 1
KAKT
XEAS
YRWU
ZBQP
AKA
"""