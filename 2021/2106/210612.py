# BOJ - 1774
import sys, math
read = sys.stdin.readline
n, m = map(int, read().split())
arr = [[*map(int, read().split())] for _ in range(n)]
dist = [(math.dist(arr[i], arr[j]), i, j) for i in range(n) for j in range(i+1, n)]
dist.sort(key=lambda x: x[0])
l = [-1] * n
def find(a):
    if l[a] == -1:
        return a
    l[a] = find(l[a])
    return l[a]
for _ in range(m):
    a, b = map(int, read().split())
    aa = find(a-1)
    bb = find(b-1)
    if aa == bb: continue
    l[bb] = aa
ans = 0
cnt = n - m - 1
for d, a, b in dist:
    aa = find(a)
    bb = find(b)
    if aa == bb: continue
    ans += d
    l[bb] = aa
    cnt -= 1
    if cnt == 0:
        break
print("%.2f" % ans)
"""
4 1
1 1
3 1
2 3
4 3
1 4
"""
exit()

# BOJ - 2151
n = int(input())
arr = [input() for _ in range(n)]
inf = 987654321
visit = [[[inf] * n for _ in range(n)] for _ in range(4)]
target = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == "#":
            target.append((i, j))
(a1, b1), (a2, b2) = target
q = [(a1, b1, i, 0) for i in range(4)]
def func(x, y, d):
    if d == 0:
        return x, y-1
    if d == 1:
        return x-1, y
    if d == 2:
        return x, y+1
    return x+1, y
ans = 987654321
while q:
    tmp = []
    for x, y, d, cnt in q:
        if (x, y) == (a2, b2):
            ans = min(ans, cnt)
            continue
        xx, yy = func(x, y, d)
        if -1 < xx < n \
                and -1 < yy < n \
                and arr[xx][yy] != "*" \
                and cnt < visit[d][xx][yy]:
            visit[d][xx][yy] = cnt
            tmp.append((xx, yy, d, cnt))
            if arr[xx][yy] == "!":
                if d == 0 or d == 2:
                    if visit[1][xx][yy]:
                        visit[1][xx][yy] = cnt + 1
                        tmp.append((xx, yy, 1, cnt + 1))
                    if visit[3][xx][yy]:
                        visit[3][xx][yy] = cnt + 1
                        tmp.append((xx, yy, 3, cnt + 1))
                else:
                    if visit[0][xx][yy]:
                        visit[0][xx][yy] = cnt + 1
                        tmp.append((xx, yy, 0, cnt + 1))
                    if visit[2][xx][yy]:
                        visit[2][xx][yy] = cnt + 1
                        tmp.append((xx, yy, 2, cnt + 1))
    q = tmp
print(ans)
"""
5
***#*
*.!.*
*!.!*
*.!.*
*#***

5
!.!.!
.....
.*...
.*...
#.!*#

9
.!*......
..!.!*!.!
#.!*.*.*.
!!.*!.!*.
.*.......
.#......!
.........
.........
!.......!
"""