# BOJ - 4055
import sys
read = sys.stdin.readline
i = 1
while 1:
    p = int(read())
    if p == 0: break
    ans = 0
    c = 0.
    for a, b in sorted([[*map(int, read().split())] for _ in range(p)],
                       key=lambda x: (x[1], x[0])):
        t = max(a, c) + 0.5
        if t <= b:
            ans += 1
            c = t
    print(f'On day {i} Emma can attend as many as {ans} parties.')
    i += 1
"""
8
8 9
8 9
9 10
9 10
9 10
23 24
23 24
23 24
8
12 13
13 14
12 13
9 10
9 10
12 13
12 14
9 11
3
14 15
14 15
14 15
0
"""