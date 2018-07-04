# BOJ - 2666
from copy import deepcopy
n = int(input())
cache = [[0 for _ in range(n)] for _ in range(n)]
a, b = map(int, input().split())
s = {(a, b)}
ans = 400
for _ in range(int(input())):
    c = int(input())
    tmp_s = set()
    tmp_cache = [[400 for _ in range(n)] for _ in range(n)]
    print(s, c)
    for a, b in s:
        print(a, b)
        if a <= c <= b:
            tmp_s.add((c, b))
            tmp_cache[c-1][b-1] = min(tmp_cache[c-1][b-1], cache[a-1][b-1] + c - a)
            tmp_s.add((a, c))
            tmp_cache[a-1][c-1] = min(tmp_cache[a-1][c-1], cache[a-1][b-1] + b - c)
            ans = min(tmp_cache[c-1][b-1], tmp_cache[a-1][c-1], ans)
        elif a > c:
            tmp_s.add((c, b))
            tmp_cache[c - 1][b - 1] = min(tmp_cache[c - 1][b - 1], cache[a - 1][b - 1] + a - c)
            ans = min(tmp_cache[c-1][b-1], ans)
        else:
            tmp_s.add((a, c))
            tmp_cache[a - 1][c - 1] = min(tmp_cache[a - 1][c - 1], cache[a - 1][b - 1] + b - c)
            ans = min(tmp_cache[a-1][c-1], ans)
    s = tmp_s.copy()
    cache = deepcopy(tmp_cache)
    print(ans, '\n')

"""
7
2 5
4
3
1
6
5
"""
