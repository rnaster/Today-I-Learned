# BOJ - 1509
from sys import setrecursionlimit
setrecursionlimit(100000)
s = input()
ss = len(s)
dp = [[-1] * ss for _ in range(ss)]
def main(a, b):
    print(a, b)
    global dp
    if dp[a][b] != -1: return dp[a][b]
    if a == b:
        dp[a][b] = 1
        return 1
    else:
        # p, q, r = 2501, 2501, 2501
        for i in range((b-a+1)//2, -1, -1):
            if s[a+i] != s[b-(i+1)]:
                r = dp[a][a+i] if dp[a][a+i] != -1 else main(a, a+i)
                r += dp[a+i+1][b-(i+2)] if dp[a+i+1][b-(i+2)] != -1 else main(a+i+1, b-(i+2))
                r += dp[b-(i+1)][b] if dp[b-(i+1)][b] != -1 else main(b-(i+1), b)
                p = dp[b-(i+1)][b] if dp[b-(i+1)][b] != -1 else main(b-(i+1), b)
                p += dp[a][b-(i+2)] if dp[a][b-(i+2)] != -1 else main(a, b-(i+2))
                q = dp[a][a+i] if dp[a][a+i] != -1 else main(a, a+i)
                q += dp[a+i+1][b] if dp[a+i+1][b] != -1 else main(a+i+1, b)
                dp[a][b] = min(p, q, r)
                return dp[a][b]
        dp[a][b] = 1
        return 1
print(main(0, ss-1))
# def main(a, b):
#     global dp
#     if dp[a][b] != -1: return dp[a][b]
#     if a == b:
#         dp[a][b] = 1
#         return 1
#     else:
#         p, q, r = 2501, 2501, 2501
#         for i in range((b-a)//2):
#             if s[a+i] != s[b-i]:
#                 if a + i+1 < ss:
#                     p = dp[a+i+1][b] if dp[a+i+1][b] != -1 else main(a+i+1, b)
#                     p += dp[a][a+i] if dp[a][a+i] != -1 else main(a, a+i)
#                 if b - i-1 >= 0:
#                     q = dp[a][b-i-1] if dp[a][b-i-1] != -1 else main(a, b-i-1)
#                     q += dp[b-i][b] if dp[b-i][b] != -1 else main(b-i, b)
#                 if a + i+1 < b - i-1:
#                     r = dp[a+i+1][b-i-1] if dp[a+i+1][b-i-1] != -1 else main(a+i+1, b-i-1)
#                     r += dp[a][a+i] if dp[a][a+i] != -1 else main(a, a+i)
#                     r += dp[b-i][b] if dp[b-i][b] != -1 else main(b-i, b)
#                 dp[a][b] = min(p, q, r)
#                 return dp[a][b]
#         dp[a][b] = 1
#         return 1
# print(main(0, ss-1))
print(*dp, sep='\n')
"""
BBCDDECAECBDABADDCEBACCCBDCAABDBADD
"""
exit()

# BOJ - 1958
s1, s2, s3 = input(), input(), input()
ss1 = len(s1)
ss2 = len(s2)
ss3 = len(s3)
dp = [[[0] * (ss1 + 1) for _ in range(ss2+1)] for _ in range(ss3+1)]
for k in range(1, ss3+1):
    for i in range(1, ss2+1):
        for j in range(1, ss1+1):
            if s2[i-1] == s1[j-1] == s3[k-1]:
                dp[k][i][j] = dp[k-1][i-1][j-1] + 1
            else:
                dp[k][i][j] = max(dp[k-1][i][j], dp[k][i-1][j], dp[k][i][j-1])
print(dp[-1][-1][-1], sep='\n')
"""
abcdefghijklmn
bdefg
efg
"""
exit()

# BOJ - 15954
import decimal
n, k = map(int, input().split())
tp = tuple(map(int, input().split()))
arr, arr_ = [0], [0]
for t in tp:
    arr.append(arr[-1]+t)
    arr_.append(arr_[-1] + t*t)
ans = decimal.Decimal('INF')
for i in range(k, n+1):
    for j in range(n-i+1):
        m = decimal.Decimal(arr[i+j]-arr[j]) / i
        v = decimal.Decimal(arr_[i+j]-arr_[j]) / i - m * m
        ans = min(ans, decimal.Decimal(v.sqrt()))
print(ans)

"""
5 3
1 2 3 4 5

10 3
1 4 1 5 9 2 6 5 3 5
"""