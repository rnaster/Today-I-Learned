# BOJ - 7575
import sys
read = sys.stdin.readline
n, k = map(int, read().split())
cache = set()
m = int(read())
arr = [*map(int, read().split())]
for i in range(m-k+1):
    tmp = tuple(arr[i:i+k])
    cache.update({tmp, tmp[::-1]})
for _ in range(n-1):
    m = int(read())
    arr = [*map(int, read().split())]
    tmp = set()
    for i in range(m-k+1):
        arr1 = tuple(arr[i:i+k])
        arr2 = arr1[::-1]
        tmp.update({arr1, arr2})
    cache &= tmp
    if len(cache) < 1:
        print('NO')
        exit()
print('YES')
"""
3 4
13
10 8 23 93 21 42 52 22 13 1 2 3 4
11
1 3 8 9 21 42 52 22 13 41 42
10
9 21 42 52 13 22 52 42 12 21
"""