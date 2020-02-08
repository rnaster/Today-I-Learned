# BOJ - 3114
import sys
sys.setrecursionlimit(100000000)
n, m = map(int, input().split())
arr = [input().split() for _ in range(n)]
cache1 = [[0] * m for _ in range(n)]
cache2 = [[0] * m for _ in range(n)]
for j in range(m):
    for i in range(1, n):
        cache1[-i][j] += int(arr[-i][j][1:]) + cache1[-i+1][j]\
            if arr[-i][j][0] == 'A' else cache1[-i+1][j]
for i in range(n):
    for j in range(1, m):
        cache2[i][-j] += int(arr[i][-j][1:]) + cache2[i][-j+1]\
            if arr[i][-j][0] == 'B' else cache2[i][-j+1]
dp = [[-1] * m for _ in range(n)]
def func(a, b):
    if (a, b) == (n-1, m-1):
        dp[a][b] = 0
        return dp[a][b]
    val = 0
    _a, _b = (a+1) % n, (b+1) % m
    if a < n-1 and b < m-1:
        tmp = dp[a+1][b+1] if dp[a+1][b+1] > -1 else func(a+1, b+1)
        tmp += cache1[_a][b] + cache2[a][_b]
        val = max(val, tmp)
    if a < n-1:
        tmp = dp[a + 1][b] if dp[a + 1][b] > -1 else func(a + 1, b)
        tmp += cache2[a][_b]
        val = max(val, tmp)
    if b < m-1:
        tmp = dp[a][b + 1] if dp[a][b+1] > -1 else func(a, b + 1)
        tmp += cache1[_a][b]
        val = max(val, tmp)
    dp[a][b] = val
    return dp[a][b]
print(func(0, 0))
"""
4 3
B2 B3 B5
A3 B1 A1
A2 A4 B1
B1 B3 A3
"""