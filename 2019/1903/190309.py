# BOJ - 16234
n, l, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visit = [[-1]*n for _ in range(n)]
ans = 0
while True:
    update = 0
    for i in range(n):
        for j in range(n):
            if visit[i][j] < ans:
                visit[i][j] += 1
                q, _q, q_size = [(i, j)], [(i, j)], 1
                while True:
                    temp = []
                    for x, y in _q:
                        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                            if -1 < x + dx < n and -1 < y + dy < n:
                                _x, _y = x + dx, y + dy
                                if visit[_x][_y] < ans and l <= abs(arr[x][y] - arr[_x][_y]) <= r:
                                    visit[_x][_y] += 1
                                    temp.append((_x, _y))
                                    q.append((_x, _y))
                                    q_size += 1
                    if temp == []: break
                    _q = temp
                if q_size > 1:
                    update += 1
                    val = 0
                    for x, y in q:
                        val += arr[x][y]
                    val = val // q_size
                    for x, y in q:
                        arr[x][y] = val
    if update > 0:
        ans += 1
    else: break
print(ans)
"""
2 20 50
50 30
20 40
# 1

2 40 50
50 30
20 40
# 0

2 20 50
50 30
30 40
# 1

3 5 10
10 15 20
20 30 25
40 22 10
# 2

4 10 50
10 100 20 90
80 100 60 70
70 20 30 40
50 20 100 10
# 3
"""