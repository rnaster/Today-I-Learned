# BOJ - 1547
ans = 1
for _ in range(int(input())):
    a, b = map(int, input().split())
    if a == ans or b == ans:
        ans = b if ans == a else a
print(ans)
"""
4
3 1
2 3
3 1
3 2
"""