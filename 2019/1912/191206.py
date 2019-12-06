# BOJ - 2606
n = int(input())
d = {}
for _ in range(int(input())):
    a, b = map(int, input().split())
    d.setdefault(a, {b}).add(b)
    d.setdefault(b, {a}).add(a)
cache = [0] * n
cache[0] = 1
q = [1]
ans = 0
while q:
    tmp = []
    for i in q:
        for j in d[i]:
            if cache[j-1] == 0:
                tmp.append(j)
                cache[j-1] = 1
                ans += 1
    q = tmp
print(ans)
"""
7
6
1 2
2 3
1 5
5 2
5 6
4 7
"""