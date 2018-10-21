# BOJ - 1012
from sys import stdin
read = lambda: stdin.readline().rstrip()
for _ in range(int(read())):
    m, n, k = map(int, read().split())
    arr = [[0 for _ in range(m)] for _ in range(n)]
    q = []
    for _ in range(k):
        x, y = map(int, read().split())
        arr[y][x] = 1
        q.append((y, x))
    ans = 0
    for coord in q:
        a, b = coord
        if arr[a][b] != 0:
            tmp_q = [coord]
            while True:
                tmp_tmp_q = []
                for c, d in tmp_q:
                    for dx, dy in ((0, 1), (-1, 0), (0, -1), (1, 0)):
                        if 0 <= c + dx < n and 0 <= d + dy < m:
                            if arr[c+dx][d+dy] == 1:
                                arr[c + dx][d + dy] = 0
                                tmp_tmp_q.append((c+dx, d+dy))
                if not tmp_tmp_q: break
                tmp_q = tmp_tmp_q[:]
            ans += 1
    print(ans)


"""
2
10 8 17
0 0
1 0
1 1
4 2
4 3
4 5
2 4
3 4
7 4
8 4
9 4
7 5
8 5
9 5
7 6
8 6
9 6
10 10 1
5 5
"""