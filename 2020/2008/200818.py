# BOJ - 1753
import heapq
import sys
read = sys.stdin.readline
v, e = map(int, read().split())
s = int(read())
arr = [{} for _ in range(v)]
for _ in range(e):
    a, b, c = map(int, read().split())
    arr[a-1][b-1] = min(arr[a-1].get(b-1, 11), c)
visit = [True] * v
l = [987654321] * v
l[s-1] = 0
h = [(0, s-1)]
while h:
    _, a = heapq.heappop(h)
    if not visit[a]: continue
    visit[a] = False
    for i, b in arr[a].items():
        if b < 11 and l[i] > l[a] + b:
            l[i] = l[a] + b
            if visit[i]:
                heapq.heappush(h, (l[i], i))
for i in l:
    if i < 987654321: print(i)
    else: print("INF")
"""
5 6
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6
"""