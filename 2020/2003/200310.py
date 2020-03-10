# BOJ - 2194
import sys
read = sys.stdin.readline
n, m, a, b, k = map(int, read().split())
arr = [[0] * m for _ in range(n)]
for _ in range(k):
    x, y = map(int, read().split())
    arr[x-1][y-1] = 1
p, q = map(int, read().split())
r, s = map(int, read().split())
visit = [[0] * m for _ in range(n)]
visit[p-1][q-1] = 1
l = [(p-1, q-1)]
d = ((0, 1), (1, 0), (0, -1), (-1, 0))
def move(x, y, idx):
    dx, dy = d[idx]
    if idx == 0:
        if y+b-1+dy < m: return True
        return False
    if idx == 1:
        if x+a-1+dx < n: return True
        return False
    if idx == 2:
        if -1 < y + dy: return True
        return False
    if -1 < x + dx: return True
    return False
def func(x, y, idx):
    dx, dy = d[idx]
    if idx == 0:
        for i in range(x, x+a):
            if arr[i][y+b-1+dy] > 0:
                return False
        return True
    if idx == 1:
        if sum(arr[x+a-1+dx][y:y+b]) > 0: return False
        return True
    if idx == 2:
        for i in range(x, x+a):
            if arr[i][y+dy] > 0:
                return False
        return True
    if sum(arr[x+dx][y:y+b]) > 0: return False
    return True
ans = 0
while l:
    tmp = []
    for x, y in l:
        if (x, y) == (r-1, s-1): print(ans);exit()
        for idx in range(4):
            dx, dy = d[idx]
            if move(x, y, idx) and visit[x+dx][y+dy] < 1 and func(x, y, idx):
                visit[x+dx][y+dy] = 1
                tmp.append((x+dx, y+dy))
    l = tmp
    ans += 1
print(-1)
"""
5 5 2 2 3
5 5
3 2
3 3
4 1
1 4
"""