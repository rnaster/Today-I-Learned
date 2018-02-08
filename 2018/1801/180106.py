# BOJ - 9184
from sys import stdin, stdout
read = lambda: stdin.readline().rstrip()
write = lambda a, b, c, val: stdout.write('w(%s, %s, %s) = %s\n' %(a, b, c, val))
dp = [[[-1 for _ in range(21)] for _ in range(21)] for _ in range(21)]
def main(a, b, c):
    global dp
    if a <= 0 or b <= 0 or c <= 0: return 1
    if a > 20 or b > 20 or c > 20:
        if dp[20][20][20] != -1: return dp[20][20][20]
        else: return main(20, 20, 20)
    dp[a][b][c] = 0
    if a < b < c:
        dp[a][b][c] += dp[a][b][c-1] if dp[a][b][c-1] != -1 else main(a, b, c-1)
        dp[a][b][c] += dp[a][b-1][c - 1] if dp[a][b-1][c - 1] != -1 else main(a, b-1, c - 1)
        dp[a][b][c] -= dp[a][b-1][c] if dp[a][b-1][c] != -1 else main(a, b-1, c)
    else:
        dp[a][b][c] += dp[a-1][b][c] if dp[a-1][b][c] != -1 else main(a-1, b, c)
        dp[a][b][c] += dp[a-1][b-1][c] if dp[a-1][b-1][c] != -1 else main(a-1, b-1, c)
        dp[a][b][c] += dp[a-1][b][c-1] if dp[a-1][b][c-1] != -1 else main(a-1, b, c-1)
        dp[a][b][c] -= dp[a-1][b - 1][c-1] if dp[a-1][b - 1][c-1] != -1 else main(a-1, b - 1, c-1)
    return dp[a][b][c]
while True:
    a, b, c = map(int, read().split())
    if a == -1 and b == -1 and c == -1: quit()
    val = main(a, b, c)
    write(a, b, c, val)

'''
1 1 1
2 2 2
10 4 6
50 50 50
-1 7 18
-1 -1 -1
'''