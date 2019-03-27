# BOJ - 16677
m = input()
s = len(m)
val, ans = 0, 'No Jam'
for _ in range(int(input())):
    w, g = input().split()
    g = int(g)
    k, t = 0, 0
    ww = len(w)
    if s > ww: continue
    for j in range(ww):
        if k < s:
            if w[j] == m[k]:
                k += 1
            else:
                t += 1
        else:
            t += ww - j
            break
    tt = g / t
    if val < tt and k == s: val = tt; ans = w
print(ans)

"""
DEVILIV
4
DEVILIVI 10
DEVILM 11
DEVILIVCONFIRMED 66
DENVERVILLAINV 70

SUBINIUM
3
INSSADANCINGMACHINE 12
SOULLESSDANCINGMACHINE 345
ALGORITHMDANCINGMACHINE 6789

"""
exit()

# BOJ - 16674
n = input()
d = {'2':0, '0':0, '1':0, '8':0}
for nn in n:
    if not nn in d: print(0);exit()
    d[nn] += 1
for dd in d:
    if d[dd] < 1: print(1);exit()
a = d['2']
for dd in d:
    if a != d[dd]: print(2);exit()
print(8)
"""
20181208

1280821

10

4
"""