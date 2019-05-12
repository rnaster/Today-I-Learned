# BOJ - 2159
import sys
sys.setrecursionlimit(10000000)
read = lambda: sys.stdin.readline().rstrip()
n = int(read())
arr = [tuple(map(int, read().split())) for _ in range(n+1)]
dp = [[-1] * (n+1) for _ in range(5)]
d = {0:(0, 0),1:(1, 0),2:(-1, 0),3:(0, 1),4:(0, -1)}
def dist(a, b, c, d):
    return abs(a-c) + abs(b-d)
def func(a, b):
    if b == n:
        dp[a][b] = 0
        return dp[a][b]
    temp = 987654321987
    x, y = arr[b]
    dx, dy = d[a]
    xx, yy = arr[b+1]
    for i in range(5):
        ddx, ddy = d[i]
        t = dp[i][b+1] if dp[i][b+1] != -1 else func(i, b+1)
        temp = min(temp, t + dist(x+dx, y+dy, xx+ddx, yy+ddy))
    dp[a][b] = temp
    return dp[a][b]
print(func(0, 0))
print(*dp, sep='\n')
"""
3
2 2
3 6
6 7
7 3
"""
sys.exit()

# BOJ - 2342
import sys
sys.setrecursionlimit(1000000)
arr = [*map(int, input().split())]
dp = [[[-1] * len(arr) for _ in range(5)] for _ in range(5)]
d = {(0,1):2,(0,2):2,(0,3):2,(0,4):2,
     (1,0):2,(2,0):2,(3,0):2,(4,0):2,
     (1,2):3,(1,4):3,
     (2,1):3,(2,3):3,
     (3,2):3,(3,4):3,
     (4,3):3,(4,1):3,
     (1,3):4,(3,1):4,
     (2,4):4,(4,2):4}
def func(a, b, c):
    if arr[c] == 0:
        dp[a][b][c] = 0
        return dp[a][b][c]
    if a == arr[c] or b == arr[c]:
        dp[a][b][c] = dp[a][b][c+1] + 1 if dp[a][b][c+1] != -1 else func(a, b, c+1) + 1
    else:
        t1 = dp[a][arr[c]][c+1] if dp[a][arr[c]][c+1] != -1 else func(a, arr[c], c+1)
        t2 = dp[arr[c]][b][c+1] if dp[arr[c]][b][c+1] != -1 else func(arr[c], b, c+1)
        dp[a][b][c] = min(t1+d[(b, arr[c])], t2+d[(a, arr[c])])
    return dp[a][b][c]
print(func(0, 0, 0))
"""
1 2 2 4 0
"""