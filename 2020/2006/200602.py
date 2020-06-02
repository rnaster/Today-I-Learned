# BOJ - 10166
n, m = map(int, input().split())
arr = [0] * 36000
for i in range(n, m+1):
    for j in range(0, 36000, 36000 // i):
        arr[j] = 1
print(sum(arr))
"""
3 6
"""
exit()

# BOJ - 10836
import sys
read = sys.stdin.readline
n, m = map(int, input().split())
arr = [[1] * n for _ in range(n)]
def func(a):
    i, j = n-1, 0
    for i in range(n-1, -1, -1):
        yield i, j
    for j in range(1, n):
        yield i, j
for _ in range(m):
    a, b, c = map(int, read().split())
    l = [2] * (n-1)

"""
4 2
2 3 2
0 6 1
"""
exit()

# BOJ - 13302
n, m = map(int, input().split())
arr = [True] * (n+1)
if m > 0:
    for i in map(int, input().split()):
        arr[i] = False
dp = [[-1] * (n+1) for _ in range(n+1)]
def func(a, b):
    if a > n:
        return 0
    if dp[a][b] > -1:
        return dp[a][b]
    val = 987654321
    if not arr[a]:
        val = min(val, func(a+1, b))
    if b > 2:
        val = min(val, func(a+1, b-3))
    val = min(val, func(a+1, b) + 10000, func(a+3, b+1) + 25000, func(a+5, b+2) + 37000)
    dp[a][b] = val
    return val
print(func(1, 0))
"""
13 5
4 6 7 11 12
"""
exit()

# BOJ - 15976
import sys
read = sys.stdin.readline
n = int(input())
arr = {}
l = [[] for _ in range(n)]
for i in range(n):
    a, b = map(int, read().split())
    arr[a] = b
    l[i] = [a, b]
n2 = int(input())
arr2 = {}
l2 = [[] for _ in range(n2)]
for i in range(n2):
    a, b = map(int, read().split())
    arr2[a] = b
    l2[i] = [a, b]
p = int(read()); q = int(read())
ans = 0
if p >= 0:
    ans = sum(l[j][1]*arr2[l[j][0]+i]
              for j in range(n)
              for i in range(p, q+1)
              if l[j][0] + i in arr2)
elif q >= 0:
    ans = sum(l2[j][1] * arr[l2[j][0] + i]
              for j in range(n2)
              for i in range(1, abs(p)+1)
              if l2[j][0]+i in arr)
    ans += sum(l[j][1]*arr2[l[j][0]+i]
               for j in range(n)
               for i in range(q+1)
               if l[j][0] + i in arr2)
else:
    ans = sum(l2[j][1] * arr[l2[j][0] + i]
              for j in range(n2)
              for i in range(abs(p), abs(q) + 1)
              if l2[j][0] + i in arr)
print(ans)
"""
3
0 1
4 4
9 5
3
1 3
2 7
10 7
-2
2
"""