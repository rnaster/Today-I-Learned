# BOJ - 7453
import sys
read = sys.stdin.readline
from bisect import bisect_left as bi
n = int(input())
arr = [[0] * n for _ in range(4)]
for i in range(n):
    a, b, c, d = map(int, read().split())
    arr[0][i] = a
    arr[1][i] = b
    arr[2][i] = c
    arr[3][i] = d
arr[0].sort();arr[1].sort()
l = sorted(arr[2][i] + arr[3][j]
           for i in range(n) for j in range(n))
s = n*n - 1
ans = 0
for i in range(n):
    for j in range(n):
        t = arr[0][i] + arr[1][j]
        if t + l[0] > 0 or t + l[-1] < 0: break
        idx = bi(l, -t)
        if l[min(idx, s)] == -t: ans += 1
print(ans)
"""
6
-45 22 42 -16
-41 -27 56 30
-36 53 -37 77
-36 30 -75 -46
26 -38 -10 62
-32 -54 -6 45
"""