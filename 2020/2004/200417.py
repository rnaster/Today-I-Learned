# BOJ - 2109
import sys
read = sys.stdin.readline
ans = 0
arr = []
n = int(input())
l = [[*map(int, read().split())] for _ in range(n)]
l.sort(key=lambda x: (-x[0], -x[1]))
for j in range(n):
    a, b = l[j]
    if len(arr) < b:
        arr.extend([0] * (b-len(arr)))
        arr[-1] = a
        ans += a
    elif arr[b-1] == 0:
        arr[b-1] = a
        ans += a
    else:
        i, _ = min(enumerate(arr[:b]), key=lambda x: (x[1], -x[0]))
        if a > arr[i]:
            ans += a - arr[i]
            arr[i] = a
print(ans)
"""
7
20 1
2 1
10 3
100 2
8 2
5 20
50 10
"""