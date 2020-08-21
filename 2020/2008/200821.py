# BOJ - 4811
import sys
read = sys.stdin.readline
ans = [0] * 31
dp = None
def func(w, h):
    if w == 0:
        dp[w][h] = 1
        return 1
    val = dp[w-1][h+1] if dp[w-1][h+1] > -1 else func(w-1, h+1)
    if h == 0:
        dp[w][h] = val
        return val
    val += dp[w][h-1] if dp[w][h-1] > -1 else func(w, h-1)
    dp[w][h] = val
    return val
while 1:
    n = int(read())
    if n == 0: break
    if ans[n] > 0: print(ans[n]); continue
    dp = [[-1] * (n+1) for _ in range(n+1)]
    ans[n] = func(n, 0)
    print(ans[n])
"""
6
1
4
2
3
30
0
"""