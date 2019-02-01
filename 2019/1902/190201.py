# BOJ - 2157
from sys import stdin
read = lambda: stdin.readline().rstrip()
n, m, k = map(int, read().split())
dp = [[-1] * n for _ in range(m)]
ans = 0
l = []
for _ in range(k):
    a, b, c = map(int, read().split())
    if a < b:
        if a > 1:
            l.append((a, b, c))
        else:
            dp[0][b - 1] = max(dp[0][b - 1], c)
for i in range(2, n+1):
    for a, b, c in l:
        if a == i:
            for j in range(m-1):
                if dp[j][a-1] > 0:
                    dp[j+1][b-1] = max(dp[j+1][b-1], dp[j][a-1]+c)
for i in range(m):
    if dp[i][-1] > 0: ans = max(ans, dp[i][-1])
print(ans)
print(*dp, sep='\n')
"""
3 3 5
1 3 10
1 2 5
2 3 3
1 3 4
3 1 100

7 4 10
1 2 3
2 3 1
1 2 5
1 3 4
2 3 8
1 2 100
5 6 1000
1 6 33
3 4 1
4 7 2
"""
exit()

# BOJ - 2629
n = int(input())
arr = tuple(map(int, input().split()))
m = int(input())
t = tuple(map(int, input().split()))
for i in t:
    dp = {i}
    b = True
    for k in arr:
        temp = set()
        for j in dp:
            temp.update({j-k, j+k, j})
        dp.update(temp)
        if 0 in dp: print('Y', end=' ');b=False;break
    if b: print('N', end=' ')
"""
2
1 4
2
3 2
"""
exit()

# BOJ - 16676
n = int(input())
if n < 11: print(1);exit()
ans = 1
k = 10
m = 1
while True:
    if n > k:
        ans += 1
        m += k
        k *= 10
    else:
        if n >= m: print(ans)
        else: print(ans-1)
        break
"""
110
"""