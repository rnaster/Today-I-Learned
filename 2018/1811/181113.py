# BOJ - 1790
# import random
# for _ in range(10):
#     a, b = random.randint(1, 1000), random.randint(1, 3000)
#     print(a, b, 'a b')
#     # a, b = map(int, input().split())
#     c, d = 9, 1
#     while True:
#         if a > c and b > c * d: a -= c; b -= c * d; d += 1; c *= 10
#         else: break
#     if d * a < b: print(-1);continue#exit()
#     p, q = divmod(b, d)
#     print(a, b, d, '######')
#     if p == 0: print(str(10 ** (d-1))[::-1][q])
#     else: print(str(10 ** (d-1) + p - 1)[::-1][q])
#     print()
# a, b = map(int, input().split())
a, b = 200, 492
c, d = 9, 1
while True:
    if a > c and b > c * d: a -= c; b -= c * d; d += 1; c *= 10
    else: break
if d * a < b: print(-1);exit()
p, q = divmod(b, d)
print(a, b, d, p, q, '######')
if p == 0: print(str(10 ** (d-1))[q-1])
else: print(str(10 ** (d-1) + p - 1)[::-1][q])
"""
20 23
"""