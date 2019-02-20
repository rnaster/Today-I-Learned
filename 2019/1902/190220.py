# BOJ - 2098
from sys import setrecursionlimit
setrecursionlimit(10000000)
n = int(input())
grid = [tuple(map(int, input().split())) for _ in range(n)]
dp = [[-1]*2**n for _ in range(n)]
def main(a, b):
    if b == 2**n -1:
        dp[a][b] = 0
        return 0
    else:
        temp = 987654321
        for i in range(n):
            if a != i and not b & 1<<i and grid[a][i] != 0:
                val = dp[i][b|1<<i] if dp[i][b|1<<i] != -1 else main(i, b|1<<i)
                temp = min(temp, val+grid[a][i])
        dp[a][b] = temp
    return dp[a][b]
print(main(1, 0))
print(*dp, sep='\n')
print('#'*30)
dp = [[-1]*2**n for _ in range(n)]
print(main(0, 0))
print(*dp, sep='\n')

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