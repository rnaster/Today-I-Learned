def BOJ7579():
    # BOJ - 7579
    from sys import stdin
    from array import array
    read = lambda: stdin.readline().rstrip()
    n, m = map(int, read().split())
    Mem = tuple(map(int, read().split()))
    cost = tuple(map(int, read().split()))
    dp0 = array('L', [0 for _ in range(sum(cost) + 1)])
    ans = 10001
    for i in range(n):
        dp1 = array('L', [0 for _ in range(sum(cost) + 1)])
        for j in range(sum(cost)+1):
            if j >= cost[i]:
                dp1[j] = max(dp0[j], dp0[j-cost[i]] + Mem[i])
            else:
                dp1[j] = dp0[j]
            if dp1[j] >= m: ans = min(ans, j)
        dp0 = dp1[:]
        del dp1
    print(ans)
    '''
    5 60
    30 10 20 35 40
    3 0 3 5 4
    '''
# BOJ - 1520
from sys import stdin
read = lambda: stdin.readline().rstrip()
N, M = map(int, read().split())
grid = []
for _ in range(N):
    grid.append(tuple(map(int, read().split())))
dp = [[-1 for _ in range(M)] for _ in range(N)]
dp[-1][-1] = 0
dp[0][0] = 1
def main(n, m):
    global dp, grid
    # print(n, m)
    # if dp[n][m] != -1: return dp[n][m]
    if n == 0 and m == 0: return 1
    else:
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            # print(dx, dy, '#')
            if 0 <= n + dx < N and 0 <= m + dy < M:
                n_dx, m_dy = n + dx, m + dy
                # print(n_dx, m_dy, '**')
                if dp[n_dx][m_dy] == -1 and grid[n_dx][m_dy] > grid[n][m]:
                    dp[n_dx][m_dy] = 0
                    dp[n][m] += main(n_dx, m_dy)
                elif dp[n_dx][m_dy] != -1 and grid[n_dx][m_dy] > grid[n][m]:
                    dp[n][m] += dp[n_dx][m_dy]
        return dp[n][m]
print(main(N-1, M-1))
'''
4 5
50 45 37 32 30
35 50 40 20 25
30 30 25 17 28
27 24 22 15 10
'''