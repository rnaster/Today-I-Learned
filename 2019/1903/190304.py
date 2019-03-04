# BOJ - 9324
for _ in range(int(input())):
    t = ''
    d = dict()
    a = True
    for tt in input():
        if t != '':
            if t == tt:
                t = ''
                d[tt] = 0
            else:
                t = ''
                a = False
                print('FAKE');break
        else:
            if tt in d:
                d[tt] += 1
                if d[tt] > 2: t = tt
            else: d[tt] = 1
    if a:
        if t: print('FAKE')
        else: print('OK')
"""
4
BAPC
AABA
ABCABCBBAAACC
BBBACQWRT
"""
exit()

# BOJ - 7976
n, k = 8, 2#map(int, input().split())
import random
arr = [random.randint(0, 20) for _ in range(n)]
# arr = tuple(map(int, input().split()))
dp = [[0]*n for _ in range(2)]
temp = 0
for i in range(k):
    if arr[i] % 2:
        dp[0][i], dp[1][i] = 1, 1
        temp += 1
if temp % 2:
    dp[1][k-1] = 1 - dp[1][k-1]
    dp[0][0] = 1 - dp[0][0]
    a, b = 1, 1
else: a, b = 0, 0
for i in range(1, n-k+1):
    p = dp[1][i-1] + arr[i+k-1]
    q = dp[0][i-1] + arr[i+k-1]
    if p % 2:
        a += 1
    if q % 2:
        b += 1
    dp[1][i+k-1] = dp[1][i-1]
    dp[0][i + k - 1] = dp[0][i - 1]
print(min(a, b))
print(*dp, sep='\n')
print(arr)
"""
8 3
1 2 3 4 5 6 7 8
"""
exit()

# BOJ - 12865
n, k = map(int, input().split())
arr = [tuple(map(int, input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(k+1)]
for i in range(1, k+1):
    if i >= arr[0][0]: dp[i][0] = arr[0][1]
    for j in range(1, n):
        if i >= arr[j][0]:
            dp[i][j] = max(dp[i][j-1], dp[i-arr[j][0]][j-1]+arr[j][1])
        else: dp[i][j] = dp[i][j-1]
print(dp[-1][-1])
print(*dp, sep='\n')
"""
4 7
6 13
4 8
3 6
5 12
"""