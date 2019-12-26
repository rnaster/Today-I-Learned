# BOJ - 17472
n, m = map(int, input().split())
arr = [[*map(int, input().split())] for _ in range(n)]
a = {i: [] for i in range(1, 7)}
k = 0
cache = [[0] * m for _ in range(n)]
d = ((0, 1), (0, -1), (1, 0), (-1, 0))
for i in range(n):
    for j in range(m):
        if cache[i][j] < 1:
            cache[i][j] = 1
            if arr[i][j] < 1: continue
            k += 1
            a[k].append((i, j))
            q = [(i, j)]
            while q:
                tmp = []
                for x, y in q:
                    for dx, dy in d:
                        if -1 < x + dx < n \
                                and -1 < y + dy < m \
                                and cache[x+dx][y+dy] < 1:
                            cache[x+dx][y+dy] = 1
                            if arr[x+dx][y+dy] > 0:
                                tmp.append((x+dx, y+dy))
                                a[k].append((x+dx, y+dy))
                q = tmp
b = 0
for k, v in a.items():
    b += len(v) > 0
    for x, y in v:
        arr[x][y] = k
dist = [[987654321] * b for _ in range(b)]
for k, v in a.items():
    for x, y in v:
        for dx, dy in d:
            x_, y_ = x + dx, y + dy
            dd = 0
            while -1 < x_ < n and -1 < y_ < m and arr[x_][y_] == 0:
                dd += 1
                x_ += dx
                y_ += dy
            if -1 < x_ < n and -1 < y_ < m and dd > 1:
                dist[k-1][arr[x_][y_]-1] = dist[arr[x_][y_]-1][k-1] = min(dist[arr[x_][y_]-1][k-1], dd)
cache = [-1] * (1 << b)
def func(visit, visit_n):
    if visit_n == b:
        cache[visit] = 0
        return cache[visit]
    else:
        temp = 987654321
        for i in range(b):
            if not visit & 1 << i:
                for j in range(b):
                    if visit & 1 << j:
                        val = cache[visit|1<<i] if cache[visit|1<<i] != -1 else func(visit | 1 << i, visit_n+1)
                        temp = min(temp, val + dist[j][i])
        cache[visit] = temp
        return cache[visit]
func(1, 1)
if cache[1] > 123456789:
    print(-1)
else:
    print(cache[1])
"""
7 8
0 0 0 0 0 0 1 1
1 1 0 0 0 0 1 1
1 1 0 0 0 0 0 0
1 1 0 0 0 1 1 0
0 0 0 0 0 1 1 0
0 0 0 0 0 0 0 0
1 1 1 1 1 1 1 1

7 7
1 1 1 0 1 1 1
1 1 1 0 1 1 1
1 1 1 0 1 1 1
0 0 0 0 0 0 0
1 1 1 0 1 1 1
1 1 1 0 1 1 1
1 1 1 0 1 1 1
"""