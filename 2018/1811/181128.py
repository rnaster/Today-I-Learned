# BOJ - 1351
from sys import setrecursionlimit
setrecursionlimit(10000000)
dp = {0:1}
n, p, q = map(int, input().split())
if n == 0: print(1);exit()
def main(n):
    global dp
    if n // p in dp.keys(): a = dp[n//p]
    else: a = main(n // p); dp[n//p] = a
    if n // q in dp.keys(): b = dp[n // q]
    else: b = main(n // q); dp[n//q] = b
    dp[n] = a + b
    return a + b
print(main(n))
"""
7 2 3
"""