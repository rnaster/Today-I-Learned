# BOJ - 10835
from sys import setrecursionlimit
setrecursionlimit(1000000)
n = int(input())
L = tuple(map(int, input().split()))
R = tuple(map(int, input().split()))
dp = [[-1 for _ in range(n)] for _ in range(n)]
def main(r, l):
    global dp
    if dp[r][l] != -1: return dp[r][l]
    else:
        if r == 0:
            dp[r][l] = R[-1] if R[-1] < L[n-1-l] else 0
            return dp[r][l]
        elif l == 0:
            if 0 < r:
                dp[r][l] = dp[r-1][l] if dp[r-1][l] != -1 else main(r-1, l)
                if R[n-1-r] < L[n-1-l]: dp[r][l] += R[n-1-r]
            return dp[r][l]
        else:
            val = 0
            a = dp[r][l-1] if dp[r][l-1] != -1 else main(r, l-1)
            b = dp[r-1][l-1] if dp[r-1][l-1] != -1 else main(r-1, l-1)
            c = -1
            if R[n-1-r] < L[n-1-l]:
                c = dp[r-1][l] if dp[r-1][l] != -1 else main(r-1, l)
                c += R[n-1-r]
            val = max(val, a, b, c)
            dp[r][l] = val
            return dp[r][l]
main(n-1, n-1)
print(*dp, sep='\n')

"""
3
3 2 5
2 4 1

4
1 2 3 4
4 1 2 3
"""