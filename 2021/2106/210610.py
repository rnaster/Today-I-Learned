# BOJ - 2234
m, n = map(int, input().split())
arr = [[[0] * m for _ in range(n)] for _ in range(4)]
for i in range(n):
    for j, k in enumerate(map(int, input().split())):
        if k >= 8:
            arr[3][i][j] = 1
            k -= 8
        if k >= 4:
            arr[2][i][j] = 1
            k -= 4
        if k >= 2:
            arr[1][i][j] = 1
            k -= 2
        if k >= 1:
            arr[0][i][j] = 1
            k -= 1
def dist(a, b):
    yield a + 1, b, 1;
    yield a - 1, b, 3;
    yield a, b + 1, 0;
    yield a, b - 1, 2
ans1, ans2, ans3 = 0, 0, 0
cache = [[1] * m for _ in range(n)]
idx = 0
def is_available(xx, yy, d):
    if arr[d][xx][yy]: return 0
    return 1
ll = []
for i in range(n):
    for j in range(m):
        idx += 1
        if cache[i][j] < 1: continue
        cache[i][j] = 0
        ans1 += 1
        cnt = 0
        l = [(i, j)]
        t = []
        while l:
            tmp = []
            for x, y in l:
                t.append((x, y))
                cnt += 1
                for xx, yy, d in dist(x, y):
                    if -1 < xx < n \
                            and -1 < yy < m \
                            and is_available(xx, yy, d) \
                            and cache[xx][yy] > 0:
                        cache[xx][yy] = -i * m -j
                        tmp.append((xx, yy))
            l = tmp
        ll.append(t)
        cache[i][j] = cnt
        ans2 = max(ans2, cnt)
for lll in ll:
    for ii, jj in lll:
        if cache[ii][jj] <= 0:
            x1, y1 = divmod(-cache[ii][jj], m)
        else:
            x1, y1 = ii, jj
        cnt = cache[x1][y1]
        for xx, yy, d in dist(ii, jj):
            if -1 < xx < n \
                    and -1 < yy < m \
                    and not is_available(xx, yy, d):
                if cache[xx][yy] < 0:
                    x2, y2 = divmod(-cache[xx][yy], m)
                else:
                    x2, y2 = xx, yy
                if (x1, y1) != (x2, y2):
                    ans3 = max(ans3, cnt + cache[x2][y2])
print(ans1, ans2, ans3, sep='\n')
"""
7 4
11 6 11 6 3 10 6
7 9 6 13 5 15 5
1 10 12 7 13 7 5
13 11 10 8 10 12 13
"""
