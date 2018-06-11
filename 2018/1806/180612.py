# BOJ - 1947
import sys
n = int(input())
d0, d1, d2 = 0, 1, 2
if n <= 3: print(n-1); sys.exit()
s0, s1, s2 = 1, 3, 11
for i in range(4, n+1):
    d0, d1, d2 = d1, d2, (i - 1) * s1 % 1000000000
    s0, s1, s2 = s1, s2, (i * s2 + d2) % 1000000000
print(d2)
