# BOJ - 10835
from sys import stdin
import sys
# sys.setrecursionlimit(1500000)
read = lambda: stdin.readline().rstrip()
n = int(read())
L = tuple(map(int, read().split()))
R = tuple(map(int, read().split()))
dp = [[-1 for _ in range(n)] for _ in range(n)]
def main(N, M):
    global dp
    if dp[N][M] != -1: return dp[N][M]
    if N == 0:
        dp[N][M] = R[N] if R[N] < L[M] else 0
        return dp[N][M]
    if M == 0:
        if R[N-1] < L[M]:
            dp[N][M] = dp[N-1][M] if dp[N-1][M] != -1 else main(N-1, M)
            dp[N][M] += R[N] if R[N] < L[M] else 0
        else:
            dp[N][M] = 0
        return dp[N][M]
    else:
        c1 = main(N, M - 1) if dp[N][M-1] == -1 else dp[N][M-1]
        c2 = main(N - 1, M - 1) if dp[N-1][M-1] == -1 else dp[N-1][M-1]
        if R[N] < L[M]:
            c3 = dp[N-1][M] if dp[N-1][M] != -1 else main(N-1, M)
            c3 += R[N]
        else: c3 = 0
        dp[N][M] = max(c1, c2, c3)
        return dp[N][M]
# print(main(n-1, n-1))

# import random
# n = 2000
# L = [random.randint(1, 2000) for _ in range(n)]
# R = [random.randint(1, 2000) for _ in range(n)]
# dp = [[-1 for _ in range(n)] for _ in range(n)]

for i in range(n): # Right
    for j in range(n): # Left
        if i == 0:
            dp[i][j] = R[i] if R[i] < L[j] else 0
            continue
        if j == 0:
            dp[i][j] = dp[i - 1][j]
            dp[i][j] += R[i] if R[i] < L[j] else 0
            continue
        else:
            c1 = dp[i][j - 1]
            c2 = dp[i - 1][j - 1]
            if R[i] < L[j]:
                c3 = dp[i - 1][j] + R[i]
            else:
                c3 = 0
            dp[i][j] = max(c1, c2, c3)
print(dp[-1][-1])
# from pprint import pprint
# pprint(dp)


def test():
    n = 1990
    # call = 0
    while n <= 2000:
        # try:
        L = [random.randint(1, 2000) for _ in range(n)]
        R = [random.randint(1, 2000) for _ in range(n)]
        dp = [[-1 for _ in range(n)] for _ in range(n)]
        print(main(n-1, n-1), '\t', n)
        n += 1
        # except:
        #     print('Error!')
        #     print(L, '\n', R)
    #     break
# test()

# from pprint import pprint
# pprint(dp, width=20)




'''
3
3 2 5
2 4 1

4
1 2 3 4
4 1 2 3

5
1 2 3 2 1
9 3 2 7 1
'''