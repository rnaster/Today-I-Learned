# BOJ - 10836
import sys
from itertools import chain
read = sys.stdin.readline
n, m = map(int, read().split())
arr = [[1] * n for _ in range(n)]
l1 = [0] * (2*n-1)
l2 = [0] * (n-1)
for _ in range(m):
    a, b, c = map(int, read().split())
    i = -1
    for d, i in zip(chain([2] * c, [1] * b), range(-1, -n, -1)):
        l1[i] += d
        l2[i] += d
    if c < n-1:
        cc = 0
        bb = b+c-n+1
    else:
        cc = c-n+1
        bb = b
    for d, j in zip(chain([2] * cc, [1] * bb), range(i-1, -n*2, -1)):
        l1[j] += d
i, j, k = n-1, 0, 0
for i in range(n-1, -1, -1):
    arr[i][0] += l1[k]
    k += 1
for j in range(1, n):
    arr[0][j] += l1[k]
    k += 1
    for i in range(1, n):
        arr[i][j] += l2[j-1]
for a in arr:
    print(*a)
"""
4 2
2 3 2
0 6 1

2 3
1 1 1
0 3 0
0 0 3
"""