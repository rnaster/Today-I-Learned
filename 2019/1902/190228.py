# BOJ - 1102
from sys import setrecursionlimit
setrecursionlimit(10000000)
n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]
dp = [-1]*(1 << n)
onoff = input()
p = int(input())
v, q = 0, 0
for i in range(n):
    if onoff[i] == 'Y':
        v |= 1 << i
        q += 1
if p <= q: print(0);exit()
def main(visit, visit_n):
    if visit_n == p:
        dp[visit] = 0
        return dp[visit]
    else:
        temp = 987654321
        for i in range(n):
            if not visit & 1 << i:
                for j in range(n):
                    if visit & 1 << j:
                        val = dp[visit|1<<i] if dp[visit|1<<i] != -1 else main(visit | 1 << i, visit_n+1)
                        temp = min(temp, val + arr[j][i])
        dp[visit] = temp
        return dp[visit]
if 0 < q < p:
    print(main(v, q))
else:
    print(-1)
"""
3
0 10 11
10 0 12
12 13 0
NYN
3
"""
