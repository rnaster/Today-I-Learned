# BOJ - 1737
import sys
sys.setrecursionlimit(1000000)
from math import pi
n = int(input())
dp = [[-1] * n for _ in range(n+1)]
def func(a, b):
    if 0 <= a - pi * b <= pi:
        dp[a][b] = 1
        return 1
    val = 0
    val += dp[a-1][b] if dp[a-1][b] > -1 else func(a-1, b)
    val += dp[a][b+1] if dp[a][b+1] > -1 else func(a, b+1)
    dp[a][b] = val % 1000000000000000000
    return dp[a][b]
print(func(n, 0))
"""
10
"""