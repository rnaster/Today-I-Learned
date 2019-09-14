# BOJ - 17144
r, c, t = map(int, input().split())
arr = [[*map(int, input().split())] for _ in range(r)]
def func():
    for i in range(r):
        for j in range(c):
            if arr[i][j] < 0:
                return i, j
a, b = func()
for _ in range(t):
    _arr = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if arr[i][j] > 4:
                d = arr[i][j] // 5
                _arr[i][j] += arr[i][j]
                for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    if -1 < i + dx < r and -1 < j + dy < c and arr[i+dx][j+dy] >= 0:
                        _arr[i+dx][j+dy] += d
                        _arr[i][j] -= d
            else:
                _arr[i][j] += arr[i][j]
    tmp0, tmp1 = _arr[0][0], _arr[a][-1]
    _arr[a] = [_arr[a-1][0]] + _arr[a][:-1]
    _arr[a][b] = -1
    _arr[0] = _arr[0][1:] + [_arr[1][-1]]
    for i in range(1, a):
        tmp0, _arr[i][0] = _arr[i][0], tmp0
        tmp1, _arr[a-i][-1] = _arr[a-i][-1], tmp1
    tmp0, tmp1 = _arr[a+1][-1], _arr[-1][0]
    _arr[a+1] = [_arr[a+2][0]] + _arr[a+1][:-1]
    _arr[a+1][b] = -1
    _arr[-1] = _arr[-1][1:] + [_arr[-2][-1]]
    ii = -2
    for i in range(a+2, r-1):
        tmp0, _arr[i][-1] = _arr[i][-1], tmp0
        tmp1, _arr[ii][0] = _arr[ii][0], tmp1
        ii += -1
    if b+1 < c:
        _arr[a][b+1] = 0
        _arr[a+1][b+1] = 0
    arr = _arr
ans = 0
for i in range(r):
    for j in range(c):
        if arr[i][j] > 0: ans += arr[i][j]
print(ans)
"""
7 8 1
0 0 0 0 0 0 0 9
0 0 0 0 3 0 0 8
-1 0 5 0 0 0 22 0
-1 8 0 0 0 0 0 0
0 0 0 0 0 10 43 0
0 0 5 0 15 0 0 0
0 0 40 0 0 0 20 0
"""
exit()

# BOJ - 15685
l = [(0, 0), (1, 0)]
dd = {0: l[:]}
for i in range(1, 11):
    _l = []
    for ll in l[::-1]:
        _l.append((ll[1] * -1, ll[0]))
    a = (l[-1][0] - _l[0][0], l[-1][1] - _l[0][1])
    for _ll in _l[1:]:
        l.append((_ll[0] + a[0], _ll[1] + a[1]))
    dd[i] = l[:]
arr = [[0] * 200 for _ in range(200)]
ans = 0
direct = {0: lambda x: x,
          1: lambda x: (x[1], -x[0]),
          2: lambda x: (-x[0], -x[1]),
          3: lambda x: (-x[1], x[0])}
for _ in range(int(input())):
    x, y, d, g = map(int, input().split())
    for a in dd[g]:
        a = direct[d](a)
        arr[a[0] + 10 + x][a[1] + 37 + y] = 1
for i in range(199):
    for j in range(199):
        if arr[i][j] + arr[i+1][j] + arr[i][j+1] + arr[i+1][j+1] > 3:
            ans += 1
print(ans)
"""
3
3 3 0 1
4 2 1 3
4 2 2 1

4
0 0 0 10
0 100 1 10
100 0 2 10
100 100 3 10
"""
exit()

# BOJ - 14891
from copy import deepcopy as copy
arr = [[*map(int, list(input()))] for _ in range(4)]
for _ in range(int(input())):
    _arr = copy(arr)
    a, b = map(int, input().split())
    a -= 1
    c = b
    for i in range(a, 3):
        if arr[i][2] == arr[i+1][-2]: break
        if c > 0:
            _arr[i+1] = _arr[i+1][1:] + _arr[i+1][:1]
        else:
            _arr[i+1] = _arr[i+1][-1:] + _arr[i+1][:-1]
        c *= -1
    c = b
    for i in range(a, 0, -1):
        if arr[i][-2] == arr[i-1][2]: break
        if c > 0:
            _arr[i-1] = _arr[i-1][1:] + _arr[i-1][:1]
        else:
            _arr[i-1] = _arr[i-1][-1:] + _arr[i-1][:-1]
        c *= -1
    if b > 0:
        _arr[a] = _arr[a][-1:] + _arr[a][:-1]
    else:
        _arr[a] = _arr[a][1:] + _arr[a][:1]
    arr = _arr
print(arr[0][0] * 1 + arr[1][0] * 2 + arr[2][0] * 4 + arr[3][0] * 8)
"""
10101111
01111101
11001110
00000010
2
3 -1
1 1
"""