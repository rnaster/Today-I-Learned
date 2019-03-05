# BOJ - 2246
import sys
read = lambda: sys.stdin.readline().rstrip()
n = int(input())
arr = [tuple(map(int, read().split())) for _ in range(n)]
ans = 0
for i in range(n):
    a, b = 0, 0
    for j in range(i+1, n):
        if arr[i][0] > arr[j][0]:
            a += 1
            if arr[i][1] < arr[j][1]: a -= 1
        if arr[i][1] > arr[j][1]:
            b += 1
            if arr[i][0] < arr[j][0]: b -= 1
    if a == 0 and b == 0: ans += 1;print(i, '###')
print(ans-1)
"""
5
300 100
100 300
400 200
200 400
100 500
"""
exit()
# BOJ - 2229
n = int(input())
arr = tuple(map(int, input().split()))
dp = [0]*n
min_arr = [[11]*n for _ in range(n)]
max_arr = [[0]*n for _ in range(n)]
min_arr[0][0] = arr[0]
max_arr[0][0] = arr[0]
for i in range(1, n):
    min_arr[0][i] = min(min_arr[0][i-1], arr[i])
    max_arr[0][i] = max(max_arr[0][i - 1], arr[i])
    min_arr[i][i], max_arr[i][i] = arr[i], arr[i]
    dp[i] = max(dp[i - 1], max_arr[0][i] - min_arr[0][i])
    for j in range(i-1, 0, -1):
        min_arr[j][i] = min(min_arr[j+1][i], arr[j])
        max_arr[j][i] = max(max_arr[j+1][i], arr[j])
        dp[i] = max(dp[i], dp[j-1] + max_arr[j][i] - min_arr[j][i])
print(*dp)
print('#'*10)
print(*min_arr, sep='\n')
print('#'*10)
print(*max_arr, sep='\n')
"""
10
2 5 7 1 3 4 8 6 9 3
"""