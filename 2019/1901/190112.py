# BOJ - 3005
r, c = map(int, input().split())
l = []
ans = 'x'*20
for _ in range(r):
    s = input()
    l.append(s)
    t, ll = '', 0
    if '#' in s:
        for ss in s:
            if ss == '#':
                if ll > 1:
                    if t < ans: ans = t
                t = ''
                ll = 0
            else:
                t += ss
                ll += 1
        if ll > 1:
            if t < ans: ans = t
    else:
        if s < ans: ans = s
for i in range(c):
    s = ''
    for j in range(r):
        s += l[j][i]
    t, ll = '', 0
    if '#' in s:
        for ss in s:
            if ss == '#':
                if ll > 1:
                    if t < ans: ans = t
                t = ''
                ll = 0
            else:
                t += ss
                ll += 1
        if ll > 1:
            if t < ans: ans = t
    else:
        if s < ans: ans = s
print(ans)
"""
5 4
luka
o#a#
kula
i#ba
aka#

3 3
aa#
#a#
bc#

2 3
#aa#
#xy#

4 7
#####xy
#aa##xy
#zz##xx
#####xx

"""
exit()

# BOJ - 10984
for _ in range(int(input())):
    c = 0
    g = 0
    for _ in range(int(input())):
        c_, g_ = map(float, input().split())
        c += c_
        g += g_ * c_
    g += 0.01
    print(int(c), round(g / c, 1))
"""
2
4
3 4.3
2 2.0
4 0.0
2 4.0
3
4 0.0
4 0.0
3 0.0
"""
exit()

# BOJ - 5046
n, b, h, w = map(int, input().split())
p = 200*10000 + 1
for _ in range(h):
    pp = int(input())
    for ww in map(int, input().split()):
        if n <= ww: p = min(p, n*pp);break
if p > b: print('stay home')
else: print(p)
"""
3 1000 2 3
200
0 2 2
300
27 3 20
"""