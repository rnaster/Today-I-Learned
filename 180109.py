# BOJ - 7576
from sys import stdin
from array import array
read = lambda: stdin.readline().rstrip()
n, m = map(int, read().split())
dp = array('b', [0 for _ in range(n * m)])
def write(x, y, v):
    global dp, n, m
    dp[n * x + y] = v
def _read(x, y):
    global dp, n, m
    return dp[n * x + y]
q = []
neg = 0
for i in range(m):
    tp = map(int, read().split())
    ix = 0
    for j in tp:
        if j != 0:
            write(i, ix, j)
            if j == 1: q.append((i, ix))
            else: neg += 1
        ix += 1
ans = 0
while True:
    tmp = []
    while q:
        x, y = q.pop()
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            if 0 <= x + dx < m and 0 <= y + dy < n:
                if _read(x+dx, y+dy) == 0:
                    tmp.append((x+dx, y+dy))
                    write(x+dx, y+dy, 1)
    if tmp == []: break
    q = tmp[:]
    del tmp
    ans += 1
if sum(dp) + neg*2 == n*m: print(ans)
else: print(-1)

'''
6 4
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 -1 -1
0 0 0 0 -1 1

2 5
-1 1
0 0
0 0
0 0
0 0
'''