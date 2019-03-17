# BOJ - 1011
import sys
read = lambda: sys.stdin.readline().rstrip()
for _ in range(int(read())):
    a, b = map(int, read().split())
    c = b-a
    k = int(c**0.5)
    if c - k*k > 0:
        if c - k*k <= k: print(2*k)
        else: print(2*k+1)
    else: print(2*k-1)
"""
3
0 3
1 5
45 50

"""
