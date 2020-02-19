# BOJ - 1577
n, m = map(int, input().split())
l = [[] for _ in range(n+1)]
for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    a, c = min(a, c), max(a, c)
    b, d = min(b, d), max(b, d)
    l[b].append((b, a, d, c))
dp = [[0] * (m+2) for _ in range(2)]
dp[0][0] = 1
ii = 1
for i in range(n+1):
    ii = (i+1) % 2
    for j in range(m+1):
        dp[ii][j] = 0
        if (i-1, j, i, j) in l[i-1]: pass
        else: dp[ii][j] += dp[1-ii][j]
        if (i, j-1, i, j) in l[i]: pass
        else: dp[ii][j] += dp[ii][j-1]
    print(*dp, '', sep='\n')
print(dp[ii][-2])
"""
6 6
2
0 0 0 1
2 0 2 1

1 1
2
0 1 1 1
1 0 0 0
"""