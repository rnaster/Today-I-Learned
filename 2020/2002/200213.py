# BOJ - 1449
n, m = map(int, input().split())
ans, a = 0, 0
for i in sorted(map(int, input().split())):
    if i < a: continue
    ans += 1
    a = i + m
print(ans)
"""
4 2
1 2 100 101 6 99
"""
exit()

# BOJ - 2531
import sys
read = sys.stdin.readline
n, d, k, c = map(int, read().split())
arr = [int(read()) for _ in range(n)]
l = [0] * (d+1)
l[c] += 1
tmp = 1
for i in range(k):
    if l[arr[i]] < 1:
        tmp += 1
    l[arr[i]] += 1
ans = tmp
for ran in [range(k, n), range(k-1)]:
    for i in ran:
        l[arr[i-k]] -= 1
        if l[arr[i-k]] < 1:
            tmp -= 1
        l[arr[i]] += 1
        if l[arr[i]] < 2:
            tmp += 1
        ans = max(ans, tmp)
print(ans)
"""
8 30 4 30
7
9
7
30
2
7
9
25
"""