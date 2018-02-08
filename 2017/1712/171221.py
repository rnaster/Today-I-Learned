# BOJ - 2490
from sys import stdin, stdout
read = lambda: stdin.readline().rstrip()
def BOJ2490():
    t = ('D', 'C', 'B', 'A', 'E')
    for _ in range(3):
        tp = tuple(map(int, read().split()))
        print(t[sum(tp)])
    '''
    0 1 0 1
    1 1 1 0
    0 0 1 1
    '''
# BOJ - 1022
r1, c1, r2, c2 = map(int, read().split())
N = max(map(abs, [r1, c1, r2, c2])) * 2 + 1
arr = [[0 for _ in range(N)] for _ in range(N)]
x = (N-1) // 2
y = (N-1) // 2
n, t, c, m = 1, 0, 0, 1
d = ((0, 1), (-1, 0), (0, -1), (1, 0))
print('i', ' x ', 'y ', ' n', ' m ', 't', 'c')
for i in range(1, N+1):
    print(i, (x, y), (n, m), t, c)
    arr[x][y] = i
    dx, dy = d[t % 4]
    x, y = x+dx, y+dy
    if n < m:
        n += 1
    else:
        n = 0
        m += c
        c = 1 - c
    if n == 0: t += 1

from pprint import pprint
pprint(arr)

'''
-3 -3 2 0
'''
