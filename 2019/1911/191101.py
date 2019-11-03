# BOJ - 17822
n, m, t = map(int, input().split())
arr = [[*map(int, input().split())] for _ in range(n)]
dd = ((0, 1), (0, -1), (1, 0), (-1, 0))
def func():
    visit = [[0] * m for _ in range(n)]
    def bfs(q):
        a, b = q[0]
        val = arr[a][b]
        qq = q
        while q:
            _q = []
            for a, b in q:
                for dx, dy in dd:
                    a_, b_ = a + dx, (b+dy) % m
                    if 0 <= a_ < n and arr[a_][b_] == val and visit[a_][b_] < 1:
                        visit[a_][b_] = 1
                        _q.append((a_, b_))
            q = _q
            qq.extend(_q)
        return qq
    is_same = True
    for i in range(n):
        for j in range(m):
            if visit[i][j] < 1:
                visit[i][j] = 1
                if arr[i][j] == 0: continue
                qq = bfs([(i, j)])
                if len(qq) > 1:
                    is_same = False
                    for a, b in qq:
                        arr[a][b] = 0
    if is_same:
        n1 = sum([sum(a) for a in arr])
        n2 = sum([m - a.count(0) for a in arr])
        if n2 == 0: print(0); exit()
        mean = n1 / n2
        for i in range(n):
            for j in range(m):
                if arr[i][j] > mean:
                    arr[i][j] += -1
                elif 0 < arr[i][j] < mean:
                    arr[i][j] += 1
    return
for r in range(t):
    x, d, k = map(int, input().split())
    if m - k >= k:
        if d == 1:
            for i in range(x, n+1, x):
                arr[i-1] = arr[i-1][k:] + arr[i-1][:k]
        else:
            for i in range(x, n+1, x):
                arr[i-1] = arr[i-1][-k:] + arr[i-1][:-k]
    else:
        k = m - k
        if d == 1:
            for i in range(x, n + 1, x):
                arr[i - 1] = arr[i - 1][-k:] + arr[i - 1][:-k]
        else:
            for i in range(x, n+1, x):
                arr[i-1] = arr[i-1][k:] + arr[i-1][:k]
    func()
print(sum([sum(a) for a in arr]))
"""
4 4 1
1 1 2 3
5 2 4 2
3 1 3 5
2 1 3 2
2 0 1

4 4 2
1 1 2 3
5 2 4 2
3 1 3 5
2 1 3 2
2 0 1
3 1 3

4 4 3
1 1 2 3
5 2 4 2
3 1 3 5
2 1 3 2
2 0 1
3 1 3
2 0 2

6 6 4
8 4 3 5 5 11
6 8 4 6 5 5
8 11 9 5 5 5
3 5 1 1 2 4
9 5 7 11 8 1
11 4 10 11 7 4
5 0 1
5 0 5
7 0 4
7 0 1

"""
