# BOJ - 2228
n, m = map(int, input().split())
dp = [[-987654321] * (n+1) for _ in range(m+1)]
arr = [int(input())]
cache = [0, arr[0]]
for i in range(1, n):
    arr.append(int(input()))
    cache.append(arr[-1]+cache[-1])
# print(cache)
for i in range(1, n+1):
    dp[1][i] = max(dp[1][i-1], arr[i-1], cache[i])
for i in range(2, m+1):
    for j in range(2*i-1, n+1):
        # for k in range(j-i): print(i, j, k)
        dp[i][j] = max(dp[i][j-1], *[dp[i-1][j-2-k] + cache[j]-cache[j-1-k] for k in range(j-i)])
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