# BOJ - 2573
import sys
read = sys.stdin.readline
n, m = map(int, read().split())
arr = [[*map(int, read().split())] for _ in range(n)]
d = ((0, 1), (0, -1), (1, 0), (-1, 0))
ans = 0
while True:
    ice = {}
    visit = [[0] * m for _ in range(n)]
    zone = 0
    for x in range(n):
        for y in range(m):
            if visit[x][y] < 1:
                visit[x][y] = 1
                if arr[x][y] > 0:
                    q = [(x, y)]
                    while q:
                        tmp = []
                        for a, b in q:
                            ice[(a, b)] = arr[a][b]
                            for dx, dy in d:
                                if -1 < a + dx < n and -1 < b + dy < m:
                                    if arr[a+dx][b+dy] < 1:
                                        ice[(a, b)] = max(0, ice[(a, b)] - 1)
                                    elif visit[a + dx][b + dy] < 1:
                                        visit[a + dx][b + dy] = 1
                                        tmp.append((a + dx, b + dy))
                        q = tmp
                    zone += 1
    if zone > 1:
        print(ans)
        break
    if ice:
        for k, v in ice.items():
            a, b = k
            arr[a][b] = v
        ans += 1
    else:
        print(0)
        break
"""
5 7
0 0 0 0 0 0 0
0 2 4 5 3 0 0
0 3 0 2 5 2 0
0 7 6 2 4 0 0
0 0 0 0 0 0 0
"""