# BOJ - 10803
import sys
sys.setrecursionlimit(1000000)
n, m = map(int, input().split())
if n == m: print(1);exit()
dp = {}
for i in range(1, min(n, m)+1):
    dp[(i, i)] = 1
def func(a, b):
    val = 100_000_001
    for i in range(1, (a+2) // 2):
        t1, t2 = i, b
        if i > b:
            t1, t2 = b, i
        tmp1 = dp[(t1, t2)] if (t1, t2) in dp else func(t1, t2)
        t1, t2 = a-i, b
        if a-i > b:
            t1, t2 = b, a-i
        tmp2 = dp[(t1, t2)] if (t1, t2) in dp else func(t1, t2)
        val = min(val, tmp1+tmp2)
    for j in range(1, (b+2) // 2):
        t1, t2 = a, j
        if a > j:
            t1, t2 = j, a
        tmp1 = dp[(t1, t2)] if (t1, t2) in dp else func(t1, t2)
        t1, t2 = a, b-j
        if a > b-j:
            t1, t2 = b-j, a
        tmp2 = dp[(t1, t2)] if (t1, t2) in dp else func(t1, t2)
        val = min(val, tmp1 + tmp2)
    dp[(a, b)] = val
    return val
if n > m: print(func(m, n))
else: print(func(n, m))
"""
6 5
"""
exit()

# BOJ - 2551
from collections import Counter
n = int(input())
arr = [0] * 10_000
val, val2 = 0, 0
for k, v in Counter(map(int, input().split())).items():
    arr[k-1] = v
    val += k*v
    val2 += k*k*v
cnt = 0
tmp = s = val
tmp2 = val2
ans1, ans2 = 1, 1
for i, j in enumerate(arr, 1):
    tmp += 2*cnt - n
    if val > tmp:
        val = tmp
        ans1 = i
    cnt += j
    tmp3 = tmp2 + i*i*n - 2*s*i
    if val2 > tmp3:
        val2 = tmp3
        ans2 = i
print(ans1, ans2)
"""
6
4 3 2 2 10 10
"""
exit()

# BOJ - 2461
from heapq import *
n, m = map(int, input().split())
arr = [sorted(map(int, input().split())) for _ in range(n)]
val, idx = -1, -1
h = []
for i in range(n):
    heappush(h, (arr[i][0], i, 0))
    if val < arr[i][0]:
        val = arr[i][0]
        idx = i
ans = 1234567890
while h:
    a, b, c = heappop(h)
    if b != idx:
        ans = min(ans, abs(val - a))
    if c == m-1: continue
    heappush(h, (arr[b][c+1], b, c+1))
    if val <= arr[b][c+1]:
        val = arr[b][c+1]
        idx = b
    print(h, val, idx)
print(ans)
"""
3 4
12 16 67 43
7 17 68 48
14 15 77 54

2 3
1 99 999
50 99 101
"""