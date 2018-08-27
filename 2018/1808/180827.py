# BOJ - 1328
from sys import setrecursionlimit
setrecursionlimit(10000000)
n, l, r = map(int, input().split())
if n == 1: print(1);exit()
dp = [[[-1 for _ in range(n + 1)] for _ in range(n + 1)] for _ in range(n + 1)]
dp[1][1][1] = 1
def main(N, L, R):
    print(N, L, R, '*')
    global dp
    if dp[N][L][R] != -1: return dp[N][L][R]
    else:
        a, b, c = 0, 0, 0
        if L + R > 3:
            if 2 <= L and L + R <= N + 1:
                a = dp[N-1][L-1][R] if dp[N-1][L-1][R] != -1 else main(N-1, L-1, R)
            if L + R <= N:
                b = dp[N-1][L][R] * (N-2) if dp[N-1][L][R] != -1 else main(N-1, L, R) * (N-2)
            if 2 <= R and L + R <= N + 1:
                c = dp[N-1][L][R-1] if dp[N-1][L][R-1] != -1 else main(N-1, L, R-1)
        elif L + R == 3:
            if 2 <= N < 4:
                dp[N][L][R] = 1
                return 1
            elif 4 <= N:
                b = dp[N-1][L][R] * (N-2) if dp[N-1][L][R] != -1 else main(N-1, L, R) * (N-2)
        dp[N][L][R] = (a + b + c) % 1000000007
        return dp[N][L][R]
print(main(n, l, r))

# for arr in dp:
#     print(*arr, sep='\n')
#     print()
"""
3 2 2
"""