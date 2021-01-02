# BOJ - 20058
n, q = map(int, input().split())
nn = 2 ** n
arr1 = [[*map(int, input().split())] for _ in range(nn)]
arr2 = [[0] * nn for _ in range(nn)]
for i in range(nn):
    for j in range(nn):
        arr2[i][j] = arr1[i][j]
arr3 = [[4] * nn for _ in range(nn)]
for l in map(int, input().split()):
    if l > 0:
        ll = 2 ** l
        f = 2 ** (n-l)
        a, b = 0, 0
        for _ in range(f):
            for _ in range(f):
                for i in range(ll):
                    for j in range(ll):
                        arr2[a + j][b + ll - i - 1] = arr1[a + i][b + j]
                b += ll
            a += ll
            b = 0
    for i in range(nn):
        for j in range(nn):
            if arr2[i][j] == 0:
                for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    if -1 < i+dx < nn and -1 < j+dy < nn:
                        arr3[i+dx][j+dy] -= 1
    for i in range(1, nn-1):
        if arr3[0][i] > 3:
            arr1[0][i] = arr2[0][i]
        else:
            arr1[0][i] = arr2[0][i] = max(arr2[0][i]-1, 0)
        if arr3[-1][i] > 3:
            arr1[-1][i] = arr2[-1][i]
        else:
            arr1[-1][i] = arr2[-1][i] = max(arr2[-1][i]-1, 0)
        if arr3[i][-1] > 3:
            arr1[i][-1] = arr2[i][-1]
        else:
            arr1[i][-1] = arr2[i][-1] = max(arr2[i][-1]-1, 0)
        if arr3[i][0] > 3:
            arr1[i][0] = arr2[i][0]
        else:
            arr1[i][0] = arr2[i][0] = max(arr2[i][0]-1, 0)
        arr3[0][i] = arr3[-1][i] = arr3[i][-1] = arr3[i][0] = 4
    for i in range(1, nn-1):
        for j in range(1, nn-1):
            if arr3[i][j] > 2:
                arr1[i][j] = arr2[i][j]
            else:
                arr1[i][j] = arr2[i][j] = max(arr2[i][j]-1, 0)
            arr3[i][j] = 4
    arr1[0][0] = arr2[0][0] = max(arr2[0][0]-1, 0)
    arr1[0][-1] = arr2[0][-1] = max(arr2[0][-1]-1, 0)
    arr1[-1][-1] = arr2[-1][-1] = max(arr2[-1][-1]-1, 0)
    arr1[-1][0] = arr2[-1][0] = max(arr2[-1][0] - 1, 0)
    arr3[0][0] = arr3[0][-1] = arr3[-1][0] = arr3[-1][-1] = 4

visit = [[True] * nn for _ in range(nn)]
ans1, ans2 = 0, 0
for i in range(nn):
    for j in range(nn):
        ans1 += arr1[i][j]
        if visit[i][j]:
            visit[i][j] = False
            if arr1[i][j] == 0: continue
            t = 0
            q = [(i, j)]
            while q:
                tmp = []
                for x, y in q:
                    t += 1
                    for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                        if -1 < x+dx < nn \
                                and -1 < y+dy < nn \
                                and visit[x+dx][y+dy] \
                                and arr1[x+dx][y+dy] > 0:
                            visit[x+dx][y+dy] = False
                            tmp.append((x+dx, y+dy))
                q = tmp
            ans2 = max(ans2, t)
print(ans1, ans2, sep='\n')
"""
3 10
1 2 3 4 5 6 7 8
8 7 6 5 4 3 2 1
1 2 3 4 5 6 7 8
8 7 6 5 4 3 2 1
1 2 3 4 5 6 7 8
8 7 6 5 4 3 2 1
1 2 3 4 5 6 7 8
8 7 6 5 4 3 2 1
1 2 0 3 2 1 2 3 2 3

2 1
0 0 0 0
0 0 0 0
0 3 0 0
0 0 0 0
0
"""