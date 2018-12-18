# BOJ - 4781
import sys
read = sys.stdin.readline
while True:
    n,m = map(float,read().split())
    if n == 0: exit()
    m = int(100*m)
    dp = [0]*(m+1)
    for _ in range(int(n)):
        c,p = map(float,read().split())
        c,p = int(c), int(100*p)
        for i in range(p,m+1):
            dp[i] = max(dp[i],dp[i-p]+c)
    print(dp[m])
"""
2 8.00
700 7.00
199 2.00
3 8.00
700 7.00
299 3.00
499 5.00
3 11.11
321 1.45
55 0.56
209 0.74
0 0.00
"""