# BOJ - 1256
import sys
m, n, k = map(int, input().split())
dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
for i in range(m+1):
    for j in range(n+1):
        if i == 0 or j == 0:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

if dp[m][n] < k: print(-1); sys.exit()


def main(M, N, K):
    if M == 0 or N == 0: return 'a' * M + 'z' * N
    else:
        if dp[M-1][N] >= K:
            return 'a' + main(M-1, N, K)
        else:
            return 'z' + main(M, N-1, K-dp[M-1][N])


print(main(m, n, k))