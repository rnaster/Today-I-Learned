# BOJ - 1509
from sys import setrecursionlimit
setrecursionlimit(10000000)
s = input()
ss = len(s)
dp = [[-1] * s for _ in range(s)]
def main(ss):
    print(ss)
    if ss == '': return 0
    if len(ss) == 1: return 1
    else:
        i = 0
        for i in range(len(ss)//2):
            # print(i, '###')
            # print(ss[:-(i+1)], ss[i+1:], ss[i+1:-(i+1)])
            if ss[i] != ss[-(i+1)]:
                return min(main(ss[:-(i+1)])+1,
                           main(ss[i+1:])+1,
                           main(ss[i+1:-(i+1)])+2)
        return 1
print(main(s))
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