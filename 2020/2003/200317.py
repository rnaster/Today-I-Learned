# BOJ - 2305
n = int(input());k = int(input())
dp = [[0] * (n+1) for _ in range(4)]
if k > 1:
    dp[0][1] = dp[3][1] = 1
    if k > 2: dp[2][1] = 1
    a = 2
else:
    dp[0][2] = dp[2][2] = dp[3][2] = 1
    a = 3
for i in range(a, n+1):
    if i == k:
        dp[0][i], dp[0][i-1] = dp[0][i-1], dp[0][i-2]
        dp[1][i], dp[1][i - 1] = dp[1][i - 1], dp[1][i - 2]
        dp[2][i], dp[2][i - 1] = dp[2][i - 1], dp[2][i - 2]
        dp[3][i], dp[3][i - 1] = dp[3][i - 1], dp[3][i - 2]
        continue
    dp[0][i] = dp[0][i-1] + dp[1][i-1] + dp[3][i-1]
    dp[3][i] = sum(dp[j][i-1] for j in range(3))
    if i-1 != k:
        dp[1][i] = dp[1][i-1] + dp[2][i-1] + dp[3][i-1]
    dp[3][i] -= sum(dp[3][i-2] if dp[j][i-1] > 0 else 0
                    for j in range(3))
    if i+1 != k and i + 1 <= n:
        dp[2][i] = dp[0][i-1] + dp[1][i-1] + dp[2][i-1] + dp[3][i-1]
print(sum(dp[i][-1] for i in range(4)))
"""
4
3
"""