# BOJ - 1695
import sys
from array import array
sys.setrecursionlimit(10000000)
n = int(input())
arr = tuple(map(int, input().split()))
dp = [array('h', [-1]*i) for i in range(n, 0, -1)]
# print(*dp, sep='\n')
def main(a, b):
    if dp[a][b-a] != -1: return dp[a][b-a]
    if a == b:
        dp[a][b-a] = 0
        return dp[a][b-a]
    else:
        # if arr[a] == arr[b]:
        #     if a+1 > b-1:
        #         dp[a][b] = 0
        #         return dp[a][b]
        #     return main(a+1, b-1)
        # else:
        #     p = dp[a + 1][b] if dp[a + 1][b] != -1 else main(a + 1, b)
        #     q = dp[a][b - 1] if dp[a][b - 1] != -1 else main(a, b - 1)
        #     dp[a][b] = min(p, q) + 1
        #     return dp[a][b]
        d = 0
        while True:
            if arr[a+d] != arr[b-d]: break
            d += 1
            if a+d >= b-d:
                dp[a][b-a] = 0
                return dp[a][b-a]
        # print(a, b, 'a+d+1: %s, b-d-a: %s' % (a+d+1, b-d-a))
        p = dp[a+d+1][b-d-a-1] if dp[a+d+1][b-d-a-1] != -1 else main(a+d+1, b-d)
        q = dp[a+d][b-d-1-a] if dp[a+d][b-d-1-a] != -1 else main(a+d, b-d-1)
        dp[a][b-a] = min(p, q) + 1
        return dp[a][b-a]
print(main(0, n-1))
print(*dp, sep='\n')
"""
1
1

5
1 2 3 4 2

6
1 2 3 3 2 1

3
1 1 2

0 2 0
1 2 0
0 1 0
[0, 1, 2]
[-1, 0, 1]
[-1, -1, 0]

0 2
1 2
2 2
1 1
0 1
[-1, 0, 1]
[-1, 0, 1]
[-1, -1, 0]
"""