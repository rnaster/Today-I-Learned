# BOJ - 2169
from array import array
from sys import stdin
read = lambda: stdin.readline().rstrip()
n, m = map(int, read().split())
dp = array('l', [0 for _ in range(m+1)])
lhs = array('l', [0 for _ in range(m+1)])
rhs = array('l', [0 for _ in range(m+1)])
lhs[0] = -101 * m * n
rhs[-1] = -101 * m * n
tp = tuple(map(int, read().split()))
for i in range(1, m+1):
    dp[i] = dp[i-1] + tp[i-1]
for i in range(1, n):
    tp = tuple(map(int, read().split()))
    for j in range(1, m+1):
        lhs[j] = max(lhs[j-1], dp[j]) + tp[j-1]
    for k in range(m-1, -1, -1):
        rhs[k] = max(rhs[k+1], dp[k+1]) + tp[k]
    for p in range(m):
        dp[p+1] = max(lhs[p+1], rhs[p])
print(dp[-1])

"""
5 5
10 25 7 8 13
68 24 -78 63 32
12 -69 100 -29 -25
-16 -22 -57 -33 99
7 -76 -11 77 15

3 3
-99 -99 -99
-80 -80 -80
-70 -70 -70
"""