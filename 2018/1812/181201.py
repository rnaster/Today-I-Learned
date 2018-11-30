# BOJ - 4948
from sys import stdin, stdout
read = lambda: stdin.readline().rstrip()
write = lambda x: stdout.write(str(x) + '\n')
def bisect(l, num):
    a = 0
    b = len(l)-1
    c = (a+b) // 2
    while a <= c < b:
        if l[c] < num:
            a = c+1
        else:
            b = c
        c = (a+b) // 2
    return c
p = [2]
N = 2
while True:
    n = int(read())
    if n == 0: exit()
    if n == 1: print(1);continue
    if N < n*2:
        N += 1
        while N <= n * 2:
            isprime = True
            for i in p:
                if i * i <= N:
                    if N % i == 0: isprime=False;break
                else: break
            if isprime: p.append(N)
            N += 1
        N -= 1
    a = bisect(p, n)
    b = None if p[-1] <= n * 2 else bisect(p, n*2)
    ans = len(p[a:b])
    if p[a] == n: ans -= 1
    write(ans)
"""
1
10
13
100
1000
10000
100000
0
"""