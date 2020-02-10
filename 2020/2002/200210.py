# BOJ -1600
k = int(input())
w, h = map(int, input().split())
arr = [[*map(int, input().split())] for _ in range(h)]
visit = [[[0] * w for _ in range(h)] for _ in range(k+1)]
for i in range(k+1):
    visit[i][0][0] = 1
q = [(0, 0, 0)]
d = ((1, 0), (-1, 0), (0, 1), (0, -1))
dd = ((-2, 1), (-1, 2), (1, 2), (2, 1),
      (2, -1), (1, -2), (-1, -2), (-2, -1))
ans = 0
while q:
    tmp = []
    for a, x, y in q:
        if (x, y) == (h-1, w-1): print(ans); exit()
        for dx, dy in d:
            if -1 < x + dx < h \
                    and -1 < y + dy < w \
                    and arr[x+dx][y+dy] < 1 \
                    and visit[a][x+dx][y+dy] < 1:
                visit[a][x+dx][y+dy] = 1
                tmp.append((a, x+dx, y+dy))
        if a < k:
            for dx, dy in dd:
                if -1 < x + dx < h \
                        and -1 < y + dy < w \
                        and arr[x + dx][y + dy] < 1 \
                        and visit[a+1][x + dx][y + dy] < 1:
                    visit[a+1][x + dx][y + dy] = 1
                    tmp.append((a+1, x+dx, y+dy))
    q = tmp
    ans += 1
print(-1)
"""
1
4 4
0 0 0 0
1 0 0 0
0 0 1 0
0 1 0 0

1
3 4
0 0 0
0 0 0
0 1 1
0 1 0

1
5 5
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 1 1
0 0 0 1 0
"""
exit()

# BOJ - 1987
n, m = map(int, input().split())
arr = [[*map(ord, input())] for _ in range(n)]
visit = [[0] * m for _ in range(n)]
d = ((0, 1), (0, -1), (1, 0), (-1, 0))
l = [0] * 26
def func(x, y):
    tmp = 1
    l[arr[x][y] - 65] = 1
    for dx, dy in d:
        if -1 < x + dx < n \
                and -1 < y + dy < m \
                and visit[x+dx][y+dy] < 1 and l[arr[x + dx][y + dy] - 65] < 1:
            visit[x+dx][y+dy] = 1
            tmp = max(tmp, func(x+dx, y+dy)+1)
            visit[x + dx][y + dy] = 0
            l[arr[x + dx][y + dy] - 65] = 0
    return tmp
print(func(0, 0))
"""
2 4
CAAB
ADCB
"""