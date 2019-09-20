# BOJ - 15684
from itertools import combinations
n, m, h = map(int, input().split())
index = set()
for _ in range(m):
    index.add(tuple(map(int, input().split())))
def func_(idx):
    b = idx
    for a in range(1, h+1):
        if (a, b) in index:
            b += 1
        elif (a, b-1) in index:
            b += -1
    return b == idx
add_ = set()
for i in range(1, h+1):
    for j in range(1, n):
        if (i, j) not in index and\
                (i, j-1) not in index and\
                (i, j+1) not in index:
            add_.add((i, j))
def func():
    for i in range(1, n+1):
        if not func_(i): return False
    return True
if func(): print(0); exit()
for i in range(1, 4):
    for combs in combinations(add_, i):
        skip = False
        for (a, b) in combs:
            if (a, b-1) in combs or (a, b+1) in combs:
                skip = True
                break
        if skip: continue
        for comb in combs:
            index.add(comb)
        if func(): print(i); exit()
        for comb in combs:
            index.remove(comb)
print(-1)
"""
5 5 6
1 1
3 2
2 3
5 1
5 4

5 6 6
1 1
3 1
5 2
4 3
2 3
1 4
"""
exit()

# BOJ - 17070
n = int(input())
arr = [[*map(int, input().split())] for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0][1] = 1
def func(i, a, b):
    if (a, b) == (n-1, n-1):
        return
    if i == 0:
        if b+1 < n and arr[a][b+1] < 1:
            dp[a][b+1] += dp[a][b]
            func(0, a, b+1)
            if a + 1 < n and arr[a+1][b+1] + arr[a+1][b] < 1:
                dp[a+1][b+1] += dp[a][b]
                func(2, a+1, b+1)
    elif i == 1:
        if a + 1 < n and arr[a+1][b] < 1:
            dp[a+1][b] += dp[a][b]
            func(1, a+1, b)
            if b + 1 < n and arr[a+1][b+1] + arr[a][b+1] < 1:
                dp[a+1][b+1] += dp[a][b]
                func(2, a+1, b+1)
    else:
        if a + 1 < n and b + 1 < n and arr[a+1][b+1] + arr[a][b+1] + arr[a+1][b] < 1:
            dp[a+1][b+1] += dp[a][b]
            func(2, a+1, b+1)
            dp[a+1][b] += dp[a][b]
            func(1, a+1, b)
            dp[a][b+1] += dp[a][b+1]
            func(0, a, b+1)
    if (a, b) in ((1, 5), (1, 4), (0, 5), (0, 4)):
        print(dp[a][b], '(i, a, b): (%s, %s, %s)' % (i, a, b))
        print('dp[1][5]: %s' % dp[1][5])
    return
func(0, 0, 1)
print(*dp, sep='\n')
"""
5
0 0 1 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0

6
0 0 0 0 0 0
0 1 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
"""
exit()

# BOJ - 16637
n = int(input())
s = [*input()]
d = {'+': lambda x, y: int(x) + int(y),
     '-': lambda x, y: int(x) - int(y),
     '*': lambda x, y: int(x) * int(y)}
def func(a, b):
    if len(b) < 2:
        a += b
        val = int(a[0])
        i = 1
        while i < len(a):
            o = a[i]
            bb = a[i+1]
            val = d[o](val, bb)
            i += 2
        return val
    aa = a[:]
    aaa = a[:]
    aa.append(d[b[1]](b[0], b[2]))
    if len(b) > 3: aa.append(b[3])
    aaa.extend(b[:2])
    return max(func(aa, b[4:]), func(aaa, b[2:]))
print(func([], s))
"""
9
3+8*7-9*2

19
1*2+3*4*5-6*7*8*9*0

19
1*2+3*4*5-6*7*8*9*9
"""