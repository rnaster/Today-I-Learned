# BOJ - 2141
import sys
read = sys.stdin.readline
n = int(input())
arr = [[*map(int, read().split())] for _ in range(n)]
arr.sort(key=lambda x: x[0])
l = [[0, 0] for _ in range(n)]
for i in range(n):
    l[i][0] = l[i-1][0] + arr[i][1] * i * (arr[i][0] - arr[i-1][0])
    l[-i-1][1] = l[-i][1] + arr[-i-1][1] * i * (arr[-i][0] - arr[-i-1][0])
print(*l, sep='\n')
print(arr[min(enumerate(l), key=lambda x: sum(x[1]))[0]][0])
"""
3
1 3
2 5
3 3
"""
exit()

# BOJ - 1461
from bisect import bisect as bi
n, m = map(int, input().split())
arr = sorted(map(int, input().split()))
idx = bi(arr, 0)
a, b = arr[:idx], arr[idx:]
def func1(a, i):
    ans_ = 0
    for ii in range(i, len(a), m):
        ans_ += a[ii] * 2
    return abs(ans_)
def func2(b, j):
    ans_ = 0
    for jj in range(j, -len(b)-1, -m):
        ans_ += b[jj] * 2
    return ans_
ans = 0
if len(a) > 0 and len(b) > 0:
    i, j = 0, -1
    if abs(a[0]) > abs(b[-1]):
        i = m
        ans = abs(a[0])
    else:
        j += -m
        ans = abs(b[-1])
    ans += func1(a, i) + func2(b, j)
elif len(a) > 0:
    ans = abs(a[0]) + func1(a, m)
else:
    ans = abs(b[-1]) + func2(b, -m-1)
print(ans)
"""
7 2
-37 2 -6 -39 -29 11 -28

7 2
37 -2 6 39 29 -11 28

10 3
-200 -100 1 2 3 4 5 6 7 8
"""