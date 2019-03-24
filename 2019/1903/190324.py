# BOJ - 5032
e, f, c = map(int, input().split())
a = e+f
ans = 0
while True:
    if a < c: print(ans);break
    ans += a // c
    a = a // c + a % c
"""
9 0 3
"""
exit()

# BOJ - 2228
n, m = map(int, input().split())
dp = [[-1] * (n+1) for _ in range(m+1)]
cache = [[0]*(n+1) for _ in range(n+1)]
arr = []
for i in range(1, n+1):
    a = int(input())
    arr.append(a)
    cache[1][i] = cache[1][i-1] + a
for i in range(2, n+1):
    for j in range(i, n+1):
        cache[i][j] = cache[i-1][j] - cache[i-1][i-1]
# print(*cache, '', sep='\n')
for i in range(1, n+1):
    dp[1][i] = max(dp[1][i-1], arr[i-1], cache[1][i])
for i in range(2, m+1):
    for j in range(2*i-1, n+1):
        dp[i][j] = max(dp[i][j-1], *[cache[j-l][j] + dp[i-1][j-2-k] for k in range(j-2*i+2) for l in range(k+1)])
print(dp[-1][-1])
print(*dp, sep='\n')
"""
6 2
-1
3
1
2
4
-1

10 3
1
2
3
4
5
6
7
8
9
10

10 3
-1
-2
-3
-4
-5
-6
-7
-8
-9
-10

"""