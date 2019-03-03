# BOJ - 3474
from sys import stdin
read = lambda: stdin.readline().rstrip()
for _ in range(int(read())):
    n = int(read())
    ans = n // 5
    if ans < 1: print(ans);continue
    a = 25
    while True:
        q = n // a
        if q > 0: ans += q; a *= 5;
        else: break
    print(ans)
"""
6
3
60
100
1024
23456
8735373
"""