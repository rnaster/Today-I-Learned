# BOJ - 12970
n, k = map(int, input().split())
if n // 2 * (n - n // 2) < k: print(-1);exit()
ans = ['A'] * n
if k < n-1:
    ans[k-n] = 'B'
    print(''.join(ans))
    exit()
i, j = 0, 0
for i in range(1, n//2+1):
    if (n-i)*i == k:
        ans[-i:] = ['B'] * i
        print(''.join(ans))
        exit()
    if (n - i)*i > k:
        i -= 1
        j = k - (n-i)*i + i
        break
ans[-i:] = ['B'] * i
ans[j] = 'B'
print(''.join(ans))
"""
10 12
"""
exit()

# BOJ - 12904
a = input();b = input()
for _ in range(len(b)-len(a)):
    if b[-1] == 'B':
        b = b[:-1]
        b = b[::-1]
    else:
        b = b[:-1]
if a == b: print(1)
else: print(0)
"""
B
ABBA
"""
exit()

# BOJ - 11559
arr = []
for _ in range(12):
    a = input()
    if a != '......':
        arr.append([*a])
visit = []
n = len(arr)
def d(a, b):
    yield a+1, b;yield a-1, b;yield a, b+1;yield a, b-1
def func(a, b):
    t = arr[a][b]
    q = [(a, b)]
    qq = [(a, b)]
    while q:
        tmp = []
        for x, y in q:
            for aa, bb in d(x, y):
                if -1 < aa < n and -1 < bb < 6 and visit[aa][bb]:
                    if arr[aa][bb] == '.':
                        visit[aa][bb] = False
                    elif arr[aa][bb] == t:
                        qq.append((aa, bb))
                        tmp.append((aa, bb))
                        visit[aa][bb] = False
        q = tmp
    if len(qq) > 3:
        for x, y in qq:
            arr[x][y] = '.'
        return 1
    return 0
def func2():
    global arr
    for j in range(6):
        l = []
        for i in range(1, n+1):
            if arr[-i][j] != '.':
                l.append(arr[-i][j])
            arr[-i][j] = '.'
        for i, ii in enumerate(l, 1):
            arr[-i][j] = ii
    arr = [a for a in arr if a.count('.') < 6]
    return
ans = 0
while 1:
    tmp = 0
    n = len(arr)
    visit = [[True] * 6 for _ in range(n)]
    for i in range(n):
        for j in range(6):
            visit[i][j] = False
            if arr[i][j] != '.':
                tmp |= func(i, j)
    if tmp: ans += tmp
    else: break
    func2()
print(ans)
"""
......
......
......
......
......
......
......
......
.Y....
.YG...
RRYG..
RRYGG.
"""
exit()

# BOJ - 2174
n, m = map(int, input().split())
arr = [[0] * n for _ in range(m)]
n2, m2 = map(int, input().split())
idx = [[-1, -1, -1] for _ in range(n2+1)]
d = {'N': 0, 'W': 1, 'S': 2, 'E': 3}
for i in range(1, n2+1):
    a, b, c = input().split()
    a, b = int(a), int(b)
    arr[-b][a-1] = i
    idx[i] = [-b, a-1, d[c]]
dd = [(-1, 0), (0, -1), (1, 0), (0, 1)]
for _ in range(m2):
    a, b, c = input().split()
    a, c = int(a), int(c)
    x, y, z = idx[a]
    if b == 'F':
        dx, dy = dd[z]
        arr[x][y] = 0
        for _ in range(c):
            x += dx;y += dy
            if -m <= x < 0 and -1 < y < n:
                if arr[x][y] > 0:
                    print('Robot %s crashes into robot %s' % (a, arr[x][y]))
                    exit()
            else:
                print('Robot %s crashes into the wall' % a)
                exit()
        arr[x][y] = a
        idx[a] = [x, y, z]
    elif b == 'L':
        idx[a] = [x, y, (z+c) % 4]
    else:
        idx[a] = [x, y, (z-c) % 4]
print('OK')
"""
3 3
1 9
2 2 W
1 F 1
1 L 1
1 F 1
1 L 1
1 F 2
1 L 5
1 F 2
1 R 3
1 F 2

5 4
2 4
1 1 E
5 4 W
1 F 3
2 F 1
1 L 1
1 F 3

5 4
2 2
1 1 E
5 4 W
1 L 96
1 F 2

5 4
2 3
1 1 E
5 4 W
1 F 4
1 L 1
1 F 20
"""