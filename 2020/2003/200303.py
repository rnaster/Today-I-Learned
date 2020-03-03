# BOJ - 1041
n = int(input())
a, b, c, d, e, f = map(int, input().split())
if n == 1:
    print(a + b + c+d+e+f - max(a, b, c, d, e, f))
    exit()
p = min(a+b,a+c,a+e,a+d,c+b,c+e,c+f,b+f,b+d,f+d,f+e,e+d)
q = min(a+b+c, a+c+e, a+b+d, a+d+e,
        f+b+c, f+c+e, f+b+d, f+d+e)
r = min(a, b, c, d, e, f)
print(r * (n-2) * (5*n-6) + p * 4*(2*n - 3) + q * 4)
"""
5
1 2 3 4 5 6
"""
exit()

# BOJ - 6064
import sys, math
read = sys.stdin.readline
def func1(n, m, x, y):
    c = y % n
    l = [(c + (m-n) * i) % n for i in range(n // math.gcd(n, m))]
    try:
        r = l.index(x % n)
    except ValueError:
        return -1
    return r * m + y
def func2(n, m, x, y):
    l = [(y - (n-m) * i) % n for i in range(n // math.gcd(n, m))]
    try:
        r = l.index(x % n)
    except ValueError:
        return -1
    return r * m + y
for _ in range(int(read())):
    n, m, x, y = map(int, read().split())
    if x > n or y > m: print(-1);continue
    if n < m:
        print(func1(n, m, x, y))
    elif n > m:
        print(func2(n, m, x, y))
    elif x == y:
        print(x)
    else:
        print(-1)
"""
4
10 12 3 9
10 12 7 2
13 11 5 6
13 11 1 4
"""