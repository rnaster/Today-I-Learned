def BOJ2167():
    # BOJ - 2167
    from sys import stdin
    read = lambda : stdin.readline().rstrip()
    n, m = map(int, read().split())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, read().split())))
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + arr[i-1][j-1]
    for _ in range(int(read())):
        a, b, c, d = map(int, read().split())
        if a == c and b == d:
            print(arr[a-1][b-1])
        elif a == 1 and b == 1:
            print(dp[c][d])
        elif b == 1:
            print(dp[c][d] - dp[a-1][d])
        elif a == 1:
            print(dp[c][d] - dp[c][b-1])
        else:
            print(dp[c][d] - dp[a-1][d] - dp[c][b-1] + dp[a-1][b-1])
    '''
    2 3
    1 2 4
    8 16 32
    3
    1 1 2 3
    1 2 1 2
    1 3 2 3
    '''
def BOJ1977():
    # BOJ - 1977
    from math import sqrt, ceil
    m = int(input())
    n = int(input())
    ans2 = ceil(sqrt(m))
    tmp = ans2
    ans1 = 0
    while tmp * tmp <= n:
        ans1 += tmp * tmp
        tmp += 1
    if ans1 == 0: print(-1); quit()
    print(ans1)
    print(ans2*ans2)

# BOJ - 1016
import math
n, m = map(int, input().split())
root = int(math.sqrt(m))
l = list(range(2, root+1))
prime = list(map(lambda x: list(map(lambda y: x if x % (y*y) != 0 else None, range(2, root+1)))))
print(prime)
# print(prime)
# quit()
ans = list(range(n, m+1))
for p in prime:
    ans = list(filter(lambda x: x % (p*p) != 0, ans))
    # print(ans)
print(len(ans))

# 1000000000000
# 1000000