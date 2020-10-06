# BOJ - 2042
import sys, math
read = sys.stdin.readline
n, m, k = map(int, read().split())
nn = math.ceil(math.log2(n))
arr = [0] * 2 ** (nn + 1)
i = 2 ** nn
for _ in range(n, 2*n):
    arr[i] = int(read())
    i += 1
def func1(a, b, c):
    if a == b:
        return arr[c]
    m = (a+b) // 2
    arr[c] = func1(a, m, 2*c) + func1(m+1, b, 2*c+1)
    return arr[c]
func1(1, 1<<nn, 1)
def func2(a, b, x, y, z):
    if y < a or b < x: return 0
    if a <= x and y <= b:
        return arr[z]
    if x == y:
        return arr[z]
    m = (x+y) // 2
    return func2(a, b, x, m, 2*z) + func2(a, b, m+1, y, 2*z+1)
def func3(a, b, c, d, e):
    if e < a or b < e: return
    arr[c] += d
    if a < b:
        m = (a+b) // 2
        func3(a, m, 2*c, d, e)
        func3(m+1, b, 2*c+1, d, e)
    return
ii = 1 << nn
for _ in range(m+k):
    a, b, c = map(int, read().split())
    if a == 1:
        c -= arr[ii+b-1]
        func3(1, ii, 1, c, b)
    else:
        print(func2(b, c, 1, ii, 1))
"""
5 2 2
1
2
3
4
5
1 3 6
2 2 5
1 5 2
2 3 5
"""