# BOJ - 6359
def foo():
    from sys import stdin
    from array import array
    read = lambda: stdin.readline().rstrip()
    lock = lambda x: 1-x
    for _ in range(int(read())):
        n = int(read())
        dp = array('B', [0 for _ in range(n)])
        s = 0
        for i in range(1, n):
            for j in range(i, n, i+1):
                dp[j] = lock(dp[j])
            s += dp[i]
        print(n - s)

from sys import stdin
read = lambda: stdin.readline().rstrip()
n, m = map(int, read().split())
arr= []
for _ in range(n):
    arr.append(tuple(map(int, read().split())))
arr = tuple(arr)
dp = [[0 for _ in range(m)] for _ in range(n)]
dp[0][0] = 1
for i in range(n):
    for j in range(m):
        for idx in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            if 0<=i+idx[0]<n and 0<=j+idx[1]<m:
                if (i+idx[0], j+idx[1]) == (3, 3): print(dp[i+idx[0]][j+idx[1]], '*', i, j, '**',dp[i][j])
                if arr[i+idx[0]][j+idx[1]] > arr[i][j]:
                    if dp[i][j]:
                        dp[i][j] = max(dp[i+idx[0]][j+idx[1]], dp[i][j])
                if arr[i+idx[0]][j+idx[1]] < arr[i][j]:
                    dp[i+idx[0]][j+idx[1]] += dp[i][j]
    print(i,j,dp)
# print(dp)