# BOJ - 7579
from sys import stdin
from array import array
read = lambda: stdin.readline().rstrip()
n, m = map(int, read().split())
Mem = tuple(map(int, read().split()))
cost = tuple(map(int, read().split()))
dp0 = array('L', [0 for _ in range(sum(cost) + 1)])
ans = 10001
# for i in range(n):
#     dp0[cost[i]] = max(dp0[cost[i]], Mem[i])
for i in range(n):
    dp1 = array('L', [0 for _ in range(sum(cost) + 1)])
    # dp1[0] = dp0[0]
    for j in range(sum(cost)+1):
        if j >= cost[i]:
            dp1[j] = max(dp0[j], dp0[j-cost[i]] + Mem[i])
        else:
            dp1[j] = dp0[j]
        if dp1[j] >= m: ans = min(ans, j)
    # if dp1[0] >= m: ans = min(ans, 0)
    dp0 = dp1[:]
    del dp1
print(ans)

'''
5 60
30 10 20 35 40
3 0 3 5 4
'''