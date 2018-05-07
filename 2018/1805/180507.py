# BOJ - 1344
from math import factorial

def mCn(n, m=18):
    res = factorial(m) // factorial(m-n) // factorial(n)
    return res

a = int(input()) * 0.01
b = int(input()) * 0.01
A, B = 0, 0
for i in [0, 1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18]:
    A += mCn(i) * a ** i * (1-a) ** (18-i)
    B += mCn(i) * b ** i * (1-b) ** (18-i)
if a == 0 and b != 0:
    print(1 - B)
elif a != 0 and b == 0:
    print(1 - A)
elif a == 0 and b == 0:
    print(0)
else:
    print(1 - (A*B))

'''
50
50
0.5265618908306351
0.5265671403612942
'''