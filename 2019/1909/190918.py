# BOJ - 5373
# 미친 문제...
arr_u = [['w'] * 3 for _ in range(3)]
arr_d = [['y'] * 3 for _ in range(3)]
arr_l = [['g'] * 3 for _ in range(3)]
arr_r = [['b'] * 3 for _ in range(3)]
arr_f = [['r'] * 3 for _ in range(3)]
arr_b = [['o'] * 3 for _ in range(3)]
def func_rot(arr, rot):
    _arr = [[''] * 3 for _ in range(3)]
    if rot == '+':
        for i in range(3):
            for j in range(3):
                _arr[j][2-i] = arr[i][j]
        return _arr
    for i in range(3):
        for j in range(3):
            _arr[2-j][i] = arr[i][j]
    return _arr
def func_u(rot, idx=0):
    global arr_f, arr_b, arr_r, arr_l, arr_u, arr_d
    if rot == '+':
        arr_f[idx], arr_r[idx], arr_b[idx], arr_l[idx]\
            = arr_r[idx], arr_b[idx][::-1], arr_l[idx], arr_f[idx][::-1]
        if idx == 0:
            arr_u = func_rot(arr_u, '+')
        else:
            arr_d = func_rot(arr_d, '-')
        return
    arr_f[idx], arr_l[idx], arr_b[idx], arr_r[idx] \
        = arr_l[idx][::-1], arr_b[idx], arr_r[idx][::-1], arr_f[idx]
    if idx == 0:
        arr_u = func_rot(arr_u, '-')
    else:
        arr_d = func_rot(arr_d, '+')
    return
def func_d(rot):
    if rot == '+':
        func_u('-', -1)
        return
    func_u('+', -1)
    return
def func_r(rot, idx=-1):
    global arr_u, arr_f, arr_d, arr_b, arr_r, arr_l
    tmp = [[arr_f[i][idx] for i in range(3)],
           [arr_d[i][idx] for i in range(3)],
           [arr_b[i][idx] for i in range(3)],
           [arr_u[i][idx] for i in range(3)]]
    if rot == '+':
        for i in range(3):
            arr_u[i][idx], arr_f[i][idx], arr_d[i][idx], arr_b[i][idx] \
                = tmp[0][i], tmp[1][2 - i], tmp[2][i], tmp[3][2 - i]
        if idx == -1:
            arr_r = func_rot(arr_r, '+')
        else:
            arr_l = func_rot(arr_l, '-')
        return
    for i in range(3):
        arr_d[2 - i][idx], arr_b[i][idx], arr_u[2 - i][idx], arr_f[i][idx] \
            = tmp[0][i], tmp[1][i], tmp[2][i], tmp[3][i]
    if idx == -1:
        arr_r = func_rot(arr_r, '-')
    else:
        arr_l = func_rot(arr_l, '+')
    return
def func_l(rot):
    if rot == '+':
        func_r('-', 0)
        return
    func_r('+', 0)
    return
def func_f(rot, idx=2):
    global arr_u, arr_r, arr_d, arr_l, arr_f, arr_b
    tmp = [[arr_l[i][2 - idx] for i in range(3)],
           [arr_u[idx][i] for i in range(3)],
           [arr_r[i][2 - idx] for i in range(3)],
           [arr_d[idx][i] for i in range(3)]]
    if rot == '+':
        for i in range(3):
            arr_u[idx][2-i], arr_r[i][2-idx], arr_d[idx][i], arr_l[i][2-idx] \
                = tmp[0][i], tmp[1][i], tmp[2][2-i], tmp[3][i]
        if idx == 2:
            arr_f = func_rot(arr_f, '+')
        else:
            arr_b = func_rot(arr_b, '-')
        return
    for i in range(3):
        arr_d[idx][i], arr_l[2-i][2-idx], arr_u[idx][i], arr_r[2-i][2-idx] \
            = tmp[0][i], tmp[1][i], tmp[2][i], tmp[3][i]
    if idx == 2:
        arr_f = func_rot(arr_f, '-')
    else:
        arr_b = func_rot(arr_b, '+')
    return
