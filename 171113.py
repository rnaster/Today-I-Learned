# BOJ - 1005
from sys import stdin
from array import array
read = lambda: stdin.readline().rstrip()
for _ in range(int(read())):
    n, k = map(int, read().split())
    c = tuple(map(int, read().split()))
    lst = [0] + [[] for _ in range(n)]
    indeg = array('h', [-1] + [0 for _ in range(n)])
    for _ in range(k):
        x, y = map(int, read().split())
        lst[x].append(y)
        indeg[y] += 1
    w = int(read())
    # res = array('H', [])
    dp = array('L', [0 for _ in range(n+1)])
    while True:
        try:
            idx = indeg.index(0)
        except: break
        indeg[idx] = -1
        dp[idx] = max(dp[idx], c[idx-1])
        for j in lst[idx]:
            indeg[j] -= 1
            dp[j] = max(dp[j], c[j-1] + dp[idx])
    print(dp[w])

'''
1
6 6
1 1 1 1 1 1
4 1
2 4
6 2
1 3
5 3
5 1
3

2
4 4
10 1 100 10
1 2
1 3
2 4
3 4
4
8 8
10 20 1 5 8 7 1 43
1 2
1 3
2 4
2 5
3 6
5 7
6 7
7 8
7
'''