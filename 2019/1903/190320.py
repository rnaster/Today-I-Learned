# BOJ - 1720
n = int(input())
dp0, dp1 = [0] * 31, [0] * 31
dp0[:4] = [0, 1, 3, 5]
dp1[:4] = [1, 1, 3, 1]
for i in range(4, 31):
    dp0[i] = dp0[i-1] + 2*dp0[i-2]
    dp1[i] = dp1[i-2] + 2*dp1[i-4]
print(dp1[n] + (dp0[n]-dp1[n])//2)
"""
4
"""