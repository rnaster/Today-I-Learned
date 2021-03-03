# BOJ - 2559
n, k = map(int, input().split())
arr = [*map(int, input().split())]
a = 0
for i in range(k):
    a += arr[i]
ans = a
for i in range(k, n):
    a += arr[i] - arr[i-k]
    ans = max(ans, a)
print(ans)
"""
10 2
3 -2 -4 -9 0 3 7 13 8 -3
"""