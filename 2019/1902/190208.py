# BOJ - 1712
p, q, r = map(int, input().split())
if q >= r: print(-1)
else: print(p // (r-q) + 1)
"""
1000 70 170
1000 160 170
"""
exit()

# BOJ - 1016
m, n = map(int, input().split())
p = 2
l = []
while n > p*p:
    l.append(p*p)
    p += 1
arr = list(range(m, n+1))
for ll in l:
    tmp = []
    for i in arr:
        if i % ll != 0:
            tmp.append(i)
    arr = tmp[:]
print(len(arr))
"""
1 10
100 100000
"""
exit()

# BOJ - 1629
a, b, c = map(int, input().split())
a %= c
if abs(a-c) < a:
    a -= c
def main(b):
    global a, c
    if b < 2: return (a ** b) % c
    else:
        t = main(b//2)
        return t*t*(a**(b%2)) % c
print(main(b))
"""
10 12 12
10 11 12
10 10 12
2 3 7
2 10 7
"""
