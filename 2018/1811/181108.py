# BOJ - 3101
n, k = map(int, input().split())
jump = tuple(input())
T = {'R': (1, 1), 'D': (1, 0), 'L': (-1, -1), 'U': (-1, 0)}
M = {'R': (1, 0), 'U': (-1, 0), 'L': (-1, -1), 'D': (1, -1)}
B = {'U': (-1, 1), 'L': (-1, 0), 'D': (1, -1), 'R': (1, 0)}
x, y = 0, 0
ans = 1
for j in jump:
    if x < n-1:
        dx, dy = T[j]
    elif x == n-1:
        dx, dy = M[j]
    else:
        dx, dy = B[j]
    x, y = x + dx, y + dy
    if x <= n - 1:
        x_ = x*(x+1) // 2 + 1
        if x % 2:
            ans += x_ + x - y
        else:
            ans += x_ + y
    else:
        x_ = n*n - (2*n - x - 1)*(2*n - x) // 2 + 1
        if x % 2:
            ans += x_ + 2*n-x-1-y-1
        else:
            ans += x_ + y
print(ans)
"""
6 8
DDRRUULL
4 8
RRRDDDUL
"""