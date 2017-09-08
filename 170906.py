#BOJ - 11066
from sys import stdin
read = lambda: stdin.readline().rstrip()
for _ in range(int(input())):
    k = int(input())
    tp = tuple(map(int, read().split()))
    mtx = [[0 for _ in range(k)] for _ in range(k)]
    for i in range(k):
        mtx[i][i] = tp[i]
    row, col = 0, 1
    while True:
        idx = 1
        while True:
            mini = 10000
            for i in range(col):
                if col - row == 1:
                    mtx[row][col] = mtx[row][row] + mtx[col][col]
                else:
                    if i == row:
                        mini = min(mini, mtx[row][row] + 2*mtx[i+1][col])
                    elif i == col:
                        mini = min(mini, mtx[col][col] + 2*mtx[row][i+1])
                    else:
                        mini = min(mini, 2*mtx[row][i+1] + 2*mtx[i+2][col])
            mtx[row][col] = mini
        if (row, col) == (0, k-1): break
        row += 1; col += 1
    print(mtx)
      ###
def foo1():
    pass