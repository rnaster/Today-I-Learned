# BOJ - 1939
import sys
read = sys.stdin.readline
n, m = map(int, read().split())
arr = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, read().split())
    arr[a-1].append((b-1, c))
    arr[b-1].append((a-1, c))
a, b = map(int, read().split())
q = [(a-1, 1_000_000_001)]
visit = [True] * n
visit[a-1] = False
ans = 0
while q:
    l = [0] * n
    for x, y in q:
        if x == b-1: ans = max(ans, y)
        for xx, yy in arr[x]:
            if visit[xx] and y >= yy:
                l[xx] = max(l[xx], yy)
    tmp = []
    for i, j in enumerate(l):
        if j > 0 and i != b-1:
            visit[i] = False
            tmp.append((i, j))
    q = tmp
print(ans)
"""
3 3
1 2 2
3 1 3
2 3 2
1 3

5 6
1 2 10
1 3 50
1 4 100
2 5 10
3 5 50
4 5 100
1 5
"""