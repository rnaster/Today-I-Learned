# BOJ - 10830
import sys
read = sys.stdin.readline
n, m = map(int, read().split())
arr = [[*map(int, read().split())] for _ in range(n)]
def func(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(n)) % 1000
             for j in range(n)]
            for i in range(n)]
def dq(l, b):
    if b == 1:
        return [[l[i][j] % 1000 for j in range(n)]
                for i in range(n)]
    ll = dq(l, b // 2)
    tmp = func(ll, ll)
    if b % 2 == 0:
        return tmp
    return func(tmp, l)
for a in dq(arr, m):
    print(*a)
"""
2 1
1000 1000
1000 1000

3 3
1 2 3
4 5 6
7 8 9

5 10
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1
"""
exit()

# BOJ - 1138
n = int(input())
ans = [0] * n
for i, j in enumerate(map(int, input().split()), 1):
    a = ans[:j].count(0)
    if a == j and ans[j] == 0:
        ans[j] = i
    else:
        for k in range(j, n):
            if ans[k] == 0:
                if a == j:
                    ans[k] = i
                    break
                a += 1
print(*ans)
"""
5
1 2 1 1 0

4
2 1 1 0

4
0 0 0 0

5
2 1 0 1 0
"""