# BOJ - 3197
import sys
read = sys.stdin.readline
n, m = map(int, read().split())
arr = [[*read()] for _ in range(n)]
p = []
l = [[(-1, -1)] * m for _ in range(n)]
def find(a):
    if l[a[0]][a[1]] == (-1, -1):
        return a
    l[a[0]][a[1]] = find(l[a[0]][a[1]])
    return l[a[0]][a[1]]
def union(a, b):
    aa = find(a)
    bb = find(b)
    if aa == bb: return
    l[bb[0]][bb[1]] = aa
    return
def dist(a, b):
    yield a+1, b
    yield a-1, b
    yield a, b+1
    yield a, b-1
for i in range(n):
    for j in range(m):
        if arr[i][j] in (".", "L"):
            if arr[i][j] == "L": p.append((i, j))
            for ii, jj in dist(i, j):
                if -1 < ii < n \
                        and -1 < jj < m \
                        and arr[ii][jj] != "X" \
                        and arr[ii][jj] != (-1, -1):
                    union((i, j), (ii, jj))
ans = 0
while 1:
    tmp = [["X"] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if arr[i][j] == "X":
                for ii, jj in dist(i, j):
                    if -1 < ii < n \
                            and -1 < jj < m \
                            and arr[ii][jj] in (".", "L"):
                        tmp[i][j] = "."
                        union((ii, jj), (i, j))
            else:
                tmp[i][j] = arr[i][j]
    ans += 1
    arr = tmp
    if find(p[0]) == find(p[1]):
        print(ans)
        break
"""
8 17
...XXXXXX..XX.XXX
....XXXXXXXXX.XXX
...XXXXXXXXXXXX..
..XXXXX.LXXXXXX..
.XXXXXX..XXXXXX..
XXXXXXX...XXXX...
..XXXXX...XXX....
....XXXXX.XXXL...
"""
exit()

# BOJ - 19237
import sys
read = sys.stdin.readline
n, m, k = map(int, read().split())
arr = [[[1001, 1001] for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j, v in enumerate(map(int, read().split())):
        if v < 1: continue
        arr[i][j] = [-v, k]
d = [*map(int, read().split())]
l = [[[*map(int, read().split())] for _ in range(4)] for _ in range(m)]
cnt = m
dd = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for ans in range(1, 1001):
    tmp = [[[1001, 1001] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j][0] > 0: continue
            a = -arr[i][j][0]
            flag = True
            for b in l[a-1][d[a-1]-1]:
                dx, dy = dd[b-1]
                if -1 < i+dx < n and -1 < j+dy < n:
                    if arr[i+dx][j+dy][0] == 1001:
                        d[a-1] = b
                        break
                    elif flag and arr[i+dx][j+dy][0] == a:
                        flag = False
                        d[a-1] = b
            dx, dy = dd[d[a-1]-1]
            if tmp[i+dx][j+dy][0] == 1001:
                tmp[i+dx][j+dy] = [-a, k]
                arr[i][j] = [a, k]
            else:
                if -tmp[i+dx][j+dy][0] > a:
                    tmp[i+dx][j+dy] = [-a, k]
                arr[i][j] = [a, k]
                cnt -= 1
    for i in range(n):
        for j in range(n):
            if tmp[i][j][0] < 0 \
                    or arr[i][j][0] == 1001 \
                    or arr[i][j][1] == 1: continue
            tmp[i][j] = [arr[i][j][0], arr[i][j][1] - 1]
    if cnt == 1: print(ans);exit()
    arr = tmp
print(-1)
"""
5 4 4
0 0 0 0 3
0 2 0 0 0
1 0 0 0 4
0 0 0 0 0
0 0 0 0 0
4 4 3 1
2 3 1 4
4 1 2 3
3 4 2 1
4 3 1 2
2 4 3 1
2 1 3 4
3 4 1 2
4 1 2 3
4 3 2 1
1 4 3 2
1 3 2 4
3 2 1 4
3 4 1 2
3 2 4 1
1 4 2 3
1 4 2 3
"""

"""
import sys
read = sys.stdin.readline
n, m, k = map(int, read().split())
arr = [[[1001, 1001] for _ in range(n)] for _ in range(n)]
pos = [0] * m
for i in range(n):
    for j, v in enumerate(map(int, read().split())):
        if v < 1: continue
        arr[i][j] = [-v, k]
        pos[v-1] = [i, j]
d = [*map(int, read().split())]
l = [[[*map(int, read().split())] for _ in range(4)] for _ in range(m)]
cnt = m
dd = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for ans in range(1, 1001):
    tmp = [[[1001, 1001] for _ in range(n)] for _ in range(n)]
    for v, (i, j) in enumerate(pos, 1):
        if i == j == -1: continue
        e, f = -1, -1
        for c in l[v][d[v]-1]:
            dx, dy = dd[c-1]
            if -1 < i+dx < n and -1 < j+dy < n:
                if arr[i+dx][j+dy][0] == 1001:
                    e = c
                    break
                elif f == -1:
                    f = c
        t = f if e == -1 else e
        dx, dy = dd[t-1]
        if tmp[i+dx][j+dy][0] == 1001:
            tmp[i+dx][j+dy] = [v, k]
            d[v] = t
            pos[v] = [i+dx, j+dy]
        else:
            if tmp[i+dx][j+dy][0] > v:
                pos[tmp[i+dx][j+dy][0]] = [-1, -1]
                tmp[i + dx][j + dy] = [v, k]
                d[v] = t
                pos[v] = [i + dx, j + dy]
            cnt -= 1
    for i in range(n):
        for j in range(n):
            if 1 < arr[i][j][1] < 1001:
                tmp[i][j] = [arr[i][j][0], arr[i][j][1] - 1]
    if cnt == 1: print(ans);exit()
    arr = tmp
    print(*arr, '', sep='\n')
print(-1)
"""