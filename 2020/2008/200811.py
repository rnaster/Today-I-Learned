# BOJ - 2056
import sys
from collections import deque
read = sys.stdin.readline
n = int(read())
arr = [[] for _ in range(n)]
l = [[0] * n for _ in range(3)]
for i in range(n):
    a = map(int, read().split())
    l[1][i] = next(a)
    next(a)
    for aa in a:
        l[0][i] += 1
        arr[aa-1].append(i)
q = deque([i for i in range(n) if l[0][i] == 0])
ans = 0
while q:
    i = q.popleft()
    l[2][i] += l[1][i]
    ans = max(ans, l[2][i])
    for j in arr[i]:
        l[2][j] = max(l[2][j], l[2][i])
        l[0][j] -= 1
        if l[0][j] == 0: q.append(j)
print(ans)
"""
7
5 0
1 1 1
3 1 2
6 1 1
1 2 2 4
8 2 2 4
4 3 3 5 6

7
5 0
1 0
3 0
6 0
1 0
8 0
4 0
"""