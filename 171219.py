# BOJ - 10835
'''
from sys import stdin
read = lambda: stdin.readline().rstrip()
n = int(read())
L = tuple(map(int, read().split()))
R = tuple(map(int, read().split()))
dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
ans = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        dp[i][j] = max(dp[i-1][j-1], dp[i][j-1])
        dp[i][j] = max(dp[i][j], dp[i-1][j]) if R[j-1] < L[i-2] else dp[i][j]
        dp[i][j] += R[j-1] if R[j-1] < L[i-1] else 0
        if i == n or j == n:
            ans = max(ans, dp[i][j])
from pprint import pprint
pprint(dp, width=20)
print(ans)
'''

from sys import stdin, setrecursionlimit
setrecursionlimit(1500000)
read = lambda: stdin.readline().rstrip()
n = int(read())
L = tuple(map(int, read().split()))
R = tuple(map(int, read().split()))
dp = [[-1 for _ in range(n)] for _ in range(n)]
def main(N, M):
    global dp
    if dp[N][M] != -1: return dp[N][M]
    if M == 0:
        dp[N][M] = 0
        return dp[N][M]
    if N == 0:


    else:
        val = max(main(N-1, M), main(N-1, M-1))
        if R[M-1] < L[N]: val = max(val, main(N, M-1))
        if R[M] < L[N]: val += R[M]
        dp[N][M] = val
        return dp[N][M]

from pprint import pprint
main(n-1, n-1)
pprint(dp, width=20)
'''
2
2 1
3 1


'''