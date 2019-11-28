# BOJ - 9519
x = int(input())
a = input()
b = set()
c = []
aa = len(a)
while a not in b:
    b.add(a)
    c.append(a)
    a = a[::2] + a[1:aa:2][::-1]
print(c[x % len(c)])
"""
9
acefdb

7
agbfced

8
adgebcf

10
aehdbfgc
"""