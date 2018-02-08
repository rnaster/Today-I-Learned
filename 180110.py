# BOJ - 2718
from sys import stdin
from array import array
read = lambda: stdin.readline().rstrip()
dp = array('L', [1, 1, 5])
M = 2
def f(N):
    global dp, M
    if N <= M: return
    for _ in range(M, N):
        dp.append(dp[-1] + dp[-2] * 4 + sum(dp[:-2]) * 2 + sum(dp[:-3][::-2]))
    M = N
for _ in range(int(read())):
    n = int(read())
    f(n)
    print(dp[n])

'''
3
2
3
7
'''