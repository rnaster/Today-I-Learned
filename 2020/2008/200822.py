# BOJ - 5569
w, h = map(int, input().split())
dp = [[[-1] * w for _ in range(h)] for _ in range(2)]
def func(a, b, c):
    if (b, c) == (h-1, w-1):
        dp[a][b][c] = 1
        return 1
    val = 0
    s = 1
    if a:
        if c == w-1: s = b + 1
        elif (b, c) != (0, 0): s = b + 2
        for i in range(s, h):
            val += dp[1-a][i][c] if dp[1-a][i][c] > -1 else func(1-a, i, c)
    else:
        if b == h-1: s = c + 1
        elif (b, c) != (0, 0): s = c + 2
        for j in range(s, w):
            val += dp[1-a][b][j] if dp[1-a][b][j] > -1 else func(1-a, b, j)
    val %= 100000
    dp[a][b][c] = val
    return val
print((func(0, 0, 0) + func(1, 0, 0)) % 100000)
"""
3 4
"""