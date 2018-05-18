# BOJ - 1947
n = int(input())
mtx = [[0 for _ in range(n+1)] for _ in range(n+1)]
mtx[0][0] = 1
mtx[1][0] = 1
mtx[1][1] = 1
for i in range(2, n+1):
    mtx[i][0] = 1
    for j in range(1, n+1):
        if i >= j:
            if j <= i - j:
                mtx[i][j] = (mtx[i-1][j-1] + mtx[i-1][j]) % 1000000000
            else:
                mtx[i][j] = mtx[i][i-j]
        else:
            break


for i in range(2, n+1):
    tmp = 0
    f = 1
    for j in range(i):
        tmp = (tmp + mtx[i][i-j]*mtx[0][j]) % 1000000000
        f = f*(j+1) % 1000000000
    mtx[0][i] = (f - tmp) % 1000000000
print(mtx[0][n])