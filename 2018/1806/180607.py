# BOJ - 1260
from sys import stdin
from collections import deque
from array import array
read = lambda: stdin.readline().rstrip()
queue = deque()
stack = deque()
n, m, v = map(int, read().split())
queue.append(v)
stack.append(v)
mtx = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(m):
    a, b = map(int, read().split())
    mtx[a-1][b-1] = 1
    mtx[b-1][a-1] = 1
dfs = 1
dfs_ = array('H', [])
dfs_cache = array('B', [0 for _ in range(n+1)])
bfs = 1
bfs_ = array('H', [])
bfs_cache = array('B', [0 for _ in range(n+1)])
while dfs + bfs:
    if queue:
        q = queue.popleft()
        if bfs_cache[q] == 0:
            bfs_.append(q)
            for i in range(n):
                if mtx[q-1][i] == 1:
                    queue.append(i+1)
            bfs_cache[q] = 1
    else:
        bfs = 0

    if stack:
        s = stack.popleft()
        if dfs_cache[s] == 0:
            dfs_.append(s)
            for j in range(n-1, -1, -1):
                if mtx[s-1][j] == 1:
                    stack.appendleft(j+1)
            dfs_cache[s] = 1
    else:
        dfs = 0
print(*dfs_)
print(*bfs_)
"""
4 5 1
1 2
1 3
1 4
2 4
3 4

4 3 2
2 3
3 1
1 2

5 10 1
1 2
1 3
1 4
1 5
2 3
2 4
2 5
3 4
3 5
4 5
"""