# BOJ - 17135
from itertools import combinations
from copy import deepcopy as copy
n, m, d = map(int, input().split())
arr = [[*map(int, input().split())] for _ in range(n)]
idx = [(n+1, i) for i in range(1, m+1)]
def dist(p, q):
    return abs(p[0] - q[0]) + abs(p[1] - q[1])
ans = 0
for comb in combinations(idx, 3):
    _ans = 0
    _arr = copy(arr)
    for k in range(n):
        a, b, c = (None, 9999), (None, 9999), (None, 9999)
        _comb = [(i-k, j) for i, j in comb]
        for j in range(1, m+1):
            for i in range(1, len(_arr)+1):
                if _arr[i-1][j-1] > 0:
                    if dist(_comb[0], (i, j)) <= d and dist(_comb[0], (i, j)) < a[1]:
                        a = ((i-1, j-1), dist(_comb[0], (i, j)))
                    if dist(_comb[1], (i, j)) <= d and dist(_comb[1], (i, j)) < b[1]:
                        b = ((i-1, j-1), dist(_comb[1], (i, j)))
                    if dist(_comb[2], (i, j)) <= d and dist(_comb[2], (i, j)) < c[1]:
                        c = ((i-1, j-1), dist(_comb[2], (i, j)))
        if a[0]:
            _ans += _arr[a[0][0]][a[0][1]]
            _arr[a[0][0]][a[0][1]] = 0
        if b[0]:
            _ans += _arr[b[0][0]][b[0][1]]
            _arr[b[0][0]][b[0][1]] = 0
        if c[0]:
            _ans += _arr[c[0][0]][c[0][1]]
            _arr[c[0][0]][c[0][1]] = 0
        _arr.pop()
    ans = max(ans, _ans)
print(ans)
"""
6 5 1
1 0 1 0 1
0 1 0 1 0
1 1 0 0 0
0 0 0 1 1
1 1 0 1 1
0 0 1 0 0
"""
exit()

# BOJ - 11729
n = int(input())
d = {(1, 2): 3, (1, 3): 2, (2, 3): 1}
l = []
def func(a, b, c):
    global l
    if a == 1:
        l.append((b, c))
        return 1
    dd = d[(min(b, c), max(b, c))]
    p = func(a-1, b, dd)
    l.append((b, c))
    q = func(a-1, dd, c)
    return p + 1 + q
print(func(n, 1, 3))
for ll in l:
    print(*ll)
"""
3
"""
exit()

# BOJ - 3190
from collections import deque
n = int(input())
arr = [[0] * n for _ in range(n)]
apple = {}
for _ in range(int(input())):
    a, b = map(int, input().split())
    apple[(a-1, b-1)] = 1
snake = deque([(0, 0), (0, 1)])
arr[0][0] = 1
arr[0][1] = 1
ans = 0
d = 1
dd = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}
ddd = {0: {'L': 3, 'D': 1},
       1: {'L': 0, 'D': 2},
       2: {'L': 1, 'D': 3},
       3: {'L': 2, 'D': 0}}
for _ in range(int(input())):
    a, b = input().split()
    a = int(a)
    while ans < a:
        print(snake, ans, d)
        x, y = snake.pop()
        dx, dy = dd[d]
        if d == 0:
            if -1 < x + dx and arr[x+dx][y+dy] < 1:
                if (x+dx, y+dy) not in apple:
                    x_, y_ = snake.popleft()
                    arr[x_][y_] = 0
                else:
                    del apple[(x + dx, y + dy)]
                arr[x + dx][y + dy] = 1
                snake.extend([(x, y), (x + dx, y + dy)])
            else:
                print(ans+1); exit()
        elif d == 1:
            if y + dy < n and arr[x+dx][y+dy] < 1:
                if (x+dx, y+dy) not in apple:
                    x_, y_ = snake.popleft()
                    arr[x_][y_] = 0
                else:
                    del apple[(x + dx, y + dy)]
                arr[x + dx][y + dy] = 1
                snake.extend([(x, y), (x + dx, y + dy)])
            else:
                print(ans+1); exit()
        elif d == 2:
            if x + dx < n and arr[x+dx][y+dy] < 1:
                if (x+dx, y+dy) not in apple:
                    x_, y_ = snake.popleft()
                    arr[x_][y_] = 0
                else:
                    del apple[(x + dx, y + dy)]
                arr[x + dx][y + dy] = 1
                snake.extend([(x, y), (x + dx, y + dy)])
            else:
                print(ans+1); exit()
        else:
            if -1 < y + dy and arr[x+dx][y+dy] < 1:
                if (x+dx, y+dy) not in apple:
                    x_, y_ = snake.popleft()
                    arr[x_][y_] = 0
                else:
                    del apple[(x + dx, y + dy)]
                arr[x + dx][y + dy] = 1
                snake.extend([(x, y), (x + dx, y + dy)])
            else:
                print(ans+1); exit()
        ans += 1
    d = ddd[d][b]

while True:
    x, y = snake.pop()
    dx, dy = dd[d]
    if d == 0:
        if -1 < x + dx and arr[x + dx][y + dy] < 1:
            if (x+dx, y+dy) not in apple:
                x_, y_ = snake.popleft()
                arr[x_][y_] = 0
            else:
                del apple[(x+dx, y+dy)]
            arr[x + dx][y + dy] = 1
            snake.extend([(x, y), (x + dx, y + dy)])
        else:
            print(ans)
            break
    elif d == 1:
        if y + dy < n and arr[x + dx][y + dy] < 1:
            if (x+dx, y+dy) not in apple:
                x_, y_ = snake.popleft()
                arr[x_][y_] = 0
            else:
                del apple[(x + dx, y + dy)]
            arr[x + dx][y + dy] = 1
            snake.extend([(x, y), (x + dx, y + dy)])
        else:
            print(ans)
            break
    elif d == 2:
        if x + dx < n and arr[x + dx][y + dy] < 1:
            if (x+dx, y+dy) not in apple:
                x_, y_ = snake.popleft()
                arr[x_][y_] = 0
            else:
                del apple[(x + dx, y + dy)]
            arr[x + dx][y + dy] = 1
            snake.extend([(x, y), (x + dx, y + dy)])
        else:
            print(ans)
            break
    else:
        if -1 < y + dy and arr[x + dx][y + dy] < 1:
            if (x+dx, y+dy) not in apple:
                x_, y_ = snake.popleft()
                arr[x_][y_] = 0
            else:
                del apple[(x + dx, y + dy)]
            arr[x + dx][y + dy] = 1
            snake.extend([(x, y), (x + dx, y + dy)])
        else:
            print(ans)
            break
    ans += 1
"""
2
1
2 2
1
1 L

2
0
5
0 D
1 D
2 D
3 D
4 D

6
3
3 4
2 5
5 3
3
3 D
15 L
17 D

10
4
1 2
1 3
1 4
1 5
4
8 D
10 D
11 D
13 L

10
5
1 5
1 3
1 2
1 6
1 7
4
8 D
10 D
11 D
13 L
"""