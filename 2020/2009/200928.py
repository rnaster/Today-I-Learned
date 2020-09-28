# BOJ - 1655
import sys
from heapq import *
read = sys.stdin.readline
n = int(read())
a = int(read())
arr = [[(-a, a)], []]
print(a)
for i in range(1, n):
    a = int(read())
    if arr[0][0][1] >= a:
        if i % 2:
            _, b = heappop(arr[0])
            heappush(arr[1], b)
        heappush(arr[0], (-a, a))
    else:
        heappush(arr[1], a)
        if i % 2 == 0:
            b = heappop(arr[1])
            heappush(arr[0], (-b, b))
    print(arr[0][0][1])
"""
7
1
5
2
10
-99
7
5
"""