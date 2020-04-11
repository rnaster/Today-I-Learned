# BOJ - 1106
n, m = map(int, input().split())
dp = [987654321] * 20001
dp[0] = 0
for j in range(m):
    a, b = map(int, input().split())
    for i in range(b, 20001):
        dp[i] = min(dp[i-b] + a, dp[i])
print(min(dp[n:]))
"""
12 2
3 5
1 1
"""