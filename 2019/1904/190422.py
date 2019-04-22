# BOJ - 14889
from itertools import combinations
n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]
d = {}
def func(l):
    val = 0
    for comb in combinations(l, 2):
        if comb in d: val += d[comb]
        else:
            i, j = comb
            d[comb] = arr[i][j] + arr[j][i]
            val += d[comb]
    return val
def main():
    ans = 987654321
    for comb in combinations(range(n), n//2):
        l = list(range(n))
        for c in comb: l.remove(c)
        a = func(comb)
        b = func(l)
        ans = min(ans, abs(a-b))
        if ans == 0: return 0
    return ans
print(main())

"""
4
0 1 2 3
4 0 5 6
7 1 0 2
3 4 5 0

6
0 1 2 3 4 5
1 0 2 3 4 5
1 2 0 3 4 5
1 2 3 0 4 5
1 2 3 4 0 5
1 2 3 4 5 0

8
0 5 4 5 4 5 4 5
4 0 5 1 2 3 4 5
9 8 0 1 2 3 1 2
9 9 9 0 9 9 9 9
1 1 1 1 0 1 1 1
8 7 6 5 4 0 3 2
9 1 9 1 9 1 0 9
6 5 4 3 2 1 9 0

(0, 1) 9
(0, 3) 14
(0, 4) 5
(1, 3) 10
(1, 4) 3
(3, 4) 10
(0, 1, 3) 33 = 9 + 14 + 10
(0, 1, 4) 17 = 9 + 5 + 3
(0, 3, 4) 29 = 14 + 5 + 10
(1, 3, 4) 23 = 10 + 3 + 10
(0, 1, 3, 4) 102 
############################
(2, 5) 9
(2, 6) 10
(2, 7) 6
(5, 6) 4
(5, 7) 3
(6, 7) 18
(2, 5, 6) 23 = 9 + 10 + 4
(2, 5, 7) 18 = 9 + 6 + 3
(2, 6, 7) 34 = 10 + 6 + 18
(5, 6, 7) 25 = 4 + 3 + 18
(2, 5, 6, 7) 100
"""