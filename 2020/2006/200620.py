# BOJ - 2637
from collections import deque
n = int(input())
arr = [[] for _ in range(n)]
l = [0] * n
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    arr[b-1].append((a-1, c))
    l[a-1] += 1
q = deque()
d = [[0] * n for _ in range(n)]
for i, ll in enumerate(l):
    if ll == 0:
        q.append(i)
        d[i][i] += 1
while q:
    i = q.popleft()
    for j, c in arr[i]:
        d[j] = [x + y * c for x, y in zip(d[j], d[i])]
        l[j] -= 1
        if l[j] == 0:
            q.append(j)
for i, j in enumerate(d[-1], 1):
    if j > 0:
        print(i, j)
"""
7
8
5 1 2
5 2 2
7 5 2
6 5 2
6 3 3
6 4 4
7 6 3
7 4 5
"""
exit()

# BOJ - 1516
from collections import deque
n = int(input())
arr = [[] for _ in range(n)]
l = [[0] * n for _ in range(3)]
for i in range(n):
    m = map(int, input().split())
    l[1][i] = next(m)
    for j in m:
        if j == -1: break
        arr[j-1].append(i)
        l[0][i] += 1
q = deque()
for i in range(n):
    if l[0][i] == 0:
        q.append(i)
while q:
    i = q.popleft()
    l[2][i] += l[1][i]
    for j in arr[i]:
        l[2][j] = max(l[2][j], l[2][i])
        l[0][j] -= 1
        if l[0][j] == 0:
            q.append(j)
for i in range(n):
    print(l[2][i])
"""
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1
"""