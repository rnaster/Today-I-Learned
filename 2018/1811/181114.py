# BOJ - 5567
from sys import stdin
read = lambda: stdin.readline().rstrip()
n = int(read())
d = {i: set() for i in range(1, n+1)}
for _ in range(int(read())):
    a, b = map(int, read().split())
    d[a].add(b)
    d[b].add(a)
ans = d[1].copy()
for i in d[1]:
    ans.update(d[i])
ans.remove(1)
print(len(ans))
"""
6
5
1 2
1 3
6 5
2 3
4 5
"""