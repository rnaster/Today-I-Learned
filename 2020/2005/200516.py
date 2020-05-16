# BOJ - 5427
import sys
read = sys.stdin.readline
n, m = 0, 0
arr = []
def dist(a, b):
    yield a+1, b; yield a-1, b; yield a, b+1; yield a, b-1
def bfs():
    visit = [[True] * n for _ in range(m)]
    ans = 0
    f = []
    q = []
    for i in range(m):
        for j in range(n):
            if arr[i][j] == '*':
                visit[i][j] = False
                for ii, jj in dist(i, j):
                    if -1 < ii < m and -1 < jj < n and visit[ii][jj]:
                        visit[ii][jj] = False
                        if arr[ii][jj] == '.':
                            f.append((ii, jj))
            elif arr[i][j] == '@':
                visit[i][j] = False
                q.append((i, j))
    while q:
        tmp = []
        for a, b in q:
            for aa, bb in dist(a, b):
                if aa in (-1, m) or bb in (-1, n): return ans + 1
                if visit[aa][bb]:
                    visit[aa][bb] = False
                    if arr[aa][bb] == '.':
                        tmp.append((aa, bb))
        tmp2 = []
        for a, b in f:
            for aa, bb in dist(a, b):
                if -1 < aa < m and -1 < bb < n and visit[aa][bb]:
                    visit[aa][bb] = False
                    if arr[aa][bb] == '.':
                        tmp2.append((aa, bb))
        q = tmp
        f = tmp2
        ans += 1
    return 0
for _ in range(int(input())):
    n, m = map(int, read().split())
    arr = [read().strip() for _ in range(m)]
    ans = bfs()
    if ans: print(ans)
    else: print('IMPOSSIBLE')
"""
5
4 3
####
#*@.
####
7 6
###.###
#*#.#*#
#.....#
#.....#
#..@..#
#######
7 4
###.###
#....*#
#@....#
.######
5 5
.....
.***.
.*@*.
.***.
.....
3 3
###
#@#
###
"""