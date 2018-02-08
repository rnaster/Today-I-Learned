# BOJ - 1937
from sys import stdin
read = lambda: stdin.readline().rstrip()
n = int(read())
grid = list(tuple(map(int, read().split())) for _ in range(n))
dp = [[-1 for _ in range(n)] for _ in range(n)]
ans = 1
def main_(a, b):
    global grid, dp, n
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        if 0 <= a + dx < n and 0 <= b + dy < n:
            a_dx, b_dy = a + dx, b + dy
            if grid[a_dx][b_dy] < grid[a][b]:
                if dp[a_dx][b_dy] == -1:
                    dp[a_dx][b_dy] = 1
                    dp[a][b] = max(dp[a][b], main_(a_dx, b_dy) + 1)
                else:
                    dp[a][b] = max(dp[a][b], dp[a_dx][b_dy] + 1)
    return dp[a][b]

def main(n):
    global ans
    for i in range(n):
        for j in range(n):
            ans = max(main_(i, j), ans)
    return ans
print(main(n))
'''
4
14 9 12 10
1 11 5 4
7 15 2 13
6 3 16 8

2 1 3 2
1 3 2 1
3 4 1 2
2 1 2 1
'''