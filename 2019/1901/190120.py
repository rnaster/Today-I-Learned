# BOJ - 9519
import math
n = int(input())
s = input()
a = len(s)
def forward(n):
    global s
    k = math.ceil(a//2)
    for _ in range(n):
        i = -1
        t = ''
        for j in range(k):
            t += s[j] + s[i]
            i += -1
        s = t + s[k] if a % 2 else t
    return s
def backward(n):
    global s
    c = 2 if a % 2 else 1
    for _ in range(n):
        t = ''
        for i in range(0, a, 2):
            t += s[i]
        for j in range(-c, -a, -2):
            t += s[j]
        s = t
    return s
b = n % (a-1)
if a - b > b: print(backward(b))
else: print(forward(a-b-1))
"""
4
0 abcdef
1 afbecd
2 adfcbe
3 aedbfc
4 acefdb
5 abcdef


6
0 abcdefg
1 agbfced
2 adgebcf
3 afdcgbe
4 aefbdgc
5 acegfdb
6 abcdefg
"""