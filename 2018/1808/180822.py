# BOJ - 4673
from sys import stdout
write = lambda x: stdout.write(x)
s = set(range(1, 10000))
def f(N):
    a, r = divmod(N, 1000)
    b, r = divmod(r, 100)
    c, d = divmod(r, 10)
    return a, b, c, d
for i in range(1, 10000):
    a, b, c, d = f(i)
    if i + a + b + c + d >= 10000: continue
    s.difference_update({i + a + b + c + d})
for n in sorted(list(s)):
    write(str(n) + '\n')
"""
1, 3, 5, 7, 9, 20, 31, 42, 53, 64, 75, 86, 97
1, 3, 5, 7, 9, 20, 31, 42, 53, 64, 75, 86, 97
"""