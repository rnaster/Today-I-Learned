# BOJ - 1673
def func(a, b):
    ans = 0
    c = 0
    while a > 0:
        ans += a
        c += a % b
        a //= b
        a += c // b
        c %= b
    return ans
while True:
    try:
        n, k = map(int, input().split())
        print(func(n, k))
    except:
        break
"""
4 3
10 3
100 5
33 7
"""
exit()

# BOJ - 1074
n, r, c = map(int, input().split())
def func(p, q, r):
    if p == 1:
        return q*2 + r
    a = 2 ** (2*p-2)
    b = 2 ** (p-1)
    if q >= b and r >= b:
        return 3 * a + func(p-1, q - b, r - b)
    if q >= b:
        return 2 * a + func(p-1, q - b, r)
    if r >= b:
        return a + func(p-1, q, r - b)
    return func(p-1, q, r)
print(func(n, r, c))
"""
3 7 7

2 3 1
"""