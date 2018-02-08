# BOJ - 2482
from sys import stdin
read = lambda: stdin.readline().rstrip()
n = int(read())
k = int(read())
dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
dp[3][1] = 3
dp[4][1] = 4
dp[4][2] = 2
for i in range(5, n+1):
    dp[i][1] = i
    for j in range(2, i//2+1):
        dp[i][j] = (dp[i-1][j] + dp[i-2][j-1]) % (10**9 + 3)