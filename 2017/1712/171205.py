# BOJ - 11003
from sys import stdin
read = lambda: stdin.readline().rstrip()
n, l = map(int, read().split())
arr = tuple(map(int, read().split()))
if n == l:
    m = min(arr)
    print(*list(m for _ in range(n)))
    quit()
m = min(arr[:l])
idx = arr[:l].index(m)
for i in range(n):
    if idx + l <= i:
        m = min(arr[i:i+l])
        idx = arr[i:i+l].index(m)
    elif arr[i] < m:
        m = arr[i]
        idx = i
    print(m, end=' ')
'''
12 3
1 5 2 3 6 2 3 7 3 5 2 6

1 1 1 2 2 2 2 2 3 3 2 2
'''