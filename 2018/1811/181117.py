# BOJ - 2960
from array import array
n, k = map(int, input().split())
arr = array('B', [0] * (n+1))
idx = 0
for i in range(2, n+1):
    if arr[i] == 0:
        for j in range(i, n+1, i):
            if arr[j] == 0:
                arr[j] = 1
                idx += 1
                if idx == k: print(j);exit()