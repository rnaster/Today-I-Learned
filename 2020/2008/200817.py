# BOJ - 1477
import heapq
n, m, k = map(int, input().split())
arr = [0] * (n + 1)
a = 0
for i, b in enumerate(sorted(map(int, input().split()))):
    arr[i] = b - a
    a = b
arr[-1] = k - a
l = []
for i, a in enumerate(arr):
    heapq.heappush(l, (-a, (i, 1)))
for _ in range(m):
    _, (b, c) = heapq.heappop(l)
    c += 1
    p, q = divmod(arr[b], c)
    if q: p += 1
    heapq.heappush(l, (-p, (b, c)))
print(-l[0][0])
"""
6 7 800
622 411 201 555 755 82
"""