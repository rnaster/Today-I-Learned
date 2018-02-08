# BOJ - 10164
from sys import stdout, stdin
read = lambda: stdin.readline().rstrip()
m, n, k = map(int, read().split())
def func(a, b):
    f = 1
    if a > b: a, b = b, a
    for i in range(1, a+1):
        f *= (a+b-i+1)
        f //= i
    return f
# import math
# print(math.factorial(30)//math.factorial(15)//math.factorial(15))
if k == 0:
    print(func(m-1, n-1))
else:
    a = k // n
    b = k % n if k % n else n
    stdout.write(str(func(a, b-1) * func(m-a-1, n-b)) + '\n')
    # print(func(a, b-1) * func(m-a-1, n-b))
    # k가 side에 있을때 골치 아픔.