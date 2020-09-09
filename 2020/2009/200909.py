# programmers - 2020 kakao intern
board = [[0,0,0,0,0,0,0,1],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,1,0,0],
         [0,0,0,0,1,0,0,0],
         [0,0,0,1,0,0,0,1],
         [0,0,1,0,0,0,1,0],
         [0,1,0,0,0,1,0,0],
         [1,0,0,0,0,0,0,0]]
board = [[0,0,1,0],
         [0,0,0,0],
         [0,1,0,1],
         [1,0,0,0]]
board = [[0, 0, 0, 0, 0, 0],
         [1, 1, 1, 1, 1, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 1, 1, 1, 1, 1],
         [0, 0, 1, 0, 0, 0],
         [1, 0, 0, 0, 1, 0]]
board = [[0, 1, 1],
         [0, 0, 1],
         [1, 0, 0]]
from heapq import *
def dist(b, c, d):
    if d == 0:
        yield b, c+1, 1, 600;yield b-1, c, 0, 100;yield b, c-1, 3, 600
    elif d == 1:
        yield b-1, c, 0, 600;yield b, c+1, 1, 100;yield b+1, c, 2, 600
    elif d == 2:
        yield b, c+1, 1, 600;yield b+1, c, 2, 100;yield b, c-1, 3, 600
    else:
        yield b+1, c, 2, 600;yield b, c-1, 3, 100;yield b-1, c, 0, 600
def solution(board):
    n = len(board)
    dp = [[[987654321] * 4 for _ in range(n)] for _ in range(n)]
    dp[0][0][1] = 0
    dp[0][0][2] = 0
    q = [(0, 0, 0, 1), (0, 0, 0, 2)]
    while q:
        a, b, c, d = heappop(q)
        for bb, cc, dd, ee in dist(b, c, d):
            if -1 < bb < n and -1 < cc < n \
                    and board[bb][cc] < 1 \
                    and dp[bb][cc][dd] > a + ee:
                dp[bb][cc][dd] = a + ee
                heappush(q, (a+ee, bb, cc, dd))
    return min(dp[-1][-1])
print(solution(board))
exit()

# BOJ - 2665
from heapq import *
n = int(input())
arr = [input() for _ in range(n)]
h = [(0, (0, 0))]
visit = [[True] * n for _ in range(n)]
def dist(a, b):
    yield a+1, b;yield a-1, b;yield a, b+1;yield a, b-1;
while h:
    a, (b, c) = heappop(h)
    if visit[b][c]: visit[b][c] = False
    else: continue
    for bb, cc in dist(b, c):
        if (bb, cc) == (n-1, n-1): print(a);exit()
        if -1 < bb < n and -1 < cc < n and visit[bb][cc]:
            if arr[bb][cc] == "1": heappush(h, (a, (bb, cc)))
            else: heappush(h, (a+1, (bb, cc)))
"""
8
11100110
11010010
10011010
11101100
01000111
00110001
11011000
11000111
"""
exit()

# BOJ - 8972
n, m = map(int, input().split())
arr = [[*input()] for _ in range(n)]
p, q = None, []
for i in range(n):
    for j in range(m):
        if arr[i][j] == "I": p = [i, j]
        elif arr[i][j] == "R": q.append([i, j])
cnt = 0
def move(a):
    global cnt
    if a == 1:
        p[0] += 1
        p[1] -= 1
    elif a == 2:
        p[0] += 1
    elif a == 3:
        p[0] += 1
        p[1] += 1
    elif a == 4:
        p[1] -= 1
    elif a == 6:
        p[1] += 1
    elif a == 7:
        p[0] -= 1
        p[1] -= 1
    elif a == 8:
        p[0] -= 1
    elif a == 9:
        p[0] -= 1
        p[1] += 1
    cnt += 1
for i in map(int, input()):
    arr[p[0]][p[1]] = "."
    move(i)
    if arr[p[0]][p[1]] == "R":
        print("kraj %s" % cnt)
        exit()
    arr[p[0]][p[1]] = "I"
    for j in range(len(q)):
        arr[q[j][0]][q[j][1]] = "."
        if p[0] == q[j][0]:
            if q[j][1] > p[1]: q[j][1] -= 1
            else: q[j][1] += 1
        elif p[1] == q[j][1]:
            if q[j][0] > p[0]: q[j][0] -= 1
            else: q[j][0] += 1
        elif p[0] < q[j][0] and p[1] < q[j][1]:
            q[j][0] -= 1
            q[j][1] -= 1
        elif p[0] < q[j][0] and p[1] > q[j][1]:
            q[j][0] -= 1
            q[j][1] += 1
        elif p[0] > q[j][0] and p[1] < q[j][1]:
            q[j][0] += 1
            q[j][1] -= 1
        else:
            q[j][0] += 1
            q[j][1] += 1
    for x, y in q:
        arr[x][y] += "R"
    tmp = []
    for x, y in q:
        t = arr[x][y].lstrip(".")
        if len(t) == 0: continue
        if len(t) == 1:
            arr[x][y] = t
            tmp.append([x, y])
        elif "I" in t:
            print("kraj %s" % cnt)
            exit()
        else:
            arr[x][y] = "."
    q = tmp
for a in arr:
    print(''.join(a))
"""
9 10
..........
.........R
..........
R.........
R...I.....
R.........
..........
.........R
....R.....
5558888

8 8
........
....R...
........
.......R
........
........
....I...
.......R
778524

12 7
R......
.......
.......
.......
.......
...I...
.......
.......
.......
.......
.......
R.....R
464453955134646

8 8
R......R
.R...RR.
..R..RR.
........
.....R..
......R.
....I...
.......R
1444
"""