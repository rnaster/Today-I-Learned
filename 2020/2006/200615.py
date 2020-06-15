# BOJ - 1916
import sys, heapq
read = sys.stdin.readline
n = int(read())
m = int(read())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, read().split())
    arr[a].append((b, c))
x, y = map(int, read().split())
dist = [987654321] * (n+1)
q = [(0, x)]
dist[x] = 0
visit = [True] * (n+1)
while q:
    xx = 0
    while q:
        _, xx = heapq.heappop(q)
        if visit[xx]: break
    if visit[xx]: visit[xx] = False
    else: break
    for a, b in arr[xx]:
        if dist[a] > dist[xx] + b:
            dist[a] = dist[xx] + b
            if visit[a]:
                heapq.heappush(q, (dist[a], a))
print(dist[y])
"""
5
8
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
1 5

5
3
1 2 2
1 3 5
2 3 1
1 3
"""