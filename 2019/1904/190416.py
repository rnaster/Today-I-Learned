# BOJ - 5624
n = int(input())
one, two = set(), set()
ans = 0
for i in map(int, input().split()):
    for j in one:
        if i - j in two: ans += 1; break
    one.add(i)
    for j in one:
        two.add(i+j)
print(ans)
"""
6
1 2 3 5 7 10
"""