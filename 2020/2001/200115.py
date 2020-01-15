# BOJ - 1926
n, m = map(int, input().split())
arr = [[*map(int, input().split())] for _ in range(n)]
d = ((0, 1), (0, -1), (1, 0), (-1, 0))
visit = [[0] * m for _ in range(n)]
def bfs(a, b):
    q = [(a, b)]
    visit[a][b] = 1
    area = 1
    while q:
        tmp = []
        for x, y in q:
            for dx, dy in d:
                if -1 < x + dx < n \
                        and -1 < y + dy < m \
                        and visit[x+dx][y+dy] < 1 \
                        and arr[x+dx][y+dy] > 0:
                    visit[x+dx][y+dy] = 1
                    tmp.append((x+dx, y+dy))
                    area += 1
        q = tmp
    return area
cnt = 0
ans = 0
for i in range(n):
    for j in range(m):
        if visit[i][j] < 1 and arr[i][j] > 0:
            ans = max(ans, bfs(i, j))
            cnt += 1
print(cnt, ans, sep='\n')
"""
6 5
1 1 0 1 1
0 1 1 0 0
0 0 0 0 0
1 0 1 1 1
0 0 1 1 1
0 0 1 1 1
"""
