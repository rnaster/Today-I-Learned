# BOJ - 15903
n, m = map(int, input().split())
arr = sorted([*map(int, input().split())])
for _ in range(m):
    a, b = arr[0], arr[1]
    arr[0], arr[1] = a+b, a+b
    arr.sort()
print(sum(arr))
"""
4 2
4 2 3 1
"""
# PriorityQueue 보다 heapQueue가 더 빠름...
exit()

# BOJ - 16235
import sys
read = lambda: sys.stdin.readline().rstrip()
n, m, k = map(int, read().split())
ground = [[5] * n for _ in range(n)]
arr = [list(map(int, read().split())) for _ in range(n)]
d = {(i, j): [] for i in range(n) for j in range(n)}
direction = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
dd = {(i, j): 0 for i in range(n) for j in range(n)}
for _ in range(m):
    x, y, z = map(int, read().split())
    d[(x-1, y-1)].append(z)
for _ in range(k):
    for x, y in d:
        zz, a = 0, 0
        temp = []
        for z in d[(x, y)]:
            if ground[x][y] >= z:
                ground[x][y] -= z
                z += 1
                temp.append(z)
                if z % 5 == 0: a += 1
                # print(kk, (x, y), z, 'ground : %d' % ground[x][y])
            else: zz += z // 2
        d[(x, y)] = temp
        ground[x][y] += zz + arr[x][y]
        dd[(x, y)] = a
    for x, y in dd:
        if dd[(x, y)] < 1: continue
        for dx, dy in direction:
            if -1 < x + dx < n and -1 < y + dy < n:
                d[(x+dx, y+dy)] = [1] * dd[(x, y)] + d[(x+dx, y+dy)]
ans = 0
for i in range(n):
    for j in range(n):
        ans += len(d[(i, j)])
print(ans)
"""
5 2 3
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 1 3
3 2 3

5 2 1
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 1 3
3 2 3

5 2 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 1 3
3 2 3
"""
exit()

# BOJ - 1773
n, c = map(int, input().split())
cache = [0] * (c+1)
ans = 0
s = set()
for _ in range(n):
    a = int(input())
    if a in s: continue
    s.add(a)
    for i in range(a, c+1, a):
        if cache[i] < 1: ans += 1; cache[i] = 1
print(ans)
"""
3 20
4
6
7
"""
exit()

# BOJ - 5556
import sys
read = lambda: sys.stdin.readline().rstrip()
d = {1:1,2:2,0:3}
n = int(read())
a = (n+1) // 2
b = (n+1) % 2
c = a % 3
for _ in range(int(read())):
    p, q = map(int, read().split())
    r = min(abs(p-a), abs(q-a),
            max(abs(p-a-b), abs(q-a-b)),
            max(abs(p-a), abs(q-a-b)),
            max(abs(p-a-b), abs(q-a)))
    print(d[(c-r) % 3])
"""
11
4
5 2
9 7
4 4
3 9

16
5
8 8
8 9
9 8
9 9
7 8

"""
exit()

# programmers - 2017 kakao blind - 추석 트래픽
lines = [
'2016-09-15 20:59:57.421 0.351s',
'2016-09-15 20:59:58.233 1.181s',
'2016-09-15 20:59:58.299 0.8s',
'2016-09-15 20:59:58.688 1.041s',
'2016-09-15 20:59:59.591 1.412s',
'2016-09-15 21:00:00.464 1.466s',
'2016-09-15 21:00:00.741 1.581s',
'2016-09-15 21:00:00.748 2.31s',
'2016-09-15 21:00:00.966 0.381s',
'2016-09-15 21:00:02.066 2.62s'
]
def solution(lines):
    l = []
    size = len(lines)
    for line in lines:
        _, t, e = line.split(' ')
        h, m, s = t.split(':')
        h, m, s, e = int(h), int(m), float(s), float(e[:-1])
        p, s = divmod(s-e, 60)
        p, m = divmod(m+p, 60)
        h += p
        h, m = map(int, (h, m))
        s = round(s, 3)
        tt = ':'.join(map(lambda x: str(x).zfill(2), (h, m, s)))
        l.append((tt, t))
    ans = 0
    for i in range(size):
        tmp = 0
        a, b = l[i]
        for j in range(size):
            c, d = l[j]
            if a <= c <= b or a <= d <= b: tmp += 1
            # else: break
        ans = max(tmp, ans)
    return ans
print(solution(lines))
