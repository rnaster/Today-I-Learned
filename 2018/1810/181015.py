# BOJ - 1057
import math
n, a, b = map(int, input().split())
a, b = min(a, b), max(a, b)
ans = math.ceil(math.log2(n))
k = ans - 1
while True:
    tmp = pow(2, k)
    if tmp < b:
        if tmp < a: a, b = a - tmp, b - tmp
        else: print(ans); exit()
    k -= 1
    ans -= 1
"""
16 8 9
"""