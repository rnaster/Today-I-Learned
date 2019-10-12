# BOJ - 2146
from itertools import combinations
n = int(input())
arr = [[*map(int, input().split())] for _ in range(n)]
group = {}
visit = [[0] * n for _ in range(n)]
d = ((0, 1), (0, -1), (1, 0), (-1, 0))
def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) - 1
def bfs(a, b):
    l = [(a, b)]
    stack = [(a, b)]
    while stack:
        _stack = []
        for x, y in stack:
            for dx, dy in d:
                if -1 < x + dx < n and -1 < y + dy < n and visit[x+dx][y+dy] < 1:
                    visit[x+dx][y+dy] = 1
                    if arr[x+dx][y+dy] > 0:
                        _stack.append((x+dx, y+dy))
                        l.append((x+dx, y+dy))
        stack = _stack
    return l
k = 0
for i in range(n):
    for j in range(n):
        if visit[i][j] < 1:
            visit[i][j] = 1
            if arr[i][j] > 0:
                group[k] = bfs(i, j)
                k += 1
ans = 9999999
for comb in combinations(group, 2):
    for a in group[comb[0]]:
        for b in group[comb[1]]:
            ans = min(ans, dist(a, b))
print(ans)
"""
10
1 1 1 0 0 0 0 1 1 1
1 1 1 1 0 0 0 0 1 1
1 0 1 1 0 0 0 0 1 1
0 0 1 1 1 0 0 0 0 1
0 0 0 1 0 0 0 0 0 1
0 0 0 0 0 0 0 0 0 1
0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 1 0 0 0 0
0 0 0 0 1 1 1 0 0 0
0 0 0 0 0 0 0 0 0 0
"""