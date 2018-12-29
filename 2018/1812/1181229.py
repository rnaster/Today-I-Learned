# BOJ - 1188
import math
n, m = map(int, input().split())
g = math.gcd(n, m)
nn, mm = n // g, m // g
if nn == 1: print((mm-nn)*n);exit()
if mm - nn == 1: print(n);exit()
ans = (mm // nn) * n
num = (mm % nn) * n
i = 2
while True:
    t = (mm - nn) * i
    if t % nn == 0: ans += (mm-nn-1) * (num // t);break
    i += 1
print(ans)
"""
2 6
"""