# BOJ - 1915
from sys import stdin
from array import array
read = lambda: stdin.readline().rstrip()
n, m = map(int, read().split())
dp0 = array('H', [0 for _ in range(m+1)])
ans = 0
for i in range(n):
    row = read()
    dp1 = array('H', [0 for _ in range(m+1)])
    for j in range(m):
        if row[j] == '1':
            dp1[j] = min(dp0[j-1], dp0[j], dp1[j-1]) + 1
            ans = max(ans, dp1[j])
        else:
            dp1[j] = 0
    dp0 = dp1[:]
print(ans**2)
'''
4 4
0100
0111
1110
0010

5 5
00011
11101
10111
11111
10010
'''