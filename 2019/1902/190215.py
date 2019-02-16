# BOJ - 11724
from sys import stdin, setrecursionlimit
setrecursionlimit(1000000)
read = lambda: stdin.readline().rstrip()
n, m = map(int, read().split())
grid = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, read().split())
    grid[a][b] = 1
    grid[b][a] = 1
ans = 0
cache = [0] * (n+1)
def func(k):
    global grid, cache
    for i in range(1, n+1):
        if cache[i] == 0 and grid[k][i] == 1:
            cache[i] = 1
            func(i)
for i in range(1, n+1):
    if cache[i] == 0:
        cache[i] = 1
        func(i)
        ans += 1
print(ans)

"""
6 5
1 2
2 5
5 1
3 4
4 6

6 8
1 2
2 5
5 1
3 4
4 6
5 4
2 4
2 3

2 0
"""