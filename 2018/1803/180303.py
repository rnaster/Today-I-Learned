# BOJ - 1328
n, l, r = map(int, input().split())
dp = [[[-1 for _ in range(n)] for _ in range(n)] for _ in range(n)]
dp[0][0][0] = 1
dp[1][0][0] = 0
dp[1][1][0] = 1
dp[1][0][1] = 1

def main(n, l, r):
    global dp
    print(n, l, r)
    if dp[n][l][r] != -1: return dp[n][l][r]
    else:
        dp[n][l][r] = 0
        if n >= 2 and n-1 >= l and n-1 >= r:
            dp[n][l][r] += main(n-1, l-1, r) if l > 0 else 0
            dp[n][l][r] += main(n-1, l, r) * (n-1) if l > 0 and r > 0 else 0
            dp[n][l][r] += main(n-1, l, r-1) if r > 0 else 0
            dp[n][l][r] = dp[n][l][r] % 1000000007
            return dp[n][l][r]
        elif n in [0, 1] and n >= l and n >= r:
            return dp[n][l][r]
        return dp[n][l][r]
        # if n >= 2 and n >= l > 0 and n >= r > 0:
        #     dp[n][l][r] = (main(n-1, l-1, r) + (n-2)*main(n-1, l, r) + main(n-1, l, r-1)) % 1000000007
        #     return dp[n][l][r]
        # elif n >= 0 and l > 0 and r > 0:
        #     return dp[n][l][r]
        # else:
        #     return 0
print(main(n-1, l-1, r-1))
from pprint import pprint
pprint(dp)
'''
3 2 2
'''