def func_b(rot):
    if rot == '+':
        func_f('-', 0)
        return
    func_f('+', 0)
    return
# L- U- L+ U- L- U- U- L+ U+ U+
# func_l('-')
# func_u('-')
# func_l('+')
# func_u('-')
# print(*arr_l, '', *arr_f, '', *arr_r, '', *arr_b, sep='\n')
# func_l('-')
# func_u('-')
# func_u('-')
# func_l('+')
# print(*arr_r, '', sep='\n')
# func_u('+')
# func_u('+')
# exit()
f = {'U': func_u, 'D': func_d, 'F': func_f, 'B': func_b, 'L': func_l, 'R': func_r}
for _ in range(int(input())):
    input()
    for c in input().split():
        f[c[0]](c[1])
    for row in arr_u:
        print(*row, sep='')
    arr_u = [['w'] * 3 for _ in range(3)]
    arr_d = [['y'] * 3 for _ in range(3)]
    arr_l = [['g'] * 3 for _ in range(3)]
    arr_r = [['b'] * 3 for _ in range(3)]
    arr_f = [['r'] * 3 for _ in range(3)]
    arr_b = [['o'] * 3 for _ in range(3)]
"""
4
1
L-
2
F+ B+
4
U- D- L+ R+
10
L- U- L+ U- L- U- U- L+ U+ U+

1
10
L- U- L+ U- L- U- U- L+ U+ U+
"""
exit()

# BOJ - 17143
import sys
read = sys.stdin.readline
p, q, m = map(int, input().split())
dd = {}
for _ in range(m):
    a, b, c, d, e = map(int, read().split())
    dd.setdefault(b, {}).setdefault(a, [c, d, e])
ans = 0
row_front = list(range(p-1, 0, -1)) + list(range(2, p+1))
row_back = list(range(2, p)) + list(range(p, 0, -1))
col_front = list(range(q-1, 0, -1)) + list(range(2, q+1))
col_back = list(range(2, q)) + list(range(q, 0, -1))
for i in range(1, q+1):
    if len(dd.get(i, {})) > 0:
        ans += dd[i][min(dd[i])][-1]
        del dd[i][min(dd[i])]
    _dd = {}
    for col, v in dd.items():
        for row, l in v.items():
            s, d, z = l
            if d == 1:
                _dd.setdefault(col, {})
                if row - s >= 1:
                    _row = row - s
                else:
                    _, h = divmod(s - row + 1, len(row_back))
                    if h <= len(row_back) // 2: d = 2
                    _row = row_back[h-1]
                _l = [s, d, z]
                _col = col
            elif d == 2:
                _dd.setdefault(col, {})
                if s + row <= p:
                    _row = s + row
                else:
                    _, h = divmod(s + row - p, len(row_front))
                    if h <= len(row_front) // 2: d = 1
                    _row = row_front[h-1]
                _l = [s, d, z]
                _col = col
            elif d == 3:
                if s + col <= q:
                    _col = s + col
                else:
                    _, h = divmod(s + col - q, len(col_front))
                    if h <= len(col_front) // 2: d = 4
                    _col = col_front[h-1]
                _l = [s, d, z]
                _row = row
                _dd.setdefault(_col, {}).setdefault(_row, _l)
            else:
                if col - s >= 1:
                    _col = col - s
                else:
                    _, h = divmod(s - col + 1, len(col_back))
                    if h <= len(col_back) // 2: d = 3
                    _col = col_back[h-1]
                _l = [s, d, z]
                _row = row
                _dd.setdefault(_col, {}).setdefault(_row, _l)
            if _dd[_col].get(_row, (0, 0, 0))[-1] < _l[-1]:
                _dd[_col][_row] = _l
    dd = _dd
print(ans)
"""
4 6 8
4 1 3 3 8
1 3 5 2 9
2 4 8 4 1
4 5 0 1 4
3 3 1 2 7
1 5 8 4 3
3 6 2 1 2
2 2 2 3 5
"""