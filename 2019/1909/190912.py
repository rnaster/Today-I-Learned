# BOJ - 14888
from itertools import permutations
input()
arr = tuple(map(int, input().split()))
oper = tuple(map(int, input().split()))
sign = lambda x: 1 if x > 0 else -1
d = {0: lambda x, y: x+y,
     1: lambda x, y: x-y,
     2: lambda x, y: x*y,
     3: lambda x, y: abs(x)//y * sign(x)}
a, b = -2 ** 34, 2 ** 34
l = []
for i, o in enumerate(oper):
    l += [i] * o
cache = {(): arr[0]}
def func(arr, per):
    if per in cache:
        return cache[per]
    cache[per] = d[per[-1]](func(arr[:-1], per[:-1]), arr[-1])
    return cache[per]
for per in set(permutations(l, sum(oper))):
    c = func(arr, per)
    a = max(a, c)
    b = min(b, c)
print(a, b, sep='\n')
# print(cache)
# print(len(cache))
# c = arr[0]
# for ar, p in zip(arr[1:], (1, 3, 0, 0, 2)):
#     c = d[p](c, ar)
#     print(c, '#')
"""
6
1 2 3 4 5 6
2 1 1 1

11
1 2 3 4 5 6 7 8 9 10 11
3 3 3 2
"""