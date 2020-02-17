# BOJ - 3190
from collections import deque
n = int(input())
arr = [[0] * n for _ in range(n)]
for _ in range(int(input())):
    a, b = map(int, input().split())
    arr[a-1][b-1] = 1
arr[0][0] = 2
q = deque([(0, 0)])
ans = 0
d = ((0, 1), (1, 0), (0, -1), (-1, 0))
dd = 0
a_ = 0
for _ in range(int(input())):
    a, b = input().split()
    a = int(a)
    dx, dy = d[dd]
    for _ in range(a - a_):
        x, y = q[-1]
        ans += 1
        if -1 < x + dx < n and -1 < y + dy < n and arr[x+dx][y+dy] < 2:
            if arr[x+dx][y+dy] < 1:
                x_, y_ = q.popleft()
                arr[x_][y_] = 0
            arr[x+dx][y+dy] = 2
            q.append((x+dx, y+dy))
        else:
            print(ans);exit()
    dd = (dd - 1) % 4 if b == 'L' else (dd + 1) % 4
    a_ = a
dx, dy = d[dd]
while 1:
    x, y = q[-1]
    ans += 1
    if -1 < x + dx < n and -1 < y + dy < n and arr[x + dx][y + dy] < 2:
        if arr[x + dx][y + dy] < 1:
            x_, y_ = q.popleft()
            arr[x_][y_] = 0
        arr[x + dx][y + dy] = 2
        q.append((x + dx, y + dy))
    else:
        print(ans)
        break
"""
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

6
3
3 4
2 5
5 3
3
3 D
15 L
17 D
"""