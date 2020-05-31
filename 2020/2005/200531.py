# BOJ - 15971
import sys
read = sys.stdin.readline
n, x, y = map(int, read().split())
arr = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, read().split())
    arr[a].append((b, c))
    arr[b].append((a, c))
q = [(x, 0, 0)]
visit = [True] * (n+1)
visit[x] = False
while q:
    tmp = []
    for a, b, c in q:
        if a == y: print(c - b);exit()
        for d, e in arr[a]:
            if visit[d]:
                visit[d] = False
                tmp.append((d, max(e, b), c + e))
    q = tmp
"""
5 1 5
1 2 1
2 3 2
3 4 3
4 5 4
"""
exit()

# BOJ - 1062
import re, string
from itertools import combinations
n, k = map(int, input().split())
if k < 5: print(0);exit()
if k == 26: print(n);exit()
pat = re.compile('[^antic]')
arr = [pat.findall(input()) for _ in range(n)]
ans = arr.count('')
arr = [a for a in arr if a != '']
s = set()
for a in arr:
    s.update(a)
if len(s) <= k-5: print(n);exit()
char = pat.findall(string.ascii_lowercase)
l = [False] * 26
def func(a):
    for aa in a:
        if not l[ord(aa) - 97]: return False
    return True
tmp = 0
for comb in combinations(s, k-5):
    tmp_tmp = 0
    l = [False] * 26
    for c in comb:
        l[ord(c) - 97] = True
    for a in arr:
        tmp_tmp += func(a)
    tmp = max(tmp, tmp_tmp)
print(ans + tmp)
"""
3 7
antazxtica
antaxytica
antayztica

3 7
antawxtica
antaytica
antaztica
"""
exit()

# BOJ - 1451
n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]
for i in range(n):
    for j, k in enumerate(map(int, input())):
        if i == 0:
            arr[i][j] = arr[i][j-1] + k
        elif j == 0:
            arr[i][j] = arr[i-1][j] + k
        else:
            arr[i][j] = arr[i-1][j] + arr[i][j-1] - arr[i-1][j-1] + k
ans = 0
for i in range(n-1):
    for j in range(m-1):
        ans = max(ans,
                  arr[i][j] * (arr[i][m-1] - arr[i][j]) * (arr[n-1][m-1] - arr[i][m-1]),
                  arr[i][j] * (arr[n-1][j] - arr[i][j]) * (arr[n-1][m-1] - arr[n-1][j]))
for i in range(n-2):
    for ii in range(i+1, n-1):
        ans = max(ans,
                  arr[i][m-1] * (arr[ii][m-1] - arr[i][m-1]) * (arr[n-1][m-1] - arr[ii][m-1]))
    for j in range(m-1):
        a = arr[i][m-1]
        b = arr[n-1][j] - arr[i][j]
        c = arr[n-1][m-1] - a - b
        ans = max(ans, a * b * c)
for j in range(m-2):
    for jj in range(j+1, m-1):
        ans = max(ans,
                  arr[n-1][j] * (arr[n-1][jj] - arr[n-1][j]) * (arr[n-1][m-1] - arr[n-1][jj]))
    for i in range(n-1):
        a = arr[n-1][j]
        b = arr[i][m-1] - arr[i][j]
        c = arr[n-1][m-1] - a - b
        ans = max(ans, a * b * c)
print(ans)
"""
1 8
11911103

3 3
123
456
789
"""
exit()

# BOJ - 1405
import sys
sys.setrecursionlimit(1000000)
n, a, b, c, d = map(int, input().split())
arr = [[True] * 29 for _ in range(29)]
arr[14][14] = False
a /= 100; b /= 100; c /= 100; d /= 100
def func(x, y):
    yield x, y+1, a
    yield x, y-1, b
    yield x+1, y, c
    yield x-1, y, d
def dfs(w, x, y, z):
    val = 0
    for xx, yy, ww in func(x, y):
        if arr[xx][yy]:
            arr[xx][yy] = False
            val += w * dfs(ww, xx, yy, z-1) if z > 1 else w * ww
            arr[xx][yy] = True
    return val
print(dfs(1, 14, 14, n))
"""
2 25 25 25 25
"""