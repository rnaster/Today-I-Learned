# BOJ - 3055
n, m = map(int, input().split())
arr = [input() for _ in range(n)]
visit = [[[0] * m for _ in range(n)] for _ in range(2)]
a, b = None, None
q = []
water, qq = set(), []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'D':
            a, b = i, j
        elif arr[i][j] == 'S':
            q.append((i, j))
        elif arr[i][j] == '*':
            water.add((i, j))
            qq.append((i, j))
d = ((0, 1), (0, -1), (1, 0), (-1, 0))
visit[1][q[0][0]][q[0][1]] = 1
for x, y in qq:
    visit[0][x][y] = 1
ans = 0
while q:
    tmptmp = []
    for x, y in qq:
        for dx, dy in d:
            if -1 < x + dx < n \
                    and -1 < y + dy < m \
                    and visit[0][x + dx][y + dy] < 1:
                visit[0][x + dx][y + dy] = 1
                if arr[x + dx][y + dy] not in ['X', 'D']:
                    water.add((x + dx, y + dy))
                    tmptmp.append((x + dx, y + dy))
    qq = tmptmp
    tmp = []
    for x, y in q:
        if (x, y) == (a, b): print(ans);exit()
        for dx, dy in d:
            if -1 < x + dx < n \
                    and -1 < y + dy < m \
                    and visit[1][x + dx][y + dy] < 1:
                visit[1][x + dx][y + dy] = 1
                if (x+dx, y+dy) not in water \
                        and arr[x + dx][y + dy] != 'X':
                    tmp.append((x + dx, y + dy))
    q = tmp
    ans += 1
print('KAKTUS')
"""
3 6
D...*.
.X.X..
....S.
"""
