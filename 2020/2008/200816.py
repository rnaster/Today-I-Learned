# BOJ - 4195
import sys
read = sys.stdin.readline
s = {}
def find(a):
    aa, bb = s[a]
    if bb == "":
        return [aa, a]
    s[a] = t = find(bb)
    return t
for _ in range(int(input())):
    s = {}
    for _ in range(int(read())):
        a, b = read().split()
        s.setdefault(a, [1, ""])
        s.setdefault(b, [1, ""])
        a1, a2 = find(a)
        b1, b2 = find(b)
        if a2 == b2:
            print(a1)
        else:
            s[b2][1] = a2
            s[a2][0] = a1 + b1
            print(a1 + b1)
"""
2
3
Fred Barney
Barney Betty
Betty Wilma
3
Fred Barney
Betty Wilma
Barney Betty
"""