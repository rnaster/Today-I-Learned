# BOJ - 20061
import sys
read = sys.stdin.readline
arr1 = [[0] * 4 for _ in range(6)]
arr2 = [[0] * 4 for _ in range(6)]
def func(arr, t, x, y):
    x1, y1 = x, y
    x2, y2 = x, y
    if t == 2:
        y2 += 1
    elif t == 3:
        x2 += 1
    min_x1, min_x2 = -6, -6
    for i in range(1, 7):
        if not arr[-i][y1]:
            min_x1 = -i
        else:
            break
    for i in range(1, 7):
        if not arr[-i][y2]:
            min_x2 = -i
        else:
            break
    max_x = max(min_x1, min_x2)
    arr[max_x][y1] = 1
    if t == 3:
        arr[max_x+1][y2] = 1
    else:
        arr[max_x][y2] = 1
    cnt = 0
    idx = 0
    while idx < 6:
        if sum(arr[idx]) == 4:
            cnt += 1
            arr.pop(idx)
            arr.append([0] * 4)
        else:
            idx += 1
    for _ in range(2):
        if sum(arr[-2]) > 0 or sum(arr[-1]) > 0:
            arr.pop(0)
            arr.append([0] * 4)
    return cnt
ans1, ans2 = 0, 0
for _ in range(int(read())):
    t, x, y = map(int, read().split())
    ans1 += func(arr1, t, x, y)
    if t == 1:
        ans1 += func(arr2, 1, y, x)
    elif t == 2:
        ans1 += func(arr2, 3, y, x)
    else:
        ans1 += func(arr2, 2, y, x)
print(ans1)
for i in range(6):
    ans2 += sum(arr1[i]) + sum(arr2[i])
print(ans2)
"""
8
1 1 1
2 3 0
3 2 2
3 2 3
3 1 3
2 0 0
3 2 0
3 1 2
"""