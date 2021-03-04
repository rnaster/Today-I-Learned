# BOJ - 6087
m, n = map(int, input().split())
arr = [input() for _ in range(n)]
cache = [[[987654321] * 4 for _ in range(m)] for _ in range(n)]
coord = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == "C":
            coord.append((i, j))
cache[coord[0][0]][coord[0][1]] = [0] * 4
q = [(*coord[0], i) for i in range(4)]
def dist(a, b, c):
    if c == 0:
        yield a-1, b, 1, 1
        yield a+1, b, 3, 1
        yield a, b+1, c, 0
    elif c == 1:
        yield a-1, b, c, 0
        yield a, b-1, 2, 1
        yield a, b+1, 0, 1
    elif c == 2:
        yield a, b-1, c, 0
        yield a+1, b, 3, 1
        yield a-1, b, 1, 1
    else:
        yield a+1, b, c, 0
        yield a, b+1, 0, 1
        yield a, b-1, 2, 1
while q:
    tmp = []
    for a, b, c in q:
        if (a, b) == coord[1]: continue
        for aa, bb, cc, dd in dist(a, b, c):
            if -1 < aa < n \
                    and -1 < bb < m \
                    and arr[aa][bb] != "*" \
                    and cache[aa][bb][cc] > cache[a][b][c] + dd:
                cache[aa][bb][cc] = cache[a][b][c] + dd
                tmp.append((aa, bb, cc))
    q = tmp
print(min(cache[coord[1][0]][coord[1][1]]))
"""
7 8
.......
......C
......*
*****.*
....*..
....*..
.C..*..
.......
"""