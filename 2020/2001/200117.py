# BOJ - 2608
a = input();b = input()
d = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1,
     'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
dd = {v: k for k, v in d.items()}
dd = sorted(dd.items(), key=lambda x: x[0], reverse=True)
def func(s):
    v = 0
    i = 0
    while i < len(s):
        if s[i:i+2] in d:
            v += d[s[i:i+2]]
            i += 2
        else:
            v += d[s[i:i+1]]
            i += 1
    return v
v = func(a) + func(b)
print(v)
l = []
for p, q in dd:
    if v // p > 0:
        if q == 'CD' and 'CM' in l \
                or q == 'XL' and 'XC' in l \
                or q == 'IV' and 'IX' in l:
            continue
        l.extend([q] * (v // p))
        v %= p
print(''.join(l))
"""
DLIII
MCMXL
"""