# BOJ - 14863
n, k = map(int, input().split())
dp = {0: 0}
for i in range(n):
    a1, a2, a3, a4 = map(int, input().split())
    tmp = {}
    for a, b in dp.items():
        if a + a1 <= k:
            tmp[a+a1] = max(tmp.get(a+a1, 0), b + a2)
        if a + a3 <= k:
            tmp[a+a3] = max(tmp.get(a+a3, 0), b + a4)
    dp = tmp
print(max(dp.values()))
"""
3 1650
500 200 200 100
800 370 300 120
700 250 300 90
"""