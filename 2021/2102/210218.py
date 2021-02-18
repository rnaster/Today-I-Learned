# BOJ - 4307
import sys
read = sys.stdin.readline
for _ in range(int(read())):
    a, b = map(int, read().split())
    ans1, ans2 = 0, 0
    for _ in range(b):
        c = int(read())
        if c > a-c:
            d, e = a-c, c
        else:
            d, e = c, a-c
        ans1 = max(ans1, d)
        ans2 = max(ans2, e)
    print(ans1, ans2)
"""
2
10 3
2
6
7
214 7
11
12
7
13
176
23
191
"""