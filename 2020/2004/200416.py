# BOJ - 1727
n, m = map(int, input().split())
arr1 = sorted(map(int, input().split()))
arr2 = sorted(map(int, input().split()))
if n > m:
    n, m = m, n
    arr1, arr2 = arr2, arr1
cache = [[0] * m for _ in range(n)]
c = m-n+1
dp = [987654321] * (c+1)
for i in range(c-1, -1, -1):
    dp[i] = min(dp[i+1], abs(arr1[-1] - arr2[n-1+i]))
for i in range(n-2, -1, -1):
    tmp = [987654321] * (c+1)
    for j in range(c-1, -1, -1):
        tmp[j] = min(tmp[j+1], abs(arr1[i] - arr2[i+j]) + dp[j])
    dp = tmp
print(dp[0])
"""
2 3
10 20
15 11 9

4 6
1 2 3 4
2 3 4 5 6 7

3 6
10 20 30
9 10 11 100 101 102

4 3
1 2 4 4
3 3 3

3 2
1 99 100
98 99
"""