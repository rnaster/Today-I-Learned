# BOJ - 3197
n, m = map(int, input().split())
l = []
s = set()
for i in range(n):
    for j, k in enumerate(input()):
        if k == 'X': s.add((i, j))
        elif k == 'L': l.append((i, j))
d = ((0, 1), (0, -1), (1, 0), (-1, 0))
def bfs():
    (a, b), (a1, b1) = l
    q = [(a, b)]
    visit = [[0] * m for _ in range(n)]
    visit[a][b] = 1
    while q:
        tmp = []
        for x, y in q:
            if (x, y) == (a1, b1): return 0
            for dx, dy in d:
                if -1 < x + dx < n \
                        and -1 < y + dy < m \
                        and visit[x+dx][y+dy] < 1 \
                        and (x+dx, y+dy) not in s:
                    visit[x+dx][y+dy] = 1
                    tmp.append((x+dx, y+dy))
        q = tmp
    return 1
ans = 0
while bfs():
    ans += 1
    tmp = set()
    for x, y in s:
        flag = True
        for dx, dy in d:
            if -1 < x + dx < n \
                    and -1 < y + dy < m \
                    and (x+dx, y+dy) not in s:
                flag = False
                break
        if flag:
            tmp.add((x, y))
    s = tmp
print(ans)
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

# BOJ - 1182
import sys
from collections import Counter
sys.setrecursionlimit(100000000)
n, m = map(int, input().split())
arr = [*map(int, input().split())]
l = []
def func(a, b):
    l.extend([b + arr[i] for i in range(a, n)])
    for i in range(a, n):
        func(i+1, b + arr[i])
    return
func(0, 0)
print(Counter(l).get(m, 0))
"""
5 0
-7 -3 -2 5 8

3 0
-3 -2 5
"""