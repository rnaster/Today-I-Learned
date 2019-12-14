# BOJ - 2468
n = int(input())
arr = [[*map(int, input().split())] for _ in range(n)]
cache = None
d = ((0, 1), (0, -1), (1, 0), (-1, 0))
def bfs(q):
    global cache
    while q:
        tmp = []
        for x, y in q:
            for dx, dy in d:
                if -1 < x + dx < n and -1 < y + dy < n and cache[x+dx][y+dy] < 1:
                    cache[x+dx][y+dy] = 1
                    tmp.append((x+dx, y+dy))
        q = tmp
    return True
ans = 1
rain = set()
k = 1
while True:
    tmp = 0
    cache = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if (i, j) not in rain and arr[i][j] <= k:
                rain.add((i, j))
    for (a, b) in rain:
        cache[a][b] = 1
    for i in range(n):
        for j in range(n):
            if cache[i][j] == 0:
                cache[i][j] = 1
                tmp += bfs([(i, j)])
    if tmp < 1:
        print(ans)
        break
    ans = max(ans, tmp)
    k += 1
"""
5
6 8 2 6 2
3 2 3 4 6
6 7 3 3 2
7 2 5 3 6
8 9 5 2 7
"""