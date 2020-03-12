# BOJ - 1644
n = int(input())
p = [True] * (n+1)
p[:2] = [False] * 2
for i in range(2, n+1):
    if p[i]:
        for j in range(i*i, n+1, i):
            p[j] = 0
p = [i for i, j in enumerate(p) if j > 0]
ans = 0
i, j = 0, 0
a = 0
while i <= j < len(p):
    if a < n:
        a += p[j]
        j = min(len(p)-1, j+1)
    elif a > n:
        a -= p[i]
        i += 1
    else:
        a += p[j] - p[i]
        j = min(len(p)-1, j+1)
        i += 1
        ans += 1
print(ans)
"""
41
"""