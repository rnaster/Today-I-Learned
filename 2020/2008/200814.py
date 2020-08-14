# BOJ - 3197
import sys
read = sys.stdin.readline
n, m = map(int, read().split())
arr = [[*read().strip()] for _ in range(n)]
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
    yield a+1, b;yield a-1, b;yield a, b+1;yield a, b-1
visit = [[True] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if arr[i][j] == "L": p.append((i, j))
        if visit[i][j] and arr[i][j] != "X":
            visit[i][j] = False
            flag = True
            for ii, jj in dist(i, j):
                if -1 < ii < n and -1 < jj < m and arr[ii][jj] != "X":
                    if visit[ii][jj]:
                        visit[ii][jj] = False
                        l[ii][jj] = (i, j)
                    elif flag:
                        l[i][j] = (ii, jj)
                        flag = False
ans = 0
while 1:
    tmp = [["."] * m for _ in range(n)]
    q = []
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 'X':
                flag = False
                for ii, jj in dist(i, j):
                    if -1 < ii < n and -1 < jj < m and arr[ii][jj] != "X":
                        flag = True
                        union((i, j), (ii, jj))
                        break
                if flag:
                    q.append((i, j))
                else:
                    tmp[i][j] = "X"
    for i, j in q:
        for ii, jj in dist(i, j):
            if -1 < ii < n and -1 < jj < m and tmp[ii][jj] == ".":
                union((i, j), (ii, jj))
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
XXXXXXXX...XXXX...
..XXXXX...XXX....
....XXXXX.XXXL...
"""
