# BOJ - 3671
from itertools import permutations
p = [True] * 10_000_000
for i in range(2, 10_000_000):
    if p[i]:
        for j in range(i*i, 10_000_000, i):
            p[j] = False
p[1] = False
for _ in range(int(input())):
    a = input()
    ans = 0
    l = set()
    for i in range(1, len(a)+1):
        for permu in permutations(a, i):
            if permu[0] == "0": continue
            t = int(''.join(permu))
            if p[t] and t not in l:
                ans += 1
                l.add(t)
    print(ans)
"""
4
17
1276543
9999999
011
"""