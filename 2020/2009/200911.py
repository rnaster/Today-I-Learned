# BOJ - 2931
n, m = map(int, input().split())
arr = [input() for _ in range(n)]
p = []
for i in range(n):
    for j in range(m):
        if arr[i][j] in ("M", "Z"):
            d = ((-1, 0), (0, 1), (1, 0), (0, -1))
            flag = True
            t1, t2, t3 = -1, -1, -1
            for k in range(4):
                if -1 < i+d[k][0] < n and -1 < j+d[k][1] < m:
                    if arr[i+d[k][0]][j+d[k][1]] != ".":
                        p.append((i, j, k))
                        flag = False
                        break
                    else:
                        t1, t2, t3 = i, j, k
            if flag:
                p.append((t1, t2, t3))
def func1(a, b, c):
    if c == 0:
        a -= 1
    elif c == 1:
        b += 1
    elif c == 2:
        a += 1
    else:
        b -= 1
    return a, b, c
def func2(a, b, c, d):
    if d == "|":
        if c == 2: return a+1, b, c
        if c == 0: return a-1, b, c
    if d == "-":
        if c == 1: return a, b+1, c
        if c == 3: return a, b-1, c
    if d == "+":
        if c in (0, 2): return func2(a, b, c, "|")
        return func2(a, b, c, "-")
    if d == "1":
        if c == 0: return a, b+1, 1
        if c == 3: return a+1, b, 2
    if d == "2":
        if c == 2: return a, b+1, 1
        if c == 3: return a-1, b, 0
    if d == "3":
        if c == 1: return a-1, b, 0
        if c == 2: return a, b-1, 3
    if d == "4":
        if c == 1: return a+1, b, 2
        if c == 0: return a, b-1, 3
    return a, b, c
q = []
for a, b, c in p:
    aa, bb, cc = func1(a, b, c)
    if arr[aa][bb] == ".":
        q.append((a, b, c))
        continue
    a, b, c = aa, bb, cc
    while 1:
        aa, bb, cc = func2(a, b, c, arr[a][b])
        if arr[aa][bb] == ".":
            q.append((a, b, c))
            break
        a, b, c = aa, bb, cc
print(p, q)
a, b, c = q[0]
a, b, c = func2(a, b, c, arr[a][b])
print((a, b, c), "*")
x, y, z = q[1]
for i in ("|", "-", "+", "1", "2", "3", "4"):
    t1, t2, t3 = func2(a, b, c, i)
    print((t1, t2, t3), "#")
    if (x, y) == (t1, t2):
        print(a+1, b+1, i)
        break
"""
6 10
Z.1----4..
|.|....|..
|..14..M..
2-+++4....
..2323....
..........

3 7
.14....
.M.Z...
..23...

1 3
M.Z
"""
exit()

# BOJ - 10800
import sys
read = sys.stdin.readline
n = int(read())
arr = [0] * n
l = {}
ans = [0] * n
t, p, q = 0, 0, 0
for i, (a, b) in sorted(enumerate([*map(int, read().split())] for _ in range(n)),
                        key=lambda x: x[1][1]):
    if t == b:
        ans[i] = p - arr[a-1] - q + l.get(a-1, 0)
    else:
        ans[i] = p - arr[a-1]
        t = b
        l = {}
        q = 0
    p += b
    arr[a-1] += b
    l[a-1] = l.get(a-1, 0) + b
    q += b
for a in ans:
    print(a)
"""
7
1 10
3 15
1 3
4 8
3 8
2 8
2 8
"""