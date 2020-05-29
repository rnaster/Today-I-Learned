# BOj - 1689
import sys
import heapq
read = sys.stdin.readline
n = int(input())
arr = sorted([*map(int, read().split())] for _ in range(n))
l = [arr[0][1]]
ans = 1
for i in range(1, n):
    a, b = arr[i]
    heapq.heappush(l, b)
    while a >= l[0]:
        heapq.heappop(l)
    ans = max(ans, len(l))
print(ans)
"""
11
1 2
3 6
7 8
10 11
13 16
0 5
5 6
2 5
6 10
9 14
12 15
"""
exit()

# BOJ - 1276
n = int(input())
arr = sorted([[*map(int, input().split())] for _ in range(n)],
             key=lambda x: x[0])
ans = 0
for i, [a, b, c] in enumerate(arr):
    x, y = True, True
    ans += 2 * a
    j = i-1
    while x | y and j > -1:
        d, e, f = arr[j]
        if x and e <= b < f:
            x = False
            ans -= d
        if y and e < c <= f:
            y = False
            ans -= d
        j -= 1
print(ans)
"""
3
1 5 10
3 1 5
5 3 7
"""