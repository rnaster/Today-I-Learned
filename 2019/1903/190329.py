# BOJ - 5721
import sys
read = lambda: sys.stdin.readline().rstrip()
while True:
    n, m = map(int, read().split())
    if n*m < 1: break
    dp1, dp2 = 0, 0
    c, d = 0, 0
    for i in range(n):
        a, b = 0, 0
        for v in map(int, read().split()):
            a, b = b, max(b, a+v)
        c, d = d, b
        dp1, dp2 = dp2, max(dp2, dp1+d)
    print(dp2)

"""
5 5
1 8 2 1 9
1 7 3 5 2
1 2 10 3 10
8 4 7 9 1
7 1 3 1 6
4 4
10 1 1 10
1 1 1 1
1 1 1 1
10 1 1 10
2 4
9 10 2 7
5 1 1 5
0 0
"""