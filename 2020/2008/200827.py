# BOJ - 1484
n = int(input())
a, b = 1, 2
l = [i*i for i in range(100_000)]
flag = True
while a < b:
    t = l[b] - l[a]
    if t > n:
        a += 1
    else:
        if t == n:
            print(b)
            flag = False
        b += 1
if flag:
    print(-1)
"""
15
"""
exit()

# BOJ - 14226
n = int(input())
q = {(1, 0)}
ans = 0
while 1:
    tmp = set()
    for a, b in q:
        if a == n: print(ans);exit()
        if b > 0:
            tmp.add((a+b, b))
        if a > 0:
            tmp.add((a-1, b))
            if a != b:
                tmp.add((a, a))
    q = tmp
    ans += 1
"""
18
"""
exit()

# BOJ - 1939
import sys
from heapq import *
read = sys.stdin.readline
n, m = map(int, read().split())
h = []
l = [[-1, 1_000_000_001] for _ in range(n)]
for _ in range(m):
    *a, b = map(int, read().split())
    heappush(h, (-b, a))
x, y = map(int, read().split())
def find(a):
    if l[a][0] == -1:
        return a
    l[a][0] = find(l[a][0])
    return l[a][0]
while h:
    c, (a, b) = heappop(h)
    aa = find(a-1)
    bb = find(b-1)
    if aa == bb: continue
    c = min(-c, l[aa][1], l[bb][1])
    l[bb][0] = aa
    l[bb][1] = l[aa][1] = c
    if find(x-1) == find(y-1):
        print(l[find(x-1)][1])
        break
"""
3 3
1 2 2
3 1 3
2 3 2
1 3
"""