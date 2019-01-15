# BOJ - 2783
a, b = map(int, input().split())
ans = min(100001, a / b * 1000)
for _ in range(int(input())):
    a, b = map(int, input().split())
    ans = min(ans, a / b * 1000)
print(ans)
"""
5 100
3
4 100
3 100
7 100
"""
exit()

# BOJ - 3067
from sys import stdin
read = lambda: stdin.readline().rstrip()
for _ in range(int(read())):
    n = int(read())
    c = tuple(map(int, read().split()))
    m = int(read())
    dp = [0] * (m+1); dp[0] = 1
    for cc in c:
        for i in range(cc, m+1):
            dp[i] += dp[i-cc]
    print(dp[-1])

"""
3
2
1 2
1000
3
1 5 10
100
2
5 7
22
"""
exit()

# BOJ - 1551
n, k = map(int, input().split())
tp = tuple(map(int, input().split(',')))
if k == 0: print(*tp, sep=',');exit()
sign = (-1)**k
cache = [sign]
a = 1
for i in range(1, k+1):
    sign *= -1
    a *= k - i + 1
    a //= i
    cache.append(a*sign)
ans = []
for i in range(n-k):
    tptp = tp[i:i+k+1]
    t = 0
    for j in range(k+1):
        t += tptp[j] * cache[j]
    ans.append(t)
print(*ans, sep=',')
"""
5 4
5,6,3,9,-1
"""