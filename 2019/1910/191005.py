# BOJ - 10982
import sys
dp = None
arr = None
n = 0
def func(_n, _a, _b):
    print(_n, _a, _b)
    global dp
    if dp[_n][_a][_b] != -1:
        return dp[_n][_a][_b]
    if _n == n:
        dp[_n][_a][_b] = max(_a, _b)
        return dp[_n][_a][_b]
    val = min(_a, _b)
    _a, _b = _a - val, _b - val
    if _a == 0 and _b == 0:
        val += min(func(_n + 1, arr[_n][0], _b),
                   func(_n + 1, _a, arr[_n][1]))
    elif _a > _b:
        val += min(func(_n + 1, arr[_n][0], _b) + _a,
                   func(_n + 1, _a, arr[_n][1]))
    else:
        val += min(func(_n + 1, _a, arr[_n][1]) + _b,
                   func(_n + 1, arr[_n][0], _b))
    dp[_n][_a][_b] = val
    return dp[_n][_a][_b]
for _ in range(int(input())):
    dp = [[[-1] * 31 for _ in range(31)] for _ in range(5)]
    n = int(input())
    arr = [[*map(int, sys.stdin.readline().split())]
           for _ in range(n)]
    print(func(0, 0, 0))
    # for a in dp:
    #     print(*a, '', sep='\n')
"""
2
3
10 5
8 5
8 5
4
15 20
30 21
5 3
10 10

1
4
15 20
30 21
5 3
10 10
"""
exit()

# BOJ - 1018
n, m = map(int, input().split())
arr = [[*input()] for _ in range(n)]
def func(_arr):
    ans1, ans2 = 0, 0
    for i in range(8):
        for j in range(8):
            if (i + j) % 2:
                if _arr[i][j] == 'B':
                    ans2 += 1
                else:
                    ans1 += 1
            else:
                if _arr[i][j] == 'W':
                    ans2 += 1
                else:
                    ans1 += 1
    return min(ans1, ans2)
ans = 9999999
for i in range(n-7):
    for j in range(m-7):
        ans = min(ans, func([arr[k][j:j+8] for k in range(i, i+8)]))
print(ans)
"""
8 8
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBBBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW
"""