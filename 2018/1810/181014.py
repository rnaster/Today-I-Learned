# BOJ - 11066
from sys import stdin
read = lambda : stdin.readline().rstrip()
for _ in range(int(read())):
    n = int(read())
    tp = tuple(map(int, read().split()))
    # cum = [[0 for _ in range(n)] for _ in range(n)]
    dp = [[5000001 for _ in range(n)] for _ in range(n)]
    for i in range(n): dp[i][i] = 0
    # for i in range(n):
    #     cum[i][i] = tp[i]
    #     dp[i][i] = 0
    #     for j in range(i+1, n):
    #         cum[i][j] = cum[i][j-1] + tp[j]
    c = 0
    for i in range(n-1, 0, -1):
        c += 1
        for r in range(i):
            x, y = r, r + c
            cum = sum(tp[x:y+1])
            for a, b in zip(range(1, c+1), range(c, 0, -1)):
                # dp[x][y] = min(dp[x][y], dp[x+a][y] + dp[x][y-b] + cum[x][y])
                dp[x][y] = min(dp[x][y], dp[x + a][y] + dp[x][y - b] + cum)
    print(dp[0][-1])
"""
2
4
40 30 30 50
15
1 21 3 4 5 35 5 4 3 5 98 21 14 17 32
"""
# for i in range(n):
#     coord[i][i] = tuple(map(int, read().split()))
#     dp[i][i] = 0
# c = 0
# for i in range(n-1, 0, -1):
#     c += 1
#     for r in range(i):
#         x, y = r, r + c
#         for a, b in zip(range(1, c+1), range(c, 0, -1)):
#             e, f = coord[x][y-b]
#             _, g = coord[x + a][y]
#             dp[x][y] = min(dp[x][y], dp[x+a][y] + dp[x][y-b] + e * f * g)
#         p, _ = coord[x][y-1]
#         _, q = coord[x+1][y]
#         coord[x][y] = (p, q)
# print(dp[0][-1])