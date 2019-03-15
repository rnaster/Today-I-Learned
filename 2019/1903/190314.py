# BOJ - 5430
for _ in range(int(input())):
    a, b = input(), int(input())
    c = list(input().strip('[]').split(','))
    if b < 1: print('error'); continue
    d = 1
    skip = False
    for aa in a:
        if aa < 'R':
            if b > 0:
                c.pop(d-1)
                b -= 1
            else: skip = True; print('error'); break
        else: d = 1 - d
    if not skip:
        print('[', end='')
        if d < 1: print(*c[::-1], sep=',', end='')
        else: print(*c, sep=',', end='')
        print(']')
"""
4
RDD
4
[1,2,3,4]
DD
1
[42]
RRD
6
[1,1,2,3,5,8]
D
1
[3]
"""
exit()

# BOJ - 1676
n = int(input())
ans = 0
while True:
    a, b = divmod(n, 5)
    if a < 1: print(ans);break
    ans += a
    n = a
"""
10
"""
exit()

# BOJ - 12851
n, k = map(int, input().split())
visit = [0] * max(n + 2, k + 2)
visit[n] = 1
cache = [0] * max(n + 2, k + 2)
cache[n] = 1
q = [n]
ans = 0
while True:
    temp = []
    _visit = []
    for i in q:
        if i > 0:
            if visit[i - 1] < 1:
                temp.append(i-1)
                _visit.append(i-1)
                cache[i - 1] += cache[i]
        if i <= k:
            if visit[i + 1] < 1:
                temp.append(i+1)
                _visit.append(i+1)
                cache[i + 1] += cache[i]
        if i*2 <= k+1:
            if visit[i * 2] < 1:
                temp.append(i*2)
                _visit.append(i*2)
                cache[i * 2] += cache[i]
    for i in _visit:
        visit[i] = 1
    ans += 1
    if visit[k] > 0:
        break
    q = temp
print(ans)
print(cache[k])
# print(cache)

"""
5 34
"""