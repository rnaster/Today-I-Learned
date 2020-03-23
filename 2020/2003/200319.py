# BOJ - 5545
n = int(input())
a, b = map(int, input().split())
c = int(input())
arr = sorted(int(input()) for _ in range(n))
ans = c // a
for i in range(n-1, -1, -1):
    c += arr[i]
    a += b
    ans = max(ans, c // a)
print(ans)
"""
3
12 2
200
50
300
100
"""