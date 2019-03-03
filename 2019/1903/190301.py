# BOJ - 5549
from sys import stdin
read = lambda: stdin.readline().rstrip()
n, m = map(int, input().split())
k = int(input())
cache_J = [[0] * (m + 1) for _ in range(n + 1)]
cache_O = [[0] * (m + 1) for _ in range(n + 1)]
cache_I = [[0] * (m + 1) for _ in range(n + 1)]
d = {'J':0, 'O':1, 'I':2}
J_ = [1, 0, 0]
O_ = [0, 1, 0]
I_ = [0, 0, 1]
for i in range(1, n+1):
    tmp = read()
    for j in range(1, m+1):
        if i < 2:
            cache_J[i][j] = cache_J[i][j - 1] + J_[d[tmp[j - 1]]]
            cache_O[i][j] = cache_O[i][j - 1] + O_[d[tmp[j - 1]]]
            cache_I[i][j] = cache_I[i][j - 1] + I_[d[tmp[j - 1]]]
        elif j < 2:
            cache_J[i][j] = cache_J[i - 1][j] + J_[d[tmp[j - 1]]]
            cache_O[i][j] = cache_O[i - 1][j] + O_[d[tmp[j - 1]]]
            cache_I[i][j] = cache_I[i - 1][j] + I_[d[tmp[j - 1]]]
        else:
            cache_J[i][j] = cache_J[i - 1][j] + cache_J[i][j - 1] - cache_J[i - 1][j - 1] + J_[d[tmp[j - 1]]]
            cache_O[i][j] = cache_O[i - 1][j] + cache_O[i][j - 1] - cache_O[i - 1][j - 1] + O_[d[tmp[j - 1]]]
            cache_I[i][j] = cache_I[i - 1][j] + cache_I[i][j - 1] - cache_I[i - 1][j - 1] + I_[d[tmp[j - 1]]]
for _ in range(k):
    a, b, c, d = map(int, read().split())
    j = cache_J[c][d] - cache_J[c][b-1] - cache_J[a-1][d] + cache_J[a-1][b-1]
    o = cache_O[c][d] - cache_O[c][b-1] - cache_O[a-1][d] + cache_O[a-1][b-1]
    i = cache_I[c][d] - cache_I[c][b-1] - cache_I[a-1][d] + cache_I[a-1][b-1]
    print(j, o, i)
"""
4 7
4
JIOJOIJ
IOJOIJO
JOIJOOI
OOJJIJO
3 5 4 7
2 2 3 6
2 2 2 2
1 1 4 7
"""
exit()

# BOJ - 2157
from sys import stdin
read = lambda: stdin.readline().rstrip()
n, m, k = map(int, input().split())
d = {i:set() for i in range(1, n+1)}
arr = [[0]*(n+1) for _ in range(n+1)]
for _ in range(k):
    a, b, c = map(int, read().split())
    if a < b:
        arr[a][b] = max(arr[a][b], c)
        d[a].add(b)
dp = [[0]*(m+1) for _ in range(n+1)]
for j in d[1]:
    dp[j][2] = arr[1][j]
for i in range(2, n):
    for j in range(2, m):
        if dp[i][j] > 0:
            for k in d[i]:
                dp[k][j+1] = max(dp[k][j+1], dp[i][j]+arr[i][k])
print(max(dp[-1]))
"""
3 3 5
1 3 10
1 2 5
2 3 3
1 3 4
3 1 100
"""