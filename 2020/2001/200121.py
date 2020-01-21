# BOJ - 2805
from bisect import bisect
n, m = map(int, input().split())
arr = sorted(map(int, input().split()))
a, b = 0, max(arr)
c = (a+b) // 2
i = bisect(arr, c)
s = sum(arr[i:])
while a < c < b:
    _s = s - (n-i) * c
    if _s == m:
        break
    elif _s > m:
        a = c
        c = (a + b) // 2
        _i = bisect(arr, c, i, n)
        s -= sum(arr[i:_i])
    else:
        b = c
        c = (a+b) // 2
        _i = bisect(arr, c, 0, i)
        s += sum(arr[_i:i])
    i = _i
print(c)
"""
4 7
20 15 10 17

4 7
2 2 2 3
"""