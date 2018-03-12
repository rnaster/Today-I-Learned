# BOJ - 1699
from array import array
n = int(input())
dp = array('B', [0 for _ in range(n+1)])
for i in range(1, n+1):
    j = 1
    m = 100001
    while j*j <= i:
        m = min(m, dp[i-j*j])
        j += 1
    dp[i] = m + 1
print(dp[-1])
