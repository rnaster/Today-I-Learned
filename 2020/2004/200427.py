# BOJ - 2831
from bisect import bisect_right as bi
input()
m1, m2 = [], []
for i in map(int, input().split()):
    if i > 0: m1.append(i)
    else: m2.append(-i)
m1.sort();m2.sort()
w1, w2 = [], []
for i in map(int, input().split()):
    if i > 0: w1.append(i)
    else: w2.append(-i)
w1.sort();w2.sort()
ans = 0
i = 0
for m in m1:
    i = bi(w2, m, i)
    if i >= len(w2): break
    ans += 1
    i += 1
i = 0
for w in w1:
    i = bi(m2, w, i)
    if i >= len(m2): break
    ans += 1
    i += 1
print(ans)
"""
3
-1800 -2200 1500
1900 1700 1500
"""
exit()

# BOJ - 2180
import sys
import heapq
read = sys.stdin.readline
arr = [[] for _ in range(40_001)]
ans = 0
for _ in range(int(input())):
    a, b = map(int, read().split())
    if a: heapq.heappush(arr[a], -b)
    else: ans += b % 40_000
t = 0
for a in range(40_000, -1, -1):
    while arr[a]:
        b = -heapq.heappop(arr[a])
        t = a*t + b
        ans = (ans + t) % 40_000
print(ans)
"""
3
2 0
1 2
0 3
"""
exit()

# BOJ - 1082
n = int(input())
arr = [*map(int, input().split())]
k = int(input())
dp = [-1] * (k+1)
def func(a):
    if a == 0:
        dp[a] = 0
        return dp[a]
    val = 0
    for i, j in enumerate(arr):
        if j <= a:
            tmp = dp[a-j] if dp[a-j] > -1 else func(a-j)
            tmp = '%s%s' % (tmp, i)
            val = max(val, int(tmp))
    dp[a] = val
    return val
print(func(k))
"""
3
6 7 8
21

10
1 1 1 1 1 1 1 1 1 1
50
"""