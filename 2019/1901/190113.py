# BOj - 2342
from sys import setrecursionlimit
setrecursionlimit(1000000)
dp = [[-1]*100001 for _ in range(2)]
def dist(x, y):
    if x == 0: return 2
    if abs(x-y) in (1, 3): return 3
    if abs(x-y) == 2: return 4
    return 1
tp = tuple(map(int, input().split()))
w = len(tp)
def main(a, b):
    print(a, b)
    if a == w:
        dp[0][w] = 0
        return 0
    elif b == w:
        dp[1][w] = 0
        return 0
    else:
        c = max(a, b)
        L = main(c+1, b) if dp[c+1][b] == -1 else dp[c+1][b]
        L += dist(tp[a], tp[c+1])
        R = main(a, c+1) if dp[a][c+1] == -1 else dp[a][c+1]
        R += dist(tp[b], tp[c+1])
        dp[a][b] = min(L, R)
        return dp[a][b]
print(main(0, 0))
"""
1 2 2 4 0
"""
exit()

# BOJ - 2618
from sys import stdin, stdout, setrecursionlimit
setrecursionlimit(1000000)
read = lambda: stdin.readline().rstrip()
write = lambda x: stdout.write(str(x)+'\n')
n = int(input())
w = int(input())
l = [(-1, -1)]
for _ in range(w):
    l.append(tuple(map(int, read().split())))
dp = [[-1]*(w+1) for _ in range(w+1)]
ll = [0]*w
def L_dist(a, b):
    x, y = l[a]
    if a == 0: x, y = 1, 1
    p, q = l[b]
    return abs(x - p) + abs(q - y)
def R_dist(a, b):
    x, y = l[a]
    if a == 0: x, y = n, n
    p, q = l[b]
    return abs(x-p) + abs(q-y)
def main(x, y):
    print(x, y)
    if x == w or y == w:
        dp[x][y] = 0
        return 0
    else:
        z = max(x, y)
        L = main(z+1, y) if dp[z+1][y] == -1 else dp[z+1][y]
        L += L_dist(x, z+1)
        R = main(x, z+1) if dp[x][z+1] == -1 else dp[x][z+1]
        R += R_dist(y, z+1)
        ll[z] = 1 if L < R else 2
        dp[x][y] = min(L, R)
        return dp[x][y]
print(main(0, 0))
# print(*dp, sep='\n')
# for i in ll:
#     write(i)
"""
6
3
3 5
5 5
2 3
"""
exit()

# BOJ - 2666
n = int(input())
a, b = map(int, input().split())
c = int(input())
l = [-1]
for _ in range(c):
    l.append(int(input()))
dp = [[[-1]*(c+1) for _ in range(n+1)] for _ in range(n+1)]
def main(x, y, z):
    if z == c:
        dp[x][y][z] = 0
        return dp[x][y][z]
    else:
        L = main(l[z+1], y, z+1) if dp[l[z+1]][y][z+1] == -1 else dp[l[z+1]][y][z+1]
        L += abs(x-l[z+1])
        R = main(x, l[z+1], z+1) if dp[x][l[z+1]][z+1] == -1 else dp[x][l[z+1]][z+1]
        R += abs(y-l[z+1])
        dp[x][y][z] = min(L, R)
    return dp[x][y][z]
print(main(a, b, 0))
"""
7
2 5
4
3
1
6
5
"""