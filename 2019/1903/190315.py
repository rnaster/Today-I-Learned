# BOJ - 2002
import sys
read = lambda: sys.stdin.readline().rstrip()
n = int(read())
l = [read() for _ in range(n)]
ll = [read() for _ in range(n)]
ans, i, j = n, 0, -1
while j != n-1:
    t = ll.index(l[i])
    if j < t:
        j = t
        ans -= 1
    i += 1
print(ans)
"""
4
ZG431SN
ZG5080K
ST123D
ZG206A
ST123D
ZG431SN
ZG206A
ZG5080K

9
A
B
C
D
E
F
G
H
I
F
G
H
I
A
B
C
D
E

4
a
b
c
d
c
d
b
a

5
ZG206A
PU234Q
OS945CK
ZG431SN
ZG5962J
ZG5962J
OS945CK
ZG206A
PU234Q
ZG431SN
"""