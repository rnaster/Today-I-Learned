# BOJ - 1509
import sys
sys.setrecursionlimit(1000000)
a = input()
n = len(a)
dp = [[-1]*n for _ in range(n)]
def func(p, q):
    if dp[p][q] != -1:
        return dp[p][q]
    if a[p] != a[q]:
        dp[p][q] = 0
        return dp[p][q]
    else:
        if q - p < 2:
            dp[p][q] = 1
            return dp[p][q]
        dp[p][q] = func(p+1, q-1)
        return dp[p][q]
for i in range(n):
    dp[i][i] = 1
    for j in range(i+1, n):
        if dp[i][j] == -1:
            func(i, j)
arr = [-1]*n
arr[0] = 1
def main(p):
    if p < 0: return 0
    if arr[p] != -1: return arr[p]
    else:
        temp = 2501
        for i in range(p, -1, -1):
            if dp[i][p] > 0:
                val = main(i-1) if arr[i-1] < 0 else arr[i-1]
                temp = min(temp, val+1)
        arr[p] = temp
    return arr[p]
print(main(n-1))
"""
BBCDDECAECBDABADDCEBACCCBDCAABDBADD
AABBBC
"""
exit()

# BOJ - 10409
n, t = map(int, input().split())
ans = 0
for w in map(int, input().split()):
    if t - w >= 0:t -= w;ans += 1
    else: break
print(ans)
"""
6 180
45 30 55 20 80 20

10 60
20 7 10 8 10 27 2 3 10 5
"""