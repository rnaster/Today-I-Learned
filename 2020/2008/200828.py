# BOJ - 16197
from operator import xor
n, m = map(int, input().split())
arr = [[*input()] for _ in range(n)]
p = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == "o":
            p.append((i, j))
            arr[i][j] = "."
visit = [[[[True] * m for _ in range(n)]
          for _ in range(m)] for _ in range(n)]
q = [p[0] + p[1]]
def dist(a, b):
    yield a+1, b;yield a-1, b;yield a, b+1;yield a, b-1
ans = 1
while q and ans < 11:
    tmp = []
    for x1, y1, x2, y2 in q:
        for (xx1, yy1), (xx2, yy2) in zip(dist(x1, y1), dist(x2, y2)):
            flag1 = True
            flag2 = True
            if not (-1 < xx1 < n and -1 < yy1 < m):
                flag1 = False
            if not (-1 < xx2 < n and -1 < yy2 < m):
                flag2 = False
            if xor(flag1, flag2):
                print(ans)
                exit()
            elif flag1 and flag2 and visit[xx1][yy1][xx2][yy2]:
                visit[xx1][yy1][xx2][yy2] = False
                if arr[xx1][yy1] == "." and arr[xx2][yy2] == ".":
                    tmp.append((xx1, yy1, xx2, yy2))
                elif arr[xx1][yy1] == ".":
                    visit[xx1][yy1][x2][y2] = False
                    tmp.append((xx1, yy1, x2, y2))
                elif arr[xx2][yy2] == ".":
                    visit[x1][y1][xx2][yy2] = False
                    tmp.append((x1, y1, xx2, yy2))
    q = tmp
    ans += 1
print(-1)
"""
5 3
###
.o.
###
.o.
###

5 3
###
.o.
#.#
.o.
###
"""