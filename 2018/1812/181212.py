# BOJ - 1021
n, m = map(int, input().split())
l = list(map(int, input().split()))
ans = 0
for _ in range(m):
    a = l.pop(0)
    b = min(a-1, n-a+1)
    ans += b
    t = []
    for ll in l:
        if ll > a:
            t.append(ll - b - 1)
        else:
            t.append(ll + b + 1)
    s = min(t)-1 if t else 0
    u = []
    for tt in t:
        u.append(tt - s)
    s = max(s, 1)
    n -= s
    n = min(n, len(u))
    l = u[:]
print(ans)
"""
10 3
1 2 3

9 6
5 1 4 2 3 9
"""