# BOJ - 2618
from sys import stdin
from array import array
read = lambda: stdin.readline().rstrip()
ans = array('L', [])
def f(X, Y): return abs(X[0] - Y[0]) + abs(X[1] - Y[1])
def f_(X):
    global dp1, dp2, coord_1, coord_2, ans
    if dp1[1] < dp2[1]: ans.append(1); coord_1 = X
    else: ans.append(2); coord_2 = X
n = int(read())
w = int(read())
coord_1, coord_2 = (1, 1), (n, n)
c0 = tuple(map(int, read().split()))
dp1, dp2 = (0, f(coord_1, c0)), (0, f(coord_2, c0))
f_(c0)
for _ in range(w-1):
    c1 = tuple(map(int, read().split()))
    dp1, dp2 = (dp1[1], min(dp2[1] + f(coord_1, c1), dp1[1] + f(c0, c1))), \
               (dp2[1], min(dp1[1] + f(coord_2, c1), dp2[1] + f(c0, c1)))
    f_(c1); c0 = c1
print(min(dp1[1], dp2[1]))
for i in ans:
    print(i)
'''
6
3
3 5
5 5
2 3
100
4
1 1
1 1
1 1
1 1
'''