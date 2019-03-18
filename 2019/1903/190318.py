# BOJ - 2616
n = int(input())
arr = tuple(map(int, input().split()))
k = int(input())
dp1, dp2, dp3 = [0]*(n+1), [0]*(n+1), [0]*(n+1)
for i in range(k, n+1):
    t = sum(arr[i-k:i])
    dp1[i], dp2[i], dp3[i] = max(dp1[i-1], t), max(dp2[i-1], dp1[i-k]+t), max(dp3[i-1], dp2[i-k]+t)
print(dp3[n])
"""
8
35 40 50 10 30 45 60 60
2

7
35 40 50 10 30 45 60
2
"""