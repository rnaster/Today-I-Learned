# BOJ - 1022
from sys import stdout
write = lambda x: stdout.write(x)
r1, c1, r2, c2 = map(int, input().split())
c0 = c2 - c1
lines, mx = [], 0
for r in range(r1, r2+1):
    if r < 0:
        init_r = 4*r*r + r + 1
        if c1 <= 0:
            if r > c1:
                init_r += 4*c1*c1 - c1 - 4*r*r
            else:
                init_r -= c1
        else:
            if -r > c1:
                init_r -= c1
            else:
                init_r += 4*c1*c1 - 3*c1 - 4*r*r - 2*r
    elif r == 0:
        if c1 < 0:
            init_r = 4*c1*c1 - c1 + 1
        elif c1 > 0:
            init_r = 4*c1*c1 - 3 * c1 + 1
        else: init_r = 1
    else:
        init_r = 4*r*r + 3*r + 1
        if c1 <= 0:
            if r >= -c1:
                init_r += c1
            else:
                init_r += 4*c1*c1 -c1 - 4*r*r -2*r
        else:
            if r+1 >= c1:
                init_r += c1
            else:
                init_r += 4*c1*c1 - 3*c1 - 4*(r+1)*(r+1) + 4*(r+1)
    l = [init_r]
    if r <= 0:
        for c in range(c1+1, c2+1):
            if c <= 0:
                if r >= c:
                    l.append(l[-1] + 8*c-5)
                else: l.append(l[-1] - 1)
            else:
                if -r >= c:
                    l.append(l[-1] - 1)
                else:
                    l.append(l[-1] + 8*(c-1) + 1)
    else:
        for c in range(c1+1, c2+1):
            if c <= 0:
                if r <= -c:
                    l.append(l[-1] + 8*c - 5)
                else:
                    l.append(l[-1] + 1)
            else:
                if r+1 >= c:
                    l.append(l[-1] + 1)
                else:
                    l.append(l[-1] + 8*(c-1) + 1)
    lines.append(l)
    mx = max(*l, mx)
ss = len(str(mx))
for line in lines:
    s = ''
    for n in line:
        s += ' ' * (ss - len(str(n))) + '%s '
    s += '\n'
    write(s % tuple(line))
"""
-3 -3 2 0
-3 -3 2 1
-3 -2 2 2
-3 0 2 3
-3 -2 2 -2
-3 2 3 2
-3 4 3 4
-3 2 3 3
-3 2 -3 4
-3 -2 3 2
"""