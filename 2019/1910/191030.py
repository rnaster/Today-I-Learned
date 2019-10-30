# BOJ - 17780
n, k = map(int, input().split())
grid = [[*map(int, input().split())] for _ in range(n)]
arr = {}
prop = []
dd = ((0, 1), (0, -1), (-1, 0), (1, 0))
rev = {1: 2, 2: 1, 3: 4, 4: 3}
for i in range(k):
    a, b, c = map(int, input().split())
    arr[(a-1, b-1)] = [i]
    prop.append((a - 1, b - 1, c))
def func(a, b, c):
    dx, dy = dd[c - 1]
    if grid[a+dx][b+dy] == 1:
        arr.setdefault((a+dx, b+dy), []).extend(arr[(a, b)][::-1])
    else:
        arr.setdefault((a + dx, b + dy), []).extend(arr[(a, b)])
    for j in arr[(a, b)]:
        prop[j] = (a + dx, b + dy, prop[j][-1])
    arr[(a, b)] = []
    return
for i in range(1, 1001):
    for j in range(k):
        a, b, c = prop[j]
        if arr[(a, b)].index(j) > 0: continue
        dx, dy = dd[c-1]
        if not (0 <= a + dx < n and 0 <= b + dy < n) or grid[a+dx][b+dy] == 2:
            prop[j] = (a, b, rev[c])
            if (0 <= a - dx < n and 0 <= b - dy < n) and grid[a-dx][b-dy] != 2:
                func(*prop[j])
        else:
            func(*prop[j])
    for _, v in arr.items():
        if len(v) > 3: print(i); exit()
print(-1)
"""
4 4
0 0 2 0
0 0 1 0
0 0 1 2
0 2 0 0
2 1 1
3 2 3
2 2 1
4 1 2

4 4
0 0 2 0
0 0 1 0
0 0 1 2
0 2 0 0
2 1 1
3 2 3
2 2 1
4 1 3
"""