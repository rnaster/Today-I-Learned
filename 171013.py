# BOJ - 2302
from sys import stdin
from array import array
read = lambda: stdin.readline().rstrip()
n, m = int(read()), int(read())
dp = array('L', [0, 1, 2])
for _ in range(n-2):
    dp.append(dp[-1] + dp[-2])
arr = array('B', [0])
for _ in range(m):
    arr.append(int(read()))
arr.append(n+1)
ans = 1
for i in range(m+1):
    num = max(arr[i+1] - arr[i] -1, 1)
    ans *= dp[num]
print(ans)