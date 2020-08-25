# BOJ - 2457
import sys
read = sys.stdin.readline
t = [0]
for i in [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]:
    t.append(t[-1] + i)
def func(a, b):
    return t[a-1] + b
arr = []
for _ in range(int(read())):
    a, b, c, d = map(int, read().split())
    a, b = func(a, b), func(c, d) - 1
    arr.append((a, b))
x, y = func(3, 1), func(11, 30)
l = []
arr.sort()
if arr[0][0] > x:
    print(0)
else:
    for a, b in arr:
        if a <= x:
            if x <= b:
                pass
        elif b >= x:
            pass
"""
4
1 1 5 31
1 1 6 30
5 15 8 31
6 10 12 10

3
1 1 7 10
7 10 7 11
7 10 12 31

2
3 1 3 2
3 2 12 1
"""
sys.exit()

# BOJ - 2170
import sys
read = sys.stdin.readline
ans = 0
p = q = -1_000_000_001
for a, b in sorted([[*map(int, read().split())] for _ in range(int(read()))],
                   key=lambda x: x[0]):
    if q <= a:
        ans += q - p
        p, q = a, b
    else:
        q = max(q, b)
print(ans + q - p)
"""
4
1 3
2 5
3 5
6 7
"""
exit()

# BOJ - 1766
import sys
from heapq import *
read = sys.stdin.readline
n, m = map(int, read().split())
arr = [[] for _ in range(n)]
l = [0] * n
for _ in range(m):
    a, b = map(int, read().split())
    arr[a-1].append(b-1)
    l[b-1] += 1
h = [i for i in range(n) if l[i] == 0]
heapify(h)
ans = []
while h:
    a = heappop(h)
    ans.append(a)
    for i in arr[a]:
        l[i] -= 1
        if l[i] == 0:
            heappush(h, i)
for a in ans:
    print(a+1, end=" ")
"""
4 2
4 2
3 1
"""