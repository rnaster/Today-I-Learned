# BOJ - 2624
from sys import stdin
from array import array
read = lambda: stdin.readline().rstrip()
t = int(read())
dp = array('L', [1] + [0 for _ in range(t)])
cache = {0}
for _ in range(int(read())):
    p, n = map(int, read().split())
    tmp = dp[:]
    tmp_cache = cache.copy()
    for c in cache:
        for i in range(1, n+1):
            if c + p * i <= t:
                tmp[c + p * i] += dp[c]
                tmp_cache.add(c + p * i)
            else:
                break
    cache.update(tmp_cache)
    dp = tmp[:]
print(dp[-1])
"""
20
3
5 3
10 2
1 5
"""