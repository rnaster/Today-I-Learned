# BOJ - 2169
from sys import stdin, stdout
from array import array
import numpy as np
read = lambda: stdin.readline().rstrip()
n, m = map(int, read().split())
tp = tuple(map(int, read().split()))
# arr = array('l', [0 for _ in range(m+2)])
arr = np.array([0 for _ in range(m+2)])
for i in range(m):
    arr[i+1] = tp[i] + arr[i]
for _ in range(n-1):
    tp = tuple(map(int, read().split()))
    temp = np.array([0 for _ in range(m+2)])
    r, l = np.array([0 for _ in range(m+2)]), np.array([0 for _ in range(m+2)])
    for i in range(m):
        r[i+1], l[-i-2] = tp[i] + r[i], tp[-i-1] + l[-i-1]
    for i in range(1, m+1):
        # R = max(tuple([arr[j] + r[j] for j in range(i, m+1)])) - r[i-1]
        # L = max(tuple([arr[j] + l[j] for j in range(1, i+1)])) - l[i+1]
        R = max(r[i:m+1] + arr[i:m+1]) - r[i-1]
        L = max(l[1:i+1] + arr[1:i+1]) - l[i+1]
        temp[i] = max(R, L)
    arr = temp[:]
    del temp
stdout.write(str(arr[-2]) + '\n')