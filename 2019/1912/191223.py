# BOJ - 17070
n = int(input())
arr = [[*map(int, input().split())] for _ in range(n)]
dp = [[[-1] * n for _ in range(n)] for _ in range(3)]
dp[2][0][1] = 1
if arr[-1][-1] == 1: print(0);exit()
def func(a, b, c):
    dp[a][b][c] = 0
    if a == 0:
        if 0 < b and 0 < c \
                and arr[b-1][c-1] + arr[b-1][c] + arr[b][c-1] < 1:
            dp[a][b][c] += sum(dp[i][b-1][c-1]
                               if dp[i][b-1][c-1] > -1 else func(i, b-1, c-1)
                               for i in [0, 1, 2])
    elif a == 1:
        if 0 < b and arr[b-1][c] < 1:
            dp[a][b][c] += sum(dp[i][b - 1][c]
                               if dp[i][b - 1][c] > -1 else func(i, b - 1, c)
                               for i in [0, 1])
    else:
        if 0 < c and arr[b][c-1] < 1:
            dp[a][b][c] += sum(dp[i][b][c - 1]
                               if dp[i][b][c - 1] > -1 else func(i, b, c - 1)
                               for i in [0, 2])
    return dp[a][b][c]
print(sum(func(i, n-1, n-1) for i in range(3)))
"""
4
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0

6
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0

5
0 0 1 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0

6
0 0 0 1 0 0
0 0 0 1 0 0
0 0 0 1 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 1 0 0 0

"""