# BOJ - 20057
n = int(input())
arr = [[*map(int, input().split())] for _ in range(n)]
ans = sum(sum(a) for a in arr)
x, y = n // 2, n // 2
d = 0
def func():
    val = 1
    while 1:
        yield val
        yield val
        val += 1
f = func()
ff = next(f)
for _ in range(n*n-1):
    v = 0
    if d == 0:
        y -= 1
        val = arr[x][y]
        if val > 0:
            for dx, dy, r in ((-1, 0, 0.07), (-2, 0, 0.02), (1, 0, 0.07), (2, 0, 0.02),
                              (-1, 1, 0.01), (1, 1, 0.01), (-1, -1, 0.1), (1, -1, 0.1),
                              (0, -2, 0.05)):
                t = int(val * r)
                v += t
                if -1 < x+dx < n and -1 < y+dy < n:
                    arr[x+dx][y+dy] += t
        if y-1 > -1:
            arr[x][y-1] += val - v
    elif d == 1:
        x += 1
        val = arr[x][y]
        if val > 0:
            for dx, dy, r in ((0, 1, 0.07), (0, -1, 0.07), (0, 2, 0.02), (0, -2, 0.02),
                              (-1, 1, 0.01), (1, 1, 0.1), (-1, -1, 0.01), (1, -1, 0.1),
                              (2, 0, 0.05)):
                t = int(val * r)
                v += t
                if -1 < x+dx < n and -1 < y+dy < n:
                    arr[x+dx][y+dy] += t
        if x+1 < n:
            arr[x+1][y] += val - v
    elif d == 2:
        y += 1
        val = arr[x][y]
        if val > 0:
            for dx, dy, r in ((-1, 0, 0.07), (-2, 0, 0.02), (1, 0, 0.07), (2, 0, 0.02),
                              (-1, 1, 0.1), (1, 1, 0.1), (-1, -1, 0.01), (1, -1, 0.01),
                              (0, 2, 0.05)):
                t = int(val * r)
                v += t
                if -1 < x + dx < n and -1 < y + dy < n:
                    arr[x + dx][y + dy] += t
        if y+1 < n:
            arr[x][y+1] += val - v
    else:
        x -= 1
        val = arr[x][y]
        if val > 0:
            for dx, dy, r in ((0, 1, 0.07), (0, -1, 0.07), (0, 2, 0.02), (0, -2, 0.02),
                              (1, -1, 0.01), (1, 1, 0.01), (-1, -1, 0.1), (-1, 1, 0.1),
                              (-2, 0, 0.05)):
                t = int(val * r)
                v += t
                if -1 < x + dx < n and -1 < y + dy < n:
                    arr[x + dx][y + dy] += t
        if x - 1 > -1:
            arr[x - 1][y] += val - v
    arr[x][y] = 0
    ff -= 1
    if ff == 0:
        ff = next(f)
        d = (d+1) % 4
val = sum(sum(a) for a in arr)
print(ans - val)
"""
5
0 0 0 0 0
0 0 0 0 0
0 100 0 0 0
0 0 0 0 0
0 0 0 0 0

7
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 100 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0

7
1 2 3 4 5 6 7
1 2 3 4 5 6 7
1 2 3 4 5 6 7
1 2 3 0 5 6 7
1 2 3 4 5 6 7
1 2 3 4 5 6 7
1 2 3 4 5 6 7

3
1000 1000 1000
1000 1000 1000
1000 1000 1000
"""