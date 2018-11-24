# BOJ - 2804
from sys import stdout
write = lambda x: stdout.write(x)
A, B = input().split()
a, b = -1, -1
aa = 0
for i in A:
    bb = 0
    for j in B:
        if i == j: a = aa; b = bb; break
        bb += 1
    if a != -1: break
    aa += 1
s = '.'*a + '%s' + '.' * (len(A)-1-a) + '\n'
bb = 0
for j in B:
    if bb == b: write(A + '\n')
    else: write(s % j)
    bb += 1
"""
BANANA PIDZAMA
"""