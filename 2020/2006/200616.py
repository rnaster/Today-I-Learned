# BOJ - 1238
import sys, heapq
read = sys.stdin.readline
n, m, x = map(int, read().split())
arr = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, read().split())
    arr[a-1].append((b-1, c))
dist = [[987654321] * n for _ in range(n)]
for i in range(n):
    l = [(0, i)]
    dist[i][i] = 0
    visit = [True] * n
    while l:
        while l:
            _, j = heapq.heappop(l)
            if visit[j]: break
        if visit[j]: visit[j] = False
        else: break
        for a, b in arr[j]:
            if dist[i][a] > dist[i][j] + b:
                dist[i][a] = dist[i][j] + b
                if visit[a]:
                    heapq.heappush(l, (dist[i][a], a))
print(max(dist[i][x] + dist[x][i] for i in range(n)))
"""
4 8 2
1 2 4
1 3 2
1 4 7
2 1 1
2 3 5
3 1 2
3 4 4
4 2 3
"""
exit()

# BOJ - 2467
from bisect import bisect_left as bi
n = int(input())
arr = [*map(int, input().split())]
a, b, c = 0, 1, abs(arr[0] + arr[1])
for i in range(n-1):
    idx = min(bi(arr, arr[i]*-1, i+1, n), n-1)
    t = abs(arr[i] + arr[idx])
    if c > t:
        c = t
        a, b = i, idx
    idx = max(idx-1, i+1)
    t = abs(arr[i] + arr[idx])
    if c > t:
        c = t
        a, b = i, idx
print(arr[a], arr[b])
"""
5
-99 -2 -1 4 98
"""
exit()

# BOJ - 1806
n, m = map(int, input().split())
arr = [*map(int, input().split())]
ans, ans2 = n+1, 0
a, b, s = 0, 0, 0
while a <= b < n:
    if s < m:
        s += arr[b]
        ans2 += 1
        b += 1
    else:
        if s - arr[a] < m:
            ans = min(ans, ans2)
            ans2 -= 1
        else:
            ans2 -= 1
            ans = min(ans, ans2)
        s -= arr[a]
        a += 1
while a < n:
    if s - arr[a] >= m:
        s -= arr[a]
        a += 1
        ans2 -= 1
    else: break
if s >= m: ans = min(ans, ans2)
if ans > n: print(0)
else: print(ans)
"""
10 15
5 1 3 5 10 7 4 9 2 8

10 10
1 1 1 1 1 1 1 1 1 1
"""
exit()

# BOJ - 2638
n, m = map(int, input().split())
arr = [[*map(int, input().split())] for _ in range(n)]
def dist(a, b):
    yield a+1, b
    yield a-1, b
    yield a, b+1
    yield a, b-1
c = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            c.append((i, j))
ans = 0
while c:
    tmp = []
    q = [(0, 0)]
    visit = [[True] * m for _ in range(n)]
    visit[0][0] = False
    while q:
        tmp2 = []
        for x, y in q:
            for xx, yy in dist(x, y):
                if -1 < xx < n and -1 < yy < m and visit[xx][yy]:
                    if arr[xx][yy] == 0:
                        tmp2.append((xx, yy))
                        visit[xx][yy] = False
                    else:
                        arr[xx][yy] += 1
        q = tmp2
    for x, y in c:
        if arr[x][y] > 2:
            arr[x][y] = 0
        else:
            arr[x][y] = 1
            tmp.append((x, y))
    c = tmp
    ans += 1
print(ans)
"""
5 5
0 0 0 0 0
0 0 1 0 0
0 1 0 1 0
0 0 1 0 0
0 0 0 0 0

8 9
0 0 0 0 0 0 0 0 0
0 0 0 1 1 0 0 0 0
0 0 0 1 1 0 1 1 0
0 0 1 1 1 1 1 1 0
0 0 1 1 1 1 1 0 0
0 0 1 1 0 1 1 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0

8 10
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 1 1 0 0 0 0 1 1 0
0 1 0 1 0 1 1 0 1 0
0 1 0 1 0 1 0 0 1 0
0 1 0 1 0 1 1 0 1 0
0 1 1 0 0 0 0 1 1 0
0 0 0 0 0 0 0 0 0 0

8 9
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 1 1 1 0
0 0 0 0 0 1 0 1 0
0 1 1 1 0 1 1 1 0
0 1 1 1 0 0 0 0 0
0 1 1 1 0 0 0 0 0
0 0 0 0 0 0 0 0 0

9 9
0 0 0 0 0 0 0 0 0
0 1 1 1 1 1 1 1 0
0 1 0 0 0 0 0 1 0
0 1 0 0 1 0 0 1 0
0 1 0 1 0 1 0 1 0
0 1 0 0 1 0 0 1 0
0 1 0 0 0 0 0 1 0
0 1 1 1 1 1 1 1 0
0 0 0 0 0 0 0 0 0
"""
exit()
