# BOJ - 2281
import sys
sys.setrecursionlimit(10000000)
read = lambda: sys.stdin.readline().rstrip()
n, m = map(int, read().split())
arr = [int(read()) for _ in range(n)]
dp = [[-1] * (m+1) for _ in range(n)]
def func(a, b):
    if a == n-1: dp[a][b] = 0; return dp[a][b]
    if b > arr[a+1]:
        t1 = dp[a+1][b-arr[a+1]-1] if dp[a+1][b-arr[a+1]-1] != -1 else func(a+1, b-arr[a+1]-1)
        t2 = dp[a+1][m-arr[a+1]] + b*b if dp[a+1][m-arr[a+1]] != -1 else func(a+1, m-arr[a+1]) + b*b
        dp[a][b] = min(t1, t2)
    else:
        dp[a][b] = dp[a+1][m-arr[a+1]] + b*b if dp[a+1][m-arr[a+1]] != -1 else func(a+1, m-arr[a+1]) + b*b
    return dp[a][b]
print(func(0, m-arr[0]))
print(*dp, sep='\n')
"""
11 20
7
4
2
3
2
5
1
12
7
5
6

3 5
5
5
5
"""
sys.exit()

# BOJ - 10527
import sys
import collections
def read(): return sys.stdin.readline().rstrip()
n = int(read())
d1 = collections.defaultdict(int)
d2 = collections.defaultdict(int)
for _ in range(n):
    d1[read()] += 1
for _ in range(n):
    d2[read()] += 1
ans = 0
for k in d1.keys() & d2.keys():
    ans += min(d1[k], d2[k])
print(ans)
"""
5
correct
wronganswer
correct
correct
timelimit
wronganswer
correct
timelimit
correct
timelimit
"""
sys.exit()

# BOJ - 15900
import sys
import collections
read = lambda: sys.stdin.readline().rstrip()
n = int(read())
d = collections.defaultdict(list)
for _ in range(n-1):
    a, b = map(int, read().split())
    d[a].append(b); d[b].append(a)
visit = [0] * (n+1)
ans = 0
q = [(1, 0)]
while q:
    a, h = q.pop()
    visit[a] = 1
    temp = True
    for i in d[a]:
        if visit[i] == 0:
            temp = False
            q.append((i, h+1))
    if temp: ans += h
if ans % 2: print('Yes')
else: print('No')
"""
8
8 1
1 4
7 4
6 4
6 5
1 3
2 3

4
4 1
3 2
2 1
"""