# BOJ - 13305
n = int(input())
arr = [*map(int, input().split())]
l = [*map(int, input().split())]
l = sorted(enumerate(l), key=lambda x: x[1])
ans = 0
a = n
for p, q in l:
    if p == 0:
        ans += q * sum(arr[:a])
        break
    if a > p:
        ans += q * sum(arr[p:a])
        a = p
print(ans)
"""
4
2 3 1
5 2 4 1
"""