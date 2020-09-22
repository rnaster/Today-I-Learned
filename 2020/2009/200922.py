# BOJ - 1956
import sys
read = sys.stdin.readline
n, k = map(int, read().split())
arr = [[987654321] * n for _ in range(n)]
for _ in range(k):
    a, b, c = map(int, read().split())
    arr[a-1][b-1] = c
for k in range(n):
    for i in range(n):
        for j in range(n):
            if arr[i][j] > arr[i][k] + arr[k][j]:
                arr[i][j] = arr[i][k] + arr[k][j]
ans = 987654321
for i in range(n):
    for j in range(i+1, n):
        ans = min(ans, arr[i][j] + arr[j][i])
if ans == 987654321: print(-1)
else: print(ans)
"""
3 4
1 2 1
3 2 1
1 3 5
2 3 2
"""