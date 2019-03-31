# BOJ - 2819
import sys
read = lambda: sys.stdin.readline().rstrip()
write = lambda x: sys.stdout.write(str(x)+'\n')
n, m = map(int, read().split())
x_dic, y_dic = {}, {}
x_l, x_r, y_u, y_d = 0, 0, 0, 0
v = 0
for _ in range(n):
    a, b = map(int, read().split())
    if a > 0: x_r += 1
    elif a < 0: x_l += 1
    if a in x_dic: x_dic[a] += 1
    else: x_dic[a] = 1
    if b > 0: y_u += 1
    elif b < 0: y_d += 1
    if b in y_dic: y_dic[b] += 1
    else: y_dic[b] = 1
    v += abs(a) + abs(b)
x, y = 0, 0
for dd in read():
    if dd in ['S', 'J']:
        if dd == 'S':
            if y in y_dic: y_d += y_dic[y]
            v += y_d - y_u
            if y+1 in y_dic: y_u -= y_dic[y+1]
            y += 1
        else:
            if y in y_dic: y_u += y_dic[y]
            v += y_u - y_d
            if y-1 in y_dic: y_d -= y_dic[y-1]
            y -= 1
    else:
        if dd == 'I':
            if x in x_dic: x_l += x_dic[x]
            v += x_l - x_r
            if x+1 in x_dic: x_r -= x_dic[x+1]
            x += 1
        else:
            if x in x_dic: x_r += x_dic[x]
            v += x_r - x_l
            if x-1 in x_dic: x_l -= x_dic[x-1]
            x -= 1
    write(v)
"""
3 5
0 0
1 1
1 -1
SIJJZ
"""