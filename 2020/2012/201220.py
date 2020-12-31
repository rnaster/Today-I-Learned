# BOJ - 20056
n, m, k = map(int, input().split())
arr1 = [[0] * n for _ in range(n)]
arr2 = [[(0, 0, 0, -1)] * n for _ in range(n)]
def func(r, c, s, d):
    if d == 0:
        r, c = r-s, c
    elif d == 1:
        r, c = r-s, c+s
    elif d == 2:
        r, c = r, c+s
    elif d == 3:
        r, c = r+s, c+s
    elif d == 4:
        r, c = r+s, c
    elif d == 5:
        r, c = r+s, c-s
    elif d == 6:
        r, c = r, c-s
    else:
        r, c = r-s, c-s
    return r % n, c % n
def func2(a, d):
    if a == -1:
        return d % 2
    if a == 2:
        return a
    if d % 2 == a:
        return a
    return 2
l = [map(int, input().split()) for _ in range(m)]
dd = (0, 2, 4, 6)
for _ in range(k):
    while l:
        r, c, m, s, d = l.pop()
        r, c = func(r-1, c-1, s, d)
        arr2[r][c] = (arr2[r][c][0] + m, arr2[r][c][1] + s, d, func2(arr2[r][c][-1], d))
        arr1[r][c] += 1
    for i in range(n):
        for j in range(n):
            if arr1[i][j] == 0: continue
            if arr1[i][j] == 1:
                m, s, d, _ = arr2[i][j]
                l.append((i+1, j+1, m, s, d))
            elif arr2[i][j][0] > 4:
                m = arr2[i][j][0] // 5
                s = arr2[i][j][1] // arr1[i][j]
                if arr2[i][j][-1] == 2:
                    for d in dd:
                        l.append((i+1, j+1, m, s, d+1))
                else:
                    for d in dd:
                        l.append((i+1, j+1, m, s, d))
            arr1[i][j] = 0
            arr2[i][j] = (0, 0, 0, -1)
ans = 0
for _, _, m, _, _ in l:
    ans += m
print(ans)
"""
4 2 1
1 1 5 2 2
1 4 7 1 6

4 2 3
1 1 5 2 2
1 4 7 1 6
"""