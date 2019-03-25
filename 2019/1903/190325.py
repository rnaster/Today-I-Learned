# BOJ - 5212
n, m = map(int, input().split())
arr = [input() for _ in range(n)]
ans = [['X']*m for _ in range(n)]
row, col = [0]*n, [0]*m
for i in range(n):
    x = 0
    for j in range(m):
        if arr[i][j] == 'X':
            a = 0
            for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                if -1 < i+dx < n and -1 < j+dy < m:
                    a += 1 if arr[i+dx][j+dy] == '.' else 0
                else: a += 1
            if a > 2: ans[i][j] = '.'
            else: x += 1; col[j] += 1
        else: ans[i][j] = '.'
    if x > 0: row[i] = 1
p, q, r, s = 0, 0, n, m
for rr in row:
    if rr < 1: p += 1
    else: break
for rr in row[::-1]:
    if rr < 1: r -= 1
    else: break
for c in col:
    if c < 1: q += 1
    else: break
for c in col[::-1]:
    if c < 1: s -= 1
    else: break
for aa in ans[p:r]:
    print(*aa[q:s], sep='')
"""
3 10
..........
..XXX.XXX.
XXX.......
"""
exit()

# BOJ - 2823
n, m = map(int, input().split())
arr = [input() for _ in range(n)]
for i in range(n):
    for j in range(m):
        a = 0
        if arr[i][j] == '.':
            for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                if -1 < i+dx < n and -1 < j+dy < m:
                    a += 1 if arr[i+dx][j+dy] == '.' else 0
            if a < 2: print(1);exit()
print(0)
"""
4 3
XXX
X.X
X.X
XXX

2 3
...
X..

3 9
...XXX...
.X.....X.
...XXX...
"""