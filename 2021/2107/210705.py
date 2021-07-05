# BOJ - 4991
import sys
from itertools import permutations
read = sys.stdin.readline
def dist(a, b):
    yield a+1,b;yield a-1,b;yield a,b+1;yield a,b-1
def func(arr, n, m):
    visit = [[-1] * m for _ in range(n)]
    s = None
    l = []
    for i in range(n):
        for j in range(m):
            if arr[i][j] == "o":
                s = (i, j)
                l.append((i, j))
                arr[i][j] = "*"
            elif arr[i][j] == "*":
                l.append((i, j))
    d = [[0] * len(l) for _ in range(len(l))]
    def func2(idx):
        coord = l[idx]
        visit[coord[0]][coord[1]] = idx
        q = [coord]
        a = 0
        while q:
            tmp = []
            a += 1
            for x, y in q:
                for xx, yy in dist(x, y):
                    if -1 < xx < n and -1 < yy < m and arr[xx][yy] != "x" and visit[xx][yy] < idx:
                        if arr[xx][yy] == "*":
                            j = l.index((xx, yy))
                            d[idx][j] = d[j][idx] = a
                        visit[xx][yy] = idx
                        tmp.append((xx, yy))
            q = tmp
        return
    for i in range(len(l)):
        func2(i)
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if d[i][j] == 0: return -1
    ans = 987654321
    ll = [i for i in range(len(l))]
    i = l.index(s)
    ll.remove(i)
    for permu in permutations(ll, len(ll)):
        i = l.index(s)
        t = 0
        for p in permu:
            t += d[i][p]
            i = p
        ans = min(ans, t)
    return ans
while 1:
    m, n = map(int, read().split())
    if (n, m) == (0, 0): break
    arr = [[*read().strip()] for _ in range(n)]
    print(func(arr, n, m))
"""
6 5
.....*
.*..*.
...o..
.*....
......
6 5
....o*
.xxxxx
.....x
xxxx.x
*....x
5 5
....*
.*.*.
..o..
..*..
.....
0 0


7 5
.......
.o...*.
.......
.*...*.
.......
15 13
.......x.......
...o...x....*..
.......x.......
.......x.......
.......x.......
...............
xxxxx.....xxxxx
...............
.......x.......
.......x.......
.......x.......
..*....x....*..
.......x.......
10 10
..........
..o.......
..........
..........
..........
.....xxxxx
.....x....
.....x.*..
.....x....
.....x....
6 5
....o*
.xxxxx
.....x
xxxx.x
*....x
0 0
"""