# BOJ - 1918
from collections import deque
l = deque()
o = ('*', '+', '-', '/')
b = ('(', ')')
for i in input():
    if i in b: continue
    if i in o:
        l.appendleft(i)
    else:
        l.append(i)
print(''.join(l))
"""
A*(B+C)
A+B*C-D/E
"""
exit()

# BOJ - 2285
import sys
read = sys.stdin.readline
n = int(read())
arr = sorted([[*map(int, read().split())] for _ in range(n)],
             key=lambda x: x[0])
if n == 1: print(1);exit()
l = enumerate([arr[i][1] * (arr[i][0] - arr[i-1][0])
               for i in range(1, n)], 1)
a, b = max(l, key=lambda x: (x[1], -x[0]))
ll = enumerate([arr[i][0] * (arr[i+1][0] - arr[i][0])
               for i in range(n-1)], 2)
c, d = max(ll, key=lambda x: (x[1], -x[0]))
if b > d:
    print(min(a+1, n-1))
elif b < d:
    print(min(c-1, 2))
else:
    print(min(a+1, c-1))
"""
3
1 3
2 5
3 3
"""
exit()

# BOJ - 2513
import sys
read = sys.stdin.readline
n, s, k = map(int, input().split())
arr = [0] * 100_001
for _ in range(n):
    a, b = map(int, read().split())
    arr[a] = b
ans = 0
for l in [range(k), range(100_000, k, -1)]:
    ss = s
    flag = True
    for i in l:
        if not arr[i]: continue
        if flag:
            a, b = divmod(arr[i], s)
            ans += 2*a*abs(i - k)
            if b:
                ans += 2*abs(i - k)
                ss = s - b
                flag = False
        elif arr[i] <= ss:
            ss -= arr[i]
        else:
            a, b = divmod(arr[i] - ss, s)
            ans += 2*a*abs(i - k)
            if b:
                ans += 2*abs(i - k)
                ss = s - b
            else:
                flag = True
print(ans)
"""
3 4 4
0 5
2 5
5 1
"""
exit()

# BOJ - 8983
import sys
from bisect import bisect_left as bi
read = sys.stdin.readline
n, m, l = map(int, read().split())
arr = sorted(map(int, read().split()))
ans = 0
def func(i, a, b):
    return abs(arr[i] - a) + b <= l
for _ in range(m):
    a, b = map(int, read().split())
    ii = bi(arr, a)
    i, ii, iii = max(ii-1, 0), min(ii, n-1), min(ii+1, n-1)
    if func(i, a, b) | func(ii, a, b) | func(iii, a, b):
        ans += 1
print(ans)
"""
4 8 4
6 1 4 9
7 2
3 3
4 5
5 1
2 2
1 4
8 4
9 4
"""