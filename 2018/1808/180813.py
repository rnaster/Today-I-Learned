# BOJ - 1475
n = input()
ans = 1
d = {i: 1 for i in range(9)}
d[6] += 1
for a in n:
    if a in ('6', '9'):
        if d[6] > 0:
            d[6] -= 1
        else:
            ans += 1
            d[6] = 1
            for i in (0, 1, 2, 3, 4, 5, 7, 8):
                d[i] += 1
    elif d[int(a)] > 0:
        d[int(a)] -= 1
    else:
        ans += 1
        d[6] += 2
        for i in (0, 1, 2, 3, 4, 5, 7, 8):
            d[i] += 1
        d[int(a)] -= 1
print(ans)

"""
9999
"""