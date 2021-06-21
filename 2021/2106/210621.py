# BOJ - 3108
n = int(input())
arr = [[*map(int, input().split())] for _ in range(n)]
def iou(i, j):
    x1, y1, x2, y2 = arr[i]
    xx1, yy1, xx2, yy2 = arr[j]
    max_x1 = max(x1, xx1)
    max_y1 = max(y1, yy1)
    min_x2 = min(x2, xx2)
    min_y2 = min(y2, yy2)
    if min_x2 < max_x1 or min_y2 < max_y1:
        return 0
    if x1 < xx1 < xx2 < x2 and y1 < yy1 < yy2 < y2:
        return 0
    return 1
l = [-1] * n
def find(a):
    if l[a] == -1:
        return a
    l[a] = find(l[a])
    return l[a]
for i in range(n):
    for j in range(i+1, n):
        if iou(i, j):
            ii = find(i)
            jj = find(j)
            if ii == jj: continue
            l[jj] = ii
ans = 1
for i in range(n):
    x1, y1, x2, y2 = arr[i]
    if x1 <= 0 <= x2 and (y1 == 0 or y2 == 0):
        ans = 0
        break
    if y1 <= 0 <= y2 and (x1 == 0 or x2 == 0):
        ans = 0
        break
ans += l.count(-1) - 1
print(ans)
"""
5
1 1 4 4
3 3 6 6
4 4 5 5
5 0 8 3
6 1 7 2
"""