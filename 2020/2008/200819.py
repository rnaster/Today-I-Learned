# BOJ - 1781
import sys
import heapq
read = sys.stdin.readline
arr = []
s = 0
for a, b in sorted([[*map(int, read().split())] for _ in range(int(read()))],
                   key=lambda x: x[0]):
    if s < a:
        heapq.heappush(arr, b)
        s += 1
    elif arr[0] < b:
        heapq.heappop(arr)
        heapq.heappush(arr, b)
print(sum(arr))
"""
7
1 6
1 7
3 2
3 1
2 4
2 5
6 1
"""