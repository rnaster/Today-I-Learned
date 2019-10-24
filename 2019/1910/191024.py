# BOJ - 17471
from itertools import combinations
n = int(input())
arr = tuple(map(int, input().split()))
aa = sum(arr)
d = {}
for i in range(1, n+1):
    _, *a = map(int, input().split())
    d[i] = set(a)
def func(l):
    q = [l.pop()]
    while q:
        _q = []
        for qq in q:
            for dd in d[qq]:
                if dd in l:
                    _q.append(dd)
                    l.remove(dd)
        q = _q
    if l: return False
    return True
ans = 987654321
for i in range(1, n // 2 + 1):
    for comb in combinations(range(1, n+1), i):
        _comb = list(comb)
        if func(_comb) and func([i for i in range(1, n+1) if i not in comb]):
            ans = min(ans, abs(sum([arr[i-1] for i in range(1, n+1) if i not in comb]) - sum([arr[i-1] for i in comb])))
if ans > 99999:
    print(-1)
else:
    print(ans)
"""
6
5 2 3 4 1 2
2 2 4
4 1 3 6 5
2 4 2
2 1 3
1 2
1 2

6
2 3 4 5 6 7
2 2 3
2 1 3
2 1 2
2 5 6
2 4 6
2 4 5
"""