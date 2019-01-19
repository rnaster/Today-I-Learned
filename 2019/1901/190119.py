# BOJ - 11066
for _ in range(int(input())):
    k = int(input())
    tp = tuple(map(int, input().split()))
    dp = [[10**10] * k for _ in range(k)]
    grid = [0] * (k+1)
    for i in range(k):
        dp[i][i] = 0
        grid[i+1] += grid[i] + tp[i]
    c = 0
    for i in range(k-1, 0, -1):
        c += 1
        for r in range(i):
            x, y = r, r + c
            for a, b in zip(range(1, c+1), range(c, 0, -1)):
                dp[x][y] = min(dp[x][y], dp[x][y-b] + dp[x+a][y] + grid[y+1] - grid[x+1] + tp[x])
    print(dp[0][-1])
"""
2
4
40 30 30 50
15
1 21 3 4 5 35 5 4 3 5 98 21 14 17 32
"""
