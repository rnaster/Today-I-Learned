# BOJ - 12931
input();arr = [*map(int, input().split())]
ans = 0
while sum(arr) > 0:
    flag = 0
    tmp = []
    for a in arr:
        if a % 2:
            a -= 1
            ans += 1
            a //= 2
            if a: flag = 1;tmp.append(a)
        elif a:
            a //= 2
            flag = 1
            tmp.append(a)
    arr = tmp
    ans += flag
print(ans)
"""
5
0 0 1 0 1
"""
exit()

# BOJ - 11509
n = int(input())
ans = 0
l = [0] * 1_000_001
for i in map(int, input().split()):
    if l[i] > 0:
        l[i] -= 1
    else:
        ans += 1
    l[i-1] += 1
print(ans)
"""
5
4 5 2 1 4
"""
exit()

# BOJ - 11000
import sys
import heapq
read = sys.stdin.readline
n = int(input())
arr = sorted([*map(int, read().split())] for _ in range(n))
l = [arr[0][1]]
ans = 1
for i in range(1, n):
    a, b = arr[i]
    if l[0] <= a:
        heapq.heappop(l)
    else:
        ans += 1
    heapq.heappush(l, b)
print(ans)
"""
3
1 3
2 4
3 5
"""
exit()

# BOJ - 1744
import sys
from bisect import bisect_right as bi
read = sys.stdin.readline
arr = sorted(int(read()) for _ in range(int(read())))
i = bi(arr, 0)
l1 = arr[:i]
l2 = arr[i:]
if len(l1) % 2:
    l1.append(1)
i = bi(l2, 1)
ans = sum(l2[:i])
if (len(l2) - ans) % 2:
    ans += l2[i]
for j in range(len(l2)-1, i, -2):
    ans += l2[j] * l2[j-1]
for j in range(0, len(l1), 2):
    ans += l1[j] * l1[j+1]
print(ans)
"""
4
-1
2
1
3

6
-1
0
0
2
1
3
"""