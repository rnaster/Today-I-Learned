# BOJ - 1689
import sys
from collections import deque
read = sys.stdin.readline
n = int(input())
arr = [[*map(int, read().split())] for _ in range(n)]
arr.sort()
q = deque()
ans = 1
tmp = 1
c, d = arr[0]
q.append((c, d))
for i in range(1, n):
    a, b = arr[i]
    q.append((a, b))
    if c < a+0.1 < d or c < b-0.1 < d:
        tmp += 1
        c, d = max(c, a), min(d, b)
    else:
        ans = max(ans, tmp)
        cc, dd = a, b
        while q:
            a, b = q[0]
            if cc < a+0.1 < dd or cc < b-0.1 < dd:
                c, d = max(cc, a), min(dd, b)
                break
            else:
                if c < a + 0.1 < d or c < b - 0.1 < d:
                    tmp -= 1
                q.popleft()
print(ans)
"""
11
1 2
3 6
7 8
10 11
13 16
0 5
5 6
2 5
6 10
9 14
12 15
"""
exit()

# BOJ - 1263
n = int(input())
arr = [[*map(int, input().split())] for _ in range(n)]
arr.sort(key=lambda x: (-x[1], -x[0]))
ans = 1000001
for a, b in arr:
    ans = min(ans, b) - a
    if ans < 0: print(-1);exit()
print(ans)
"""
4
3 5
8 14
5 20
1 16

2
1 2
1 2
"""