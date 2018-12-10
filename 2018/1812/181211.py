# BOJ - 2666
n = int(input())
a, b = map(int, input().split())
k = int(input())
arr = [0]
dp = [[[-1 for _ in range(k+1)] for _ in range(n+1)] for _ in range(n+1)]
for _ in range(k):
    arr.append(int(input()))
def main(p, q, r):
    print(p, q, r)
    global dp
    if r == k: dp[p][q][r] = 0
    if dp[p][q][r] != -1: return dp[p][q][r]
    else:
        if dp[arr[r]][q][r+1] != -1:
            t = dp[arr[r]][q][r+1]
        else:
            t = main(arr[r], q, r+1)
        t += abs(arr[r] - p)
        if dp[p][arr[r]][r+1] != -1:
            s = dp[p][arr[p]][r+1]
        else:
            s = main(p, arr[r], r+1)
        s += abs(arr[r] - q)
        dp[p][q][r] = min(t, s)
        return dp[p][q][r]
print(main(a, b, 1))
import numpy as np
l = np.array(dp).transpose([2, 1, 0])
for i in l:
    print(*i, sep='\n')
    print('#######\n')

"""
7
2 5
4
3
1
6
5
"""