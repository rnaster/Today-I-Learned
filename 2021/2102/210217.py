# BOJ - 1535
import sys
sys.setrecursionlimit(10**6)
n = int(input())
arr = [[*map(int, input().split())], [*map(int, input().split())]]
dp = [[-1] * 101 for _ in range(n)]
def func(a, b):
    if a == 0:
        dp[a][b] = 0
        if b > arr[0][a]:
            dp[a][b] = arr[1][a]
        return dp[a][b]
    val = dp[a-1][b] if dp[a-1][b] > -1 else func(a-1, b)
    if b > arr[0][a]:
        tmp = dp[a-1][b-arr[0][a]] if dp[a-1][b-arr[0][a]] > -1 else func(a-1, b-arr[0][a])
        val = max(val, tmp + arr[1][a])
    dp[a][b] = val
    return val
print(func(n-1, 100))
"""
3
1 21 79
20 30 25
"""