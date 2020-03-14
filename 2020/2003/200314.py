# BOJ - 2758
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
l = []
n_, m_ = 0, 0
for _ in range(int(input())):
    n, m = map(int, input().split())
    l.append((n, m))
    n_, m_ = max(n_, n), max(m_, m)
dp = [[-1] * (m_ + 1) for _ in range(n_ + 1)]
def func(a, b):
    if a == 1:
        dp[a][b] = 1
        return dp[a][b]
    i = b * 2
    val = 0
    while i * 2 ** (a-2) <= m:
        val += dp[a-1][i] if dp[a-1][i] > -1 else func(a-1, i)
        i += 1
    dp[a][b] = val
    return dp[a][b]
for n, m in l:
    ans = 0
    i = 1
    while i * 2 ** max(0, n-2) <= m:
        ans += func(n, i)
        i += 1
    print(ans)
print(*dp, '', sep='\n')
"""
2
4 10
3 10

4
1 10
2 10
3 10
4 10
"""
exit()

# BOJ - 1500
a, b = map(int, input().split())
p, q = divmod(a, b)
print(p, q)
if q:
    print((p + 1) ** q * p ** (b - q))
else:
    print(p ** b)
"""
10 3
"""
exit()

# BOJ - 1105
a, b = input().split()
ans = 0
for i, j in zip(a.zfill(len(b)), b):
    if i == j:
        if i == '8': ans += 1
    else:
        print(ans)
        exit()
print(ans)
"""
8808 8880
"""
