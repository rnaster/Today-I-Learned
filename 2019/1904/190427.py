# BOJ - 15686
import itertools
n, m = map(int, input().split())
h, c = [], []
for i in range(n):
    temp = tuple(input().split())
    for j in range(n):
        if temp[j] == '1': h.append((i, j))
        elif temp[j] == '2': c.append((i, j))
def func(hh, cc):
    p, q = hh
    r, s = cc
    return abs(p-r) + abs(q-s)
ans = 987654321
for comb in itertools.combinations(range(len(c)), m):
    temp1 = 0
    for hh in h:
        temp2 = 987654321
        for i in comb:
            temp2 = min(temp2, func(hh, c[i]))
        temp1 += temp2
    ans = min(ans, temp1)
print(ans)
"""
5 3
0 0 1 0 0
0 0 2 0 1
0 1 2 0 0
0 0 1 0 0
0 0 0 0 2
"""
exit()

# BOJ - 7562
import sys
read = lambda: sys.stdin.readline().rstrip()
d = ((-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1))
def bfs(q, visit, a, b):
    ans = 0
    while q:
        temp = []
        for i in range(0, len(q), 2):
            x, y = q[i], q[i+1]
            if a == x and b == y: return ans
            for dx, dy in d:
                if -1 < x + dx < n and -1 < y + dy < n and visit[x+dx][y+dy] == 0:
                    visit[x+dx][y+dy] = 1
                    temp.extend([x+dx, y+dy])
        q = temp
        ans += 1
for _ in range(int(read())):
    n = int(read())
    visit = [[0] * n for _ in range(n)]
    q = [*map(int, read().split())]
    a, b = map(int, read().split())
    visit[q[0]][q[1]] = 1
    print(bfs(q, visit, a, b))
"""
3
8
0 0
7 0
100
0 0
30 50
10
1 1
1 1
"""