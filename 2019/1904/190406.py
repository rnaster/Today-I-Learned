# BOJ - 3806
import sys
read = lambda: sys.stdin.readline().rstrip()
for i in range(1, int(read())+1):
    ans = 0
    d1, d2 = {'0':0, '1':0, '?':0}, {'0':0, '1':0,'?':0}
    neq = 0
    for ar1, ar2 in zip(read(), read()):
        if ar1 != ar2:
            d1[ar1] += 1
            d2[ar2] += 1

"""
4
01??00
001010
01
10
110001
000000
?11000
100???

"""