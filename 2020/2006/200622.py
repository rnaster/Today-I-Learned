# BOJ - 1111
import math
n = int(input())
arr = [*map(int, input().split())]
if n == 1: print("A");exit()
if n == 2:
    if arr[0] == arr[1]: print(arr[0])
    else: print("A")
    exit()
def func(l, ll):
    return sum(a * b for a, b in zip(l, ll))
arr1 = arr[:-1]
arr2 = arr[1:]
one = [1] * (n - 1)
a = func(arr1, arr1)
b = c = func(arr1, one)
d = n - 1
e = func(arr1, arr2)
f = func(one, arr2)
if a == 0 or f == 0: print("B");exit()
q1 = a // c
q2 = b // d
q3 = e // f
if a % c == 0 and b % d == 0 and q1 == q2:
    if e % f == 0 and q3 == q1 and f % math.gcd(c, d) == 0:
        print("A")
    else:
        print("B")
    exit()
dt = a * d - b * c
a, d = d, a
b, c = -b, -c
a1, a2 = (a * e + b * f) // dt, (c * e + d * f) // dt
print(arr[-1] * a1 + a2)
"""
4
1 4 13 40

5
3 3 3 3 4


"""
