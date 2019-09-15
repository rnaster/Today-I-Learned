# BOJ - 15683
from copy import deepcopy as copy
n, m = map(int, input().split())
arr = [[*map(int, input().split())] for _ in range(n)]
d = {1: (((0, 1),), ((0, -1),), ((1, 0),), ((-1, 0),)),
     2: (((0, 1), (0, -1)), ((-1, 0), (1, 0))),
     3: (((0, 1), (1, 0)), ((1, 0), (0, -1)), ((0, -1), (-1, 0)), ((-1, 0), (0, 1))),
     4: (((0, 1), (1, 0), (0, -1)), ((1, 0), (0, -1), (-1, 0)), ((0, -1), (-1, 0), (0, 1)), ((-1, 0), (0, 1), (1, 0))),
     5: (((0, 1), (1, 0), (0, -1), (-1, 0)),)}
l = []
for i in range(n):
    for j in range(m):
        if 0 < arr[i][j] < 6:
            l.append((i, j))
def main(arr, l):
    if len(l) < 1:
        return sum([1 for row in arr for r in row if r < 1])
    ans = 999
    a, b = l[0]
    for dd in d[arr[a][b]]:
        _arr = copy(arr)
        for dx, dy in dd:
            c = 1
            while -1 < a + dx * c < n and -1 < b + dy * c < m:
                if _arr[a+dx * c][b + dy * c] > 5: break
                if _arr[a+dx*c][b+dy*c] < 1:
                    _arr[a+dx*c][b+dy*c] = 1.5
                c += 1
        ans = min(ans, main(_arr, l[1:]))
    return ans
print(main(arr, l))
"""
6 6
0 0 0 0 0 0
0 2 0 0 0 0
0 0 0 0 6 0
0 6 0 0 2 0
0 0 0 0 0 0
0 0 0 0 0 5
"""