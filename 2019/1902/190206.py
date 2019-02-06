# BOJ - 10040
from sys import stdin
read = lambda: stdin.readline().rstrip()
n, m = map(int, read().split())
N = [int(read()) for _ in range(n)]
M = [int(read()) for _ in range(m)]
cache = [-1] * (max(M)+1)
vote = [0] * (n+1)
ans, idx = 0, None
for mm in M:
    if cache[mm] == -1:
        for i in range(1, n+1):
            if N[i-1] <= mm:
                cache[mm] = i
                break
    vote[cache[mm]] += 1
    if ans < vote[cache[mm]]:
        ans = vote[cache[mm]]
        idx = cache[mm]
print(idx)
"""
4 3
5
3
1
4
4
3
2
"""