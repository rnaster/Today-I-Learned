# BOJ - 10835
from sys import stdin
read = lambda: stdin.readline().rstrip()
n = int(read())
L = tuple(map(int, read().split()))
R = tuple(map(int, read().split()))
dp = [[-1 for _ in range(n)] for _ in range(n)]

def main(n, m):
    global dp
    if dp[n][m] != -1: return dp[n][m]
    if n == 0:
        dp[n][m] = R[n] if R[n] < L[m] else 0
        return dp[n][m]
    if m == 0:
        if R[n-1] < L[m]:
            dp[n][m] = main(n-1, m)
            dp[n][m] += R[n] if R[n] < L[m] else 0
        else:
            dp[n][m] = 0
        return dp[n][m]
    else:
        c1 = main(n, m-1) if R[n] >= L[m-1] else 0
        c2 = main(n-1, m-1) if R[n-1] >= L[m-1] else 0
        c3 = main(n-1, m) if R[n-1] < L[m] else 0
        dp[n][m] = max(c1, c2, c3)
        dp[n][m] += R[n] if R[n] < L[m] else 0
        return dp[n][m]
print(main(n-1, n-1))

'''
3
3 2 5
2 4 1
4
1 2 3 4
4 1 2 3
'''