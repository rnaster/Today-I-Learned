# BOJ - 9020
import sys
from bisect import bisect_right as bisect
read = sys.stdin.readline
cache = {}
l = [*range(10001)]
p = []
for i in range(2, 10001):
    if l[i] > 0:
        p.append(i)
        for j in range(2*i, 10001, i):
            l[j] = 0
def func(a):
    idx = bisect(p, a)
    ans = "%s %s"
    for i in range(idx-1, -1, -1):
        for j in range(i+1, idx):
            if p[i] + p[j] > a: break
            elif p[i] + p[j] == a:
                cache[a] = ans % (p[i], p[j])
                return cache[a]
for _ in range(int(read())):
    a = int(read())
    if l[a // 2] > 0:
        print("%s %s" % (a // 2, a // 2))
    else:
        print(cache.get(a, func(a)))
"""
4
8
10
16
14
"""
exit()
# BOJ - 1695
import sys
sys.setrecursionlimit(10000000)
n = int(input())
arr = tuple(map(int, input().split()))
dp = [[-1] * n for _ in range(n)]
def func(a, b):
    global dp
    val = 0
    for _ in range((b - a + 1) // 2):
        if arr[a] == arr[b]:
            a += 1
            b += -1
        else:
            val = min(dp[a+1][b] if dp[a+1][b] != -1 else func(a+1, b),
                      dp[a][b-1] if dp[a][b-1] != -1 else func(a, b-1)) + 1
            break
    dp[a][b] = val
    return val
print(func(0, n-1))
"""
5
1 2 3 4 2

6
1 2 3 4 5 6

10
1 2 3 4 5 6 7 8 9 10
"""