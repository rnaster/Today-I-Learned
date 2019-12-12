# BOJ - 5014
f, s, g, u, d = map(int, input().split())
cache = [0] * (f+1)
cache[s] = 1
q = [s]
ans = 0
while q:
    tmp = []
    for qq in q:
        if qq == g:
            print(ans); exit()
        if qq + u <= f and cache[qq + u] == 0:
            cache[qq + u] = 1
            tmp.append(qq + u)
        if qq - d > 0 == cache[qq - d]:
            cache[qq - d] = 1
            tmp.append(qq - d)
    q = tmp
    ans += 1
print('use the stairs')
"""
10 1 10 2 1

100 2 1 1 0
"""
exit()

# BOJ - 2644
n = int(input())
a, b = map(int, input().split())
arr = [list() for _ in range(n+1)]
for _ in range(int(input())):
    p, q = map(int, input().split())
    arr[p].append(q)
    arr[q].append(p)
ans = 0
q = [a]
cache = [0] * (n+1)
cache[a] = 1
while q:
    tmp = []
    for qq in q:
        if qq == b:
            print(ans);exit()
        for qqq in arr[qq]:
            if cache[qqq] == 0:
                cache[qqq] = 1
                tmp.append(qqq)
    q = tmp
    ans += 1
print(-1)
"""
9
7 3
7
1 2
1 3
2 7
2 8
2 9
4 5
4 6
"""