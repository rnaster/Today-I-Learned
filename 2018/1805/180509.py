# BOJ - 2698
from sys import stdin
read = lambda : stdin.readline().rstrip()

dp = [[0 for _ in range(101)] for _ in range(101)]
dp[2][0] = 3
dp[2][1] = 1
dp[3][0] = 5
dp[3][1] = 2
dp[3][2] = 1
idx = 3
for _ in range(int(read())):
    n, k = map(int, read().split())
    if idx < n:
        for i in range(idx+1, n+1):
            for j in range(n+1):
                if i > j:
                    dp[i][j] = dp[i - 1][j] + dp[i - 2][j]
                    if j == 0:
                        continue
                    dp[i][j] += dp[i-1][j-1] - dp[i-2][j-1]
        print(dp[n][k])
        idx = n
    else:
        print(dp[n][k])

'''
10
5 2
20 8
30 17
40 24
50 37
60 52
70 59
80 73
90 84
100 90
'''