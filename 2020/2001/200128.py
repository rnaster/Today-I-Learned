# BOJ - 2572
import sys
sys.setrecursionlimit(10000000)
read = sys.stdin.readline
n = int(read())
l = read().split()
m, k = map(int, read().split())
d = {i: [] for i in range(1, m+1)}
for _ in range(k):
    a, b, c = read().split()
    a, b = int(a), int(b)
    d[a].append((b, c))
    d[b].append((a, c))
dp = [[-1] * (m+1) for _ in range(n+1)]
def func(p, q):
    if p == n:
        dp[p][q] = 0
        return dp[p][q]
    val = 0
    for a, b in d[q]:
        tmp = dp[p+1][a] if dp[p+1][a] > -1 else func(p+1, a)
        if b == l[p]: tmp += 10
        val = max(val, tmp)
    dp[p][q] = val
    return dp[p][q]
print(func(0, 1))
"""
5 
R G R B G 
4 5 
1 2 R 
1 3 G 
2 3 G 
1 4 R 
4 3 B
"""