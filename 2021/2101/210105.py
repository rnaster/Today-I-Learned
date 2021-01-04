# BOJ - 14719
n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]
for j, v in enumerate(map(int, input().split())):
    for i in range(1, v+1):
        arr[-i][j] = 1
ans = 0
for i in range(1, n+1):
    flag = False
    a = 0
    for j in range(m):
        if arr[-i][j] == 1:
            if flag:
                ans += a
                a = 0
            else:
                flag = True
        elif flag:
            a += 1
print(ans)
print(*arr, sep='\n')
"""
4 4
3 0 1 4
"""
exit()

# BOJ - 1963
prime = []
l = [True] * 10000
for i in range(2, 10000):
    if l[i]:
        for j in range(i*i, 10000, i):
            l[j] = False
        if i > 1000:
            prime.append(i)
d = {p: i for i, p in enumerate(prime)}
def func(a, b):
    ans = 0
    q = [a]
    visit = [True] * len(prime)
    visit[d[a]] = False
    while q:
        tmp = []
        for p in q:
            if p == b:
                return ans
            div = 10
            for _ in range(4):
                x, _ = divmod(p, div)
                y = p % (div // 10)
                for i in range(10):
                    pp = x*div + i * div // 10 + y
                    if pp in d and visit[d[pp]]:
                        tmp.append(pp)
                        visit[d[pp]] = False
                div *= 10
        q = tmp
        ans += 1
    return 0
for _ in range(int(input())):
    a, b = map(int, input().split())
    print(func(a, b))
"""
3
1033 8179
1373 8017
1033 1033
"""