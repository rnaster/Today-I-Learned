# BOJ - 1495
from sys import stdin
read = lambda: stdin.readline().rstrip()
n, s, m = map(int, read().split())
tp = tuple(map(int, read().split()))
arr = set([s])
for i in range(n):
    tmp = set()
    for num in arr:
        if 0 <= num-tp[i] <= m: tmp.add(num-tp[i])
        if 0 <= num+tp[i] <= m: tmp.add(num+tp[i])
    ans = max(tmp) if tmp else -1
    arr = tmp
    del tmp
if 0 <= ans <= m: print(ans)
else: print(-1)