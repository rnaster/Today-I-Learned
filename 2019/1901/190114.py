# BOJ - 5532
L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
print(L - max((A+C-1)//C, (B+D-1)//D))
"""
20
25
30
6
8
"""
exit()

# BOJ - 1790
p, q = map(int, input().split())
a, b = 0, 1
while True:
    if q > a:
        a += 9 * b * 10 ** (b-1)
        b += 1
    else:
        a -= 9 * (b-1) * 10 ** (b-2)
        x = 10 ** (b-2) + (q - a) // (b-1) - 1
        r = (q - a) % (b-1)
        if r:
            if p > x: print(str(x+1)[r-1])
            else: print(-1)
        else:
            if p >= x: print(str(x)[-1])
            else: print(-1)
        break

"""
20 23
"""
exit()

# BOJ - 1748
n = int(input())
m = 1
k = 1
ans = 0
while True:
    if n > m * 9:
        ans += 9 * k * 10 ** (k-1)
    else:
        ans += (n - 10**(k-1) + 1) * k
        print(ans)
        break
    m = 10 * m + 1
    k += 1

"""
120
"""