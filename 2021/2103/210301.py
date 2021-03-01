# BOJ - 17828
from string import ascii_uppercase
a, b = map(int, input().split())
if b < a or b > a * 26:
    print("!")
    exit()
b -= a
p, q = divmod(b, 25)
a -= p
if q > 0:
    a -= 1
print("A" * a, ascii_uppercase[q] * bool(q), "Z" * p, sep="")
"""
6 64

6 157
"""