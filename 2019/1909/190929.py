# BOJ - 17142
from itertools import combinations
n, m = map(int, input().split())
arr = [[*map(int, input().split())] for _ in range(n)]
l = []
cnt = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] > 1: l.append((i, j))
        elif arr[i][j] < 1: cnt += 1
ans = 999999
d = ((0, 1), (0, -1), (1, 0), (-1, 0))
for comb in combinations(l, m):
    _ans = 0
    visit = [[0] * n for _ in range(n)]
    for x, y in comb:
        visit[x][y] = 1
    _cnt = 0
    _l = list(comb)
    while _l and _cnt < cnt:
        _l_ = []
        for x, y in _l:
            for dx, dy in d:
                if -1 < x + dx < n\
                        and -1 < y + dy < n\
                        and visit[x+dx][y+dy] < 1\
                        and arr[x+dx][y+dy] != 1:
                    _l_.append((x+dx, y+dy))
                    visit[x+dx][y+dy] = 1
                    if arr[x+dx][y+dy] == 0: _cnt += 1
        _l = _l_
        _ans += 1
    if _cnt == cnt:
        ans = min(ans, _ans)
if ans > 3000:
    print(-1)
else:
    print(ans)
"""
7 3
2 0 2 0 1 1 0
0 0 1 0 1 2 0
0 1 1 2 1 0 0
2 1 0 0 0 0 2
0 0 0 2 0 1 1
0 1 0 0 0 0 0
2 1 0 0 2 0 2
"""
exit()

# BOJ - 16953
a, b = map(int, input().split())
s = {a}
ans = 0
while s:
    _s = set()
    for i in s:
        if i == b: print(ans); exit()
        if i * 2 <= b:
            _s.add(i*2)
        if i * 10 + 1 <= b:
            _s.add(i*10 + 1)
    s = _s
    ans += 1
print(-1)
exit()

# BOJ - 17281
from itertools import permutations
n = int(input())
innings = [[*map(int, input().split())] for _ in range(n)]
def func(order):
    ans = 0
    i = 0
    for inning in innings:
        p, q, r = 0, 0, 0
        out = 0
        while out < 3:
            if inning[order[i]] == 0:
                out += 1
            elif inning[order[i]] == 1:
                ans += p
                p, q, r = q, r, 1
            elif inning[order[i]] == 2:
                ans += p + q
                p, q, r = r, 1, 0
            elif inning[order[i]] == 3:
                ans += p + q + r
                p, q, r = 1, 0, 0
            else:
                ans += p + q + r + 1
                p, q, r = 0, 0, 0
            i = (i+1) % 9
    return ans
ans = 0
for permu in permutations(range(1, 9), 8):
    order = list(permu[:3]) + [0] + list(permu[3:])
    ans = max(ans, func(order))
print(ans)
"""
2
4 3 2 1 0 4 3 2 1
1 2 3 4 1 2 3 4 0

2
4 0 0 0 1 1 1 0 0
0 0 0 0 0 0 0 0 0

9
4 4 4 4 4 4 4 4 0
4 4 4 4 4 4 4 4 0
4 4 4 4 4 4 4 4 0
4 4 4 4 4 4 4 4 0
4 4 4 4 4 4 4 4 0
4 4 4 4 4 4 4 4 0
4 4 4 4 4 4 4 4 0
4 4 4 4 4 4 4 4 0
4 4 4 4 4 4 4 4 0
"""