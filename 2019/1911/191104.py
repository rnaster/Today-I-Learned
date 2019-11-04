# BOJ - 2174
a, b = map(int, input().split())
m, n = map(int, input().split())
robot = []
dd = {}
ddd = {'N': 0, 'E': 1, 'S': 2, 'W': 3}
for idx in range(m):
    i, j, d = input().split()
    robot.append([int(j)-1, int(i)-1, ddd[d]])
    dd[(int(j)-1, int(i)-1)] = idx
ddd = {0: (1, 0), 2: (-1, 0), 1: (0, 1), 3: (0, -1)}
for _ in range(n):
    i, c, j = input().split()
    i, j = int(i)-1, int(j)
    p, q, d = robot[i]
    if c == 'F':
        dx, dy = ddd[d]
        for jj in range(1, j+1):
            tmp = dd.get((p + jj * dx, q + jj * dy), -1)
            if tmp > -1:
                print('Robot %d crashes into robot %d' % (i+1, tmp+1))
                exit()
        if not (0 <= p+j*dx < a and 0 <= q + j*dy < b):
            print('Robot %d crashes into the wall' % (i+1))
            exit()
        else:
            dd[(p+j*dx, q+j*dy)] = i
            dd[(p, q)] = -1
            robot[i][:2] = [p + j*dx, q + j * dy]
    elif c == 'L':
        robot[i][-1] = (d - j) % 4
    else:
        robot[i][-1] = (d + j) % 4
print('OK')
exit()

# BOJ - 17837
n, k = map(int, input().split())
grid = [[*map(int, input().split())] for _ in range(n)]
arr = {}
prop = []
dd = ((0, 1), (0, -1), (-1, 0), (1, 0))
rev = {1: 2, 2: 1, 3: 4, 4: 3}
for i in range(k):
    a, b, c = map(int, input().split())
    arr[(a-1, b-1)] = [i]
    prop.append((a - 1, b - 1, c))
def func(j):
    a, b, c = prop[j]
    idx = arr[(a, b)].index(j)
    dx, dy = dd[c - 1]
    if grid[a+dx][b+dy] == 1:
        arr.setdefault((a+dx, b+dy), []).extend(arr[(a, b)][idx:][::-1])
    else:
        arr.setdefault((a + dx, b + dy), []).extend(arr[(a, b)][idx:])
    for jj in arr[(a, b)][idx:]:
        prop[jj] = (a + dx, b + dy, prop[jj][-1])
    del arr[(a, b)][idx:]
    return
for i in range(1, 1001):
    for j in range(k):
        a, b, c = prop[j]
        dx, dy = dd[c-1]
        if not (0 <= a + dx < n and 0 <= b + dy < n) or grid[a+dx][b+dy] == 2:
            prop[j] = (a, b, rev[c])
            if (0 <= a - dx < n and 0 <= b - dy < n) and grid[a-dx][b-dy] != 2:
                func(j)
        else:
            func(j)
        for _, v in arr.items():
            if len(v) > 3: print(i); exit()
print(-1)
"""
6 10
0 1 2 0 1 1
1 2 0 1 1 0
2 1 0 1 1 0
1 0 1 1 0 2
2 0 1 2 0 1
0 2 1 0 2 1
1 1 1
2 2 2
3 3 4
4 4 1
5 5 3
6 6 2
1 6 3
6 1 2
2 4 3
4 2 1
"""