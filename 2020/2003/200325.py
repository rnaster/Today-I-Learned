# BOJ - 17404
import sys
read = sys.stdin.readline
n = int(input())
dp = [[1001] * 3 for _ in range(3)]
arr = [*map(int, read().split())]
for i in range(3):
    dp[i][i] = arr[i]
for _ in range(n-1):
    a, b, c = map(int, read().split())
    dp = [[min(dp[i][1], dp[i][2]) + a,
           min(dp[i][0], dp[i][2]) + b,
           min(dp[i][0], dp[i][1]) + c]
          for i in range(3)]
print(min(dp[i][j] for i in range(3) for j in range(3) if i != j))
"""
3
26 40 83
49 60 57
13 89 99
"""