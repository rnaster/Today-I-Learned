# BOJ - 9328
import sys
read = sys.stdin.readline
def dist(a, b):
    yield a+1, b;yield a-1, b;yield a, b+1;yield a, b-1;
def func():
    n, m = map(int, read().split())
    arr = [read().strip() for _ in range(n)]
    l = read().strip()
    if l[0] == '0': l = ''
    ans = 0
    visit = [[True] * m for _ in range(n)]
    q = []
    door = [[] for _ in range(26)]
    key = [False] * 26
    for ll in l:
        key[ord(ll)-97] = True
    for i in range(n):
        t1 = ord(arr[i][0]) - 65
        visit[i][0] = False
        if arr[i][0] == ".":
            q.append((i, 0))
        elif arr[i][0] == "$":
            q.append((i, 0))
            ans += 1
        elif -1 < t1 < 26:
            if key[t1]:
                q.append((i, 0))
            else:
                door[t1].append((i, 0))
        t2 = ord(arr[i][m-1]) - 65
        visit[i][m-1] = False
        if arr[i][m-1] == ".":
            q.append((i, m-1))
        elif arr[i][m-1] == "$":
            q.append((i, m-1))
            ans += 1
        elif -1 < t2 < 26:
            if key[t2]:
                q.append((i, m-1))
            else:
                door[t2].append((i, m-1))
    for j in range(1, m-1):
        t1 = ord(arr[0][j]) - 65
        visit[0][j] = False
        if arr[0][j] == ".":
            q.append((0, j))
        elif arr[0][j] == "$":
            q.append((0, j))
            ans += 1
        elif -1 < t1 < 26:
            if key[t1]:
                q.append((0, j))
            else:
                door[t1].append((0, j))
        t2 = ord(arr[n-1][j]) - 65
        visit[n-1][j] = False
        if arr[n-1][j] == ".":
            q.append((n-1, j))
        elif arr[n-1][j] == "$":
            q.append((n-1, j))
            ans += 1
        elif -1 < t2 < 26:
            if key[t2]:
                q.append((n-1, j))
            else:
                door[t2].append((n-1, j))
    while q:
        tmp = []
        for a, b in q:
            for aa, bb in dist(a, b):
                if -1 < aa < n \
                        and -1 < bb < m \
                        and arr[aa][bb] != "*" \
                        and visit[aa][bb]:
                    visit[aa][bb] = False
                    t = ord(arr[aa][bb])
                    if arr[aa][bb] == ".":
                        tmp.append((aa, bb))
                    elif arr[aa][bb] == "$":
                        tmp.append((aa, bb))
                        ans += 1
                    elif -1 < t - 97 < 26:
                        tmp.append((aa, bb))
                        key[t-97] = True
                        tmp.extend(door[t-97])
                    elif key[t-65]:
                        tmp.append((aa, bb))
                    else:
                        door[t-65].append((aa, bb))
        q = tmp
    print(ans)
    return
for _ in range(int(read())):
    func()
"""
3
5 17
*****************
.............**$*
*B*A*P*C**X*Y*.X.
*y*x*a*p**$*$**$*
*****************
cz
5 11
*.*********
*...*...*x*
*X*.*.*.*.*
*$*...*...*
***********
0
7 7
*ABCDE*
X.....F
W.$$$.G
V.$$$.H
U.$$$.J
T.....K
*SQPML*
irony

1
4 7
$****$*
*Ba*A$*
..c*.B*
****.**
b
"""
exit()

# BOJ - 2539
import sys
read = sys.stdin.readline
n, m = map(int, read().split())
k = int(read())
kk = int(read())
arr = sorted([[*map(int, read().split())] for _ in range(kk)], key=lambda x: x[1])
def func(a):
    cnt = 0
    i = 1_000_001
    for x, y in arr:
        if x > a:
            return False
        if i <= y < i + a:
            pass
        else:
            cnt += 1
            i = y
    return cnt <= k
a, b = 0, max(n, m)
c = (a+b)//2
while a < c < b:
    if func(c):
        b = c
    else:
        a = c
    c = (a+b)//2
print(c+1)
"""
4 14
4
9
1 2
2 1
2 3
1 6
3 5
1 10
3 6
1 12
2 13
"""