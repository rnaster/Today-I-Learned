# BOJ - 2515
import sys
from bisect import bisect_left
read = sys.stdin.readline
n, s = map(int, read().split())
arr = [tuple(map(int, read().split())) for _ in range(n)]
arr = sorted(arr, key=lambda x:x[0])
hh = [arr[i][0] for i in range(n)]
dp = [0] * n#;dp[0] = arr[0][1]
for i in range(n):
    if hh[i] < s:
        dp[i] = max(dp[i-1], arr[i][1])
    else:
        idx = bisect_left(hh, hh[i]-s)
        if hh[idx] != hh[i]-s: idx -= 1
        dp[i] = max(dp[i-1], dp[idx]+arr[i][1])
print(dp)
print(*arr, sep='\n')
"""
11 4
15 80
8 300
8 230
10 100
10 110
17 200
17 210
20 75
26 80
15 90
26 90

2 2
3 4
1 9

5 7
4 5
2 5
5 7
10 3
6 1

5 6
5 8
1 2
6 4
7 8
9 7
"""