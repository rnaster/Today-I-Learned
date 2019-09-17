# BOJ - 17140
from collections import Counter
r, c, k = map(int, input().split())
arr = [[*map(int, input().split())] for _ in range(3)]
def func1():
    global arr
    _arr = []
    nrow = 0
    for row in arr:
        counter = Counter(row)
        del counter[0]
        nrow = max(nrow, len(counter) * 2)
        l = []
        for key, value in sorted(counter.items(), key=lambda x: (x[1], x[0])):
            l.extend([key, value])
        _arr.append(l[:100])
    nrow = min(nrow, 100)
    for row in _arr:
        row.extend([0] * (nrow - len(row)))
    arr = _arr
    return
def func2():
    global arr
    _arr = []
    ncol = 0
    for j in range(len(arr[0])):
        counter = Counter([arr[i][j] for i in range(len(arr))])
        del counter[0]
        ncol = max(ncol, len(counter) * 2)
        l = []
        for key, value in sorted(counter.items(), key=lambda x: (x[1], x[0])):
            l.extend([key, value])
        _arr.append(l[:100])
    ncol = min(ncol, 100)
    for col in _arr:
        col.extend([0] * (ncol - len(col)))
    arr = [list(x) for x in zip(*_arr)]
    return
ans = 0
for _ in range(101):
    if len(arr) >= r and len(arr[0]) >= c and arr[r-1][c-1] == k:
        print(ans)
        exit()
    ans += 1
    if len(arr) < len(arr[0]):
        func2()
    else:
        func1()
print(-1)
"""
1 2 1
1 2 1
2 1 3
3 3 3

1 2 4
1 2 1
2 1 3
3 3 3

1 2 100
1 2 3
1 2 3
1 23 1

4 4 4
3 3 3
3 3 3
3 3 3

50 50 1
1 2 3
1 2 3
1 2 3
"""