# BOJ - 7453
import sys
from collections import Counter
read = sys.stdin.readline
n = int(read())
arr = [[0] * n for _ in range(4)]
for i in range(n):
    arr[0][i], arr[1][i], arr[2][i], arr[3][i] = map(int, read().split())
c1 = Counter(arr[0][i] + arr[1][j] for i in range(n) for j in range(n))
c2 = Counter(arr[2][i] + arr[3][j] for i in range(n) for j in range(n))
ans = 0
for k, v in c1.items():
    if -k in c2:
        ans += v * c2[-k]
print(ans)
"""
6
-45 22 42 -16
-41 -27 56 30
-36 53 -37 77
-36 30 -75 -46
26 -38 -10 62
-32 -54 -6 45
"""
exit()

# BOJ - 18809
from itertools import combinations
n, m, g, r = map(int, input().split())
arr = [[*map(int, input().split())] for _ in range(n)]
l = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2: l.append((i, j))
def dist(a, b):
    yield a+1, b;yield a-1, b;yield a, b+1;yield a, b-1;
def func(a, b):
    l1 = [l[i] for i in a]
    l2 = [l[i] for i in b]
    visit = [[[-1, -1] for _ in range(m)] for _ in range(n)]
    ans = 0
    for i, j in l1 + l2:
        visit[i][j] = [0, 0]
    t = 1
    while l1 and l2:
        tmp1 = []
        for i, j in l1:
            for ii, jj in dist(i, j):
                if -1 < ii < n and -1 < jj < m \
                        and visit[ii][jj] == [-1, -1] \
                        and arr[ii][jj] > 0:
                    visit[ii][jj][0] = t
                    tmp1.append((ii, jj))
        tmp2 = []
        for i, j in l2:
            for ii, jj in dist(i, j):
                if -1 < ii < n and -1 < jj < m \
                        and visit[ii][jj][1] == -1 \
                        and visit[ii][jj][0] in [-1, t] \
                        and arr[ii][jj] > 0:
                    visit[ii][jj][1] = t
                    tmp2.append((ii, jj))
        tmp3 = []
        for i, j in tmp1:
            if visit[i][j][0] == visit[i][j][1] == t:
                ans += 1
            else:
                tmp3.append((i, j))
        l1 = tmp3
        l2 = [(i, j) for i, j in tmp2 if visit[i][j][0] != visit[i][j][1]]
        t += 1
    return ans
ans = 0
if r != g:
    for rr in combinations(range(len(l)), r):
        for gg in combinations([i for i in range(len(l)) if i not in rr], g):
            ans = max(ans, func(gg, rr))
else:
    for comb in combinations(range(len(l)), 2*r):
        for rr in combinations(comb, r):
            ans = max(ans, func([c for c in comb if c not in rr], rr))
print(ans)
"""
13 17 2 4
1 1 1 1 1 1 1 2 1 1 1 1 1 1 1 1 0
1 1 0 0 1 1 1 1 1 1 0 1 1 1 1 1 1
1 0 1 1 1 1 0 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 0 1 1 2 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 0 1 1 1
1 1 1 1 1 1 0 1 1 1 0 1 0 1 1 1 1
1 1 1 1 1 1 1 2 1 1 1 1 1 1 0 1 1
1 1 1 1 1 0 1 1 1 1 1 1 1 1 1 1 1
1 1 1 0 1 1 1 1 1 1 1 1 1 1 1 1 1
2 1 1 1 1 1 2 1 1 1 1 2 1 1 1 1 1
2 1 1 1 1 1 1 1 1 1 1 1 1 1 2 1 1
"""