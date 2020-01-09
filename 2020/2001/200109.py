# BOJ - 2491
a, b, c = 0, 0, -1
ans = 1
input()
for i in map(int, input().split()):
    if c < i:
        b += 1
        ans = max(ans, a)
        a = 1
    elif c > i:
        a += 1
        ans = max(ans, b)
        b = 1
    else:
        a += 1
        b += 1
    c = i
print(max(ans, a, b))
"""
9
1 2 2 4 4 5 7 7 2

2
1 5 3 6 4 7 1 3 2 9 5

2
0 0
"""