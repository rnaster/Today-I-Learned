# BOJ - 3649
import sys
from bisect import bisect_left as bi
read = sys.stdin.readline
while 1:
    try:
        a = int(read()) * 10000000
        n = int(read())
        l = [0] * n
        for i in range(n):
            l[i] = int(read())
    except:
        break
    l.sort()
    flag = True
    for i in range(n):
        idx = min(n-1, bi(l, a-l[i], i+1, n))
        if l[i] + l[idx] == a:
            print('yes', l[i], l[idx])
            flag = False
            break
    if flag:
        print('danger')
"""
1
4
9999998
1
2
9999999

1
3
4000000
5000000
7000000
"""