# BOJ - 15988
from sys import stdin
from array import array
read = lambda: stdin.readline().rstrip()
dp = array('Q', [0]*1000001)
dp[1], dp[2], dp[3] = 1, 2, 4
t = 4
for _ in range(int(input())):
    n = int(read())
    if dp[n] > 0: print(dp[n])
    else:
        for i in range(t, n+1):
            dp[i] = (dp[i-1]+dp[i-2]+dp[i-3]) % 1000000009
        print(dp[n])
    t = n+1
"""
3
7
4
10
"""
exit()

# BOJ - 2098
from sys import setrecursionlimit
setrecursionlimit(10000000)
n = int(input())
grid = [tuple(map(int, input().split())) for _ in range(n)]
dp = [[-1]*(1 << n) for _ in range(n)]
p = 0
def main(a, b):
    global p
    if b == (1 << n) - 1:
        dp[a][b] = 0
        return 0
    else:
        temp = 987654321
        for i in range(n):
            if not b & 1<<i and grid[a][i] != 0:
                if i != p or b | 1<< i == 2 ** n - 1:
                    val = dp[i][b|1<<i] if dp[i][b|1<<i] != -1 else main(i, b|1<<i)
                    temp = min(temp, val+grid[a][i])
        dp[a][b] = temp
    return dp[a][b]
print(main(p, 0))
print(*list(range(1<<n)), sep=' \t')
print(*dp, sep='\n')
# print('#'*30)
# dp = [[-1]*2**n for _ in range(n)]
# print(main(0, 0))
# print(*list(range(1<<n)), sep=' \t')
# print(*dp, sep='\n')

"""
4
0 10 15 20
5  0  9 10
6 13  0 12
8  8  9  0

3
0 10 15
5  0  9
6 13  0

2
0 1
87 0

4
0 1 1 1
1 0 1 1
1 1 0 1
1 1 1 0
"""