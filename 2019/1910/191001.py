# BOJ - 17406
from copy import deepcopy as copy
n, m, k = map(int, input().split())
arr = [[*map(int, input().split())] for _ in range(n)]
l = [[*map(int, input().split())] for _ in range(k)]
def _func_(_arr):
    a, b = len(_arr), len(_arr[0])
    for i in range(min(a // 2, b // 2)):
        tmp0 = _arr[i][b-i-1]
        tmp1 = _arr[-i-1][i]
        _arr[i][i+1:b-i] = _arr[i][i:-1-i]
        _arr[-i-1][i:-1-i] = _arr[-i-1][i+1:b-i]
        for j in range(i+1, a-(i+1)):
            _arr[j][b-i-1], tmp0 = tmp0, _arr[j][b-i-1]
        _arr[a-i-1][b-i-1] = tmp0
        for j in range(a-i-2, i, -1):
            _arr[j][i], tmp1 = tmp1, _arr[j][i]
        _arr[i][i] = tmp1
    return _arr
def _func(_arr, _l):
    r, c, s = _l
    _arr_ = _func_([_arr[i][c-s-1: c+s]
                    for i in range(r-s-1, r+s)])
    _i = 0
    for i in range(r-s-1, r+s):
        _j = 0
        for j in range(c-s-1, c+s):
            _arr[i][j] = _arr_[_i][_j]
            _j += 1
        _i += 1
    return _arr
def func(visit, _arr):
    if len(visit) == k:
        ans = 99999999
        for row in _arr:
            ans = min(ans, sum(row))
        return ans
    ans = 9999999999
    for i, _l in enumerate(l):
        if str(i) not in visit:
            _arr_ = _func(copy(_arr), _l)
            ans = min(ans, func(visit + '%s' % i, _arr_))
    return ans
print(func('', arr))
"""
5 6 2
1 2 3 2 5 6
3 8 7 2 1 3
8 2 3 1 4 5
3 4 5 1 1 1
9 3 2 1 4 3
3 4 2
4 2 1
"""