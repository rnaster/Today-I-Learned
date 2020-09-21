# BOJ - 1613
import sys
read = sys.stdin.readline
n, k = map(int, read().split())
arr = [[False] * n for _ in range(n)]
q = []
for _ in range(k):
    a, b = map(int, read().split())
    arr[a-1][b-1] = True
    q.append((a-1, b-1))
while q:
    a, b = q.pop()
    for i in range(n):
        if arr[b][i] and not arr[a][i]:
            arr[a][i] = True
            q.append((a, i))
for _ in range(int(read())):
    a, b = map(int, read().split())
    if arr[a-1][b-1]: print(-1)
    elif arr[b-1][a-1]: print(1)
    else: print(0)
"""
5 5
1 2
1 3
2 3
3 4
2 4
3
1 5
2 4
3 1
"""
exit()

# BOJ - 1799
n = int(input())
arr = [[*map(int, input().split())] for _ in range(n)]
def func(a, b):
    x, y = divmod(a, n)
    if a == n*n -1:
        if arr[x][y] == 1:
            return b+1
        return b
    if arr[x][y] == 1:
        t1, t2 = min(n-x, n-y), min(y, n-x-1)
        l = [arr[x+i][y+i] for i in range(t1)]
        ll = [arr[x+i][y-i] for i in range(1, t2+1)]
        for i in range(t1):
            arr[x+i][y+i] = 0
        for i in range(1, t2+1):
            arr[x+i][y-i] = 0
        val = func(a+1, b+1)
        for i in range(t1):
            arr[x+i][y+i] = l[i]
        for i in range(1, t2+1):
            arr[x+i][y-i] = ll[i-1]
        return max(val, func(a+1, b))
    else:
        return func(a+1, b)
print(func(0, 0))
"""
5
1 1 0 1 1
0 1 0 0 0
1 0 1 0 1
1 0 0 0 0
1 0 1 1 1
"""