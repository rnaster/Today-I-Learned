# BOJ - 3663
import string
d = {w: i for i, w in enumerate(string.ascii_uppercase)}
for _ in range(int(input())):
    ans = 0
    ans2 = 0
    a = input().strip()
    b, c = 0, 0
    for i in range(len(a)):
        if a[i] > 'N': ans += 26 - d[a[i]] + 1
        else: ans += d[a[i]] + 1
        if a[i] == 'A': b += 1
        else: b = 0
        if a[-i] > 'N': ans2 += 26 - d[a[-i]] + 1
        else: ans2 += d[a[-i]] + 1
        if a[-i] == 'A': c += 1
        else: c = 0
    ans -= b
    ans2 -= c
    ans = max(min(ans, ans2)-1, 0)
    print(ans)
"""
6
JEROEN
JAN
A
ABABA
ZZAZZA
AAZAAZ
"""
exit()

# BOJ - 1092
from bisect import bisect as bi
input()
l = sorted(map(int, input().split()))
n = int(input())
arr = sorted(map(int, input().split()))
ll = [(min(bi(arr, i), n-1), i) for i in l]
visit = [1] * n
ans = 0
t = n
while ll and n > 0:
    tmp = []
    for i, j in ll:
        while i > -1 and (visit[i] < 1 or arr[i] > j):
            i -= 1
        if i > -1:
            tmp.append((i, j))
            n -= visit[i]
            visit[i] = 0
    ll = tmp
    ans += 1
if n > 0:
    print(-1)
else:
    print(ans)
"""
3
6 8 9
6
2 5 2 4 7 100

3
1 2 9
5
4 5 6 7 8
"""