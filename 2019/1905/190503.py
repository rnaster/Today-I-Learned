# BOJ - 7569
import sys
read = lambda: sys.stdin.readline().rstrip()
m, n, h = map(int, read().split())
num = 0
visit = [[[0]*m for _ in range(n)] for _ in range(h)]
q = []
for i in range(h):
    for j in range(n):
        k = 0
        for t in map(int, read().split()):
            visit[i][j][k] = t
            if visit[i][j][k] == 1: q.append((i, j, k))
            elif visit[i][j][k] == 0: num += 1
            k += 1
d = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
ans = 0
while q:
    temp = []
    for z, x, y in q:
        for dx, dy, dz in d:
            if -1 < x+dx < n and -1 < y+dy < m and -1 < z+dz < h and visit[z+dz][x+dx][y+dy] == 0:
                visit[z+dz][x+dx][y+dy] = 1
                num -= 1
                temp.append((z+dz, x+dx, y+dy))
    ans += 1
    q = temp
if num == 0: print(ans-1)
else: print(-1)
"""
5 3 2
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 1 0 0
0 0 0 0 0
"""
sys.exit()

# BOJ - 7576
import sys
read = lambda: sys.stdin.readline().rstrip()
n, m = map(int, read().split())
visit = [list(map(int, read().split())) for _ in range(m)]
q = []
num = 0
for i in range(m):
    for j in range(n):
        if visit[i][j] == 1: q.append((i, j))
        elif visit[i][j] == 0: num += 1
ans = 0
d = ((1, 0), (-1, 0), (0, 1), (0, -1))
while q:
    temp = []
    for x, y in q:
        for dx, dy in d:
            if -1 < x+dx < m and -1 < y+dy < n and visit[x+dx][y+dy] == 0:
                visit[x+dx][y+dy] = 1
                num -= 1
                temp.append((x+dx, y+dy))
    ans += 1
    q = temp
if num == 0: print(ans-1)
else: print(-1)
"""
6 4
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1

6 4
0 -1 0 0 0 0
-1 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1
"""
sys.exit()

# BOJ - 11403
import collections
import sys
read = lambda: sys.stdin.readline().rstrip()
n = int(read())
visit = [list(read().split()) for _ in range(n)]
q = collections.deque()
for i in range(n):
    for j in range(n):
        if visit[i][j] == '1':
            q.append((i, j))
while q:
    x, y = q.pop()
    for i in range(n):
        if visit[y][i] == '1' and visit[x][i] == '0':
            visit[x][i] = '1'
            q.append((x, i))
for v in visit:
    print(*v)
"""
3
0 1 0
0 0 1
1 0 0

7
0 0 0 1 0 0 0
0 0 0 0 0 0 1
0 0 0 0 0 0 0
0 0 0 0 1 1 0
1 0 0 0 0 0 0
0 0 0 0 0 0 1
0 0 1 0 0 0 0
"""
sys.exit()

# BOJ - 1600
import sys
read = lambda: sys.stdin.readline().rstrip()
k = int(read())
w, h = map(int, read().split())
arr = [tuple(map(int, read().split())) for _ in range(h)]
visit = [[[0] * w for _ in range(h)] for _ in range(k+1)]; visit[0][0][0] = 1
q = [(0, 0, 0)]
d = ((1, 0), (-1, 0), (0, 1), (0, -1))
dd = ((-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1))
ans = 0
while q:
    temp = []
    for a, x, y in q:
        # if x == h-1 and y == w-1: print(ans);exit()
        for dx, dy in d:
            if -1 < x + dx < h and -1 < y + dy < w and arr[x+dx][y+dy] != 1 and visit[a][x+dx][y+dy] == 0:
                visit[a][x+dx][y+dy] = 1
                temp.append((a, x+dx, y+dy))
        for dx, dy in dd:
            if -1 < x + dx < h and -1 < y + dy < w and arr[x + dx][y + dy] != 1 and visit[a][x + dx][y + dy] == 0 and a < k:
                visit[a+1][x+dx][y+dy] = 1
                temp.append((a+1, x+dx, y+dy))
    q = temp
    ans += 1
    if sum([visit[i][-1][-1] for i in range(k+1)]) > 0: print(ans);exit()
print(-1)
"""
1
4 4
0 0 0 0
1 0 0 0
0 0 1 0
0 1 0 0
"""
sys.exit()

# BOJ - 2206
import sys
read = lambda: sys.stdin.readline().rstrip()
n, m = map(int, read().split())
arr = [read() for _ in range(n)]
visit = [[[0] * m for _ in range(n)] for _ in range(2)]; visit[0][0][0] = 1
q = [(0, 0, 0)]
d = ((1, 0), (-1, 0), (0, 1), (0, -1))
ans = 1
while q:
    temp = []
    for a, x, y in q:
        if x == n-1 and y == m-1: print(ans);exit()
        for dx, dy in d:
            if -1 < x + dx < n and -1 < y + dy < m and visit[a][x+dx][y+dy] == 0:
                if arr[x+dx][y+dy] == '1':
                    if a == 0:
                        visit[1][x+dx][y+dy] = 1
                        temp.append((1, x+dx, y+dy))
                else:
                    visit[a][x+dx][y+dy] = 1
                    temp.append((a, x+dx, y+dy))
    q = temp
    ans += 1
print(-1)
"""
6 4
0100
1110
1000
0000
0111
0000

4 4
0101
0101
0001
1110

3 6
010000
010111
000010

7 8
01000000
01111110
01100000
01101111
01100000
01111110
00000000

10 8
00000000
11111110
01111110
01100000
01101111
01101111
01100000
01111110
01111110
00000000

"""


"""
# Title: 벽 부수고 이동하기
# Link: https://www.acmicpc.net/problem/2206

import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))
read_list_str = lambda: list(sys.stdin.readline().strip())


def solution(n: int, m: int, game_map: list):
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visits = [[[-1 for _ in range(2)] for _ in range(m)] for _ in range(n)]

    queue = deque()
    queue.append((0, 0, False, 1))
    visits[0][0][0] = 1

    while queue:
        x, y, broken, step = queue.popleft()
        
        for move in moves:
            xx, yy = x + move[0], y + move[1]
            if 0 <= xx < m and 0 <= yy < n:
                if broken:
                    if game_map[yy][xx] == '0' and visits[yy][xx][1] == -1:
                        visits[yy][xx][1] = step+1
                        queue.append((xx, yy, True, step+1))
                elif not broken:
                    if game_map[yy][xx] == '0' and visits[yy][xx][0] == -1:
                        visits[yy][xx][0] = step+1
                        queue.append((xx, yy, False, step+1))
                    elif game_map[yy][xx] == '1' and visits[yy][xx][1] == -1:
                        visits[yy][xx][1] = step+1
                        queue.append((xx, yy, True, step+1))

    return max(visits[n-1][m-1]) if -1 in visits[n-1][m-1] else min(visits[n-1][m-1])


def main():
    N, M = read_list_int()
    game_map = []
    for _ in range(N):
        game_map.append(read_list_str())
    print(solution(N, M, game_map))


if __name__ == '__main__':
    main()
"""