# BOJ - 10942
from sys import stdin, setrecursionlimit
setrecursionlimit(10000000)
read = lambda : stdin.readline().rstrip()
n = int(read())
arr = tuple(map(int, read().split()))
dp = [[-1 for _ in range(n+1)] for _ in range(n+1)]
def func(s, e):
    global dp
    if not (1 <= s <= n and 1 <= e <= n and s <= e): return 1
    if dp[s][e] == -1:
        if arr[s-1] == arr[e-1]:
            dp[s][e] = 1 * func(s+1, e-1)
        else:
            dp[s][e] = 0
    return dp[s][e]

for _ in range(int(read())):
    s, e = map(int, read().split())
    print(func(min(s, e), max(s, e)))

'''
7
1 2 1 3 1 2 1
4
1 3
2 5
3 3
5 7
'''

# BOJ - 1793
from sys import stdin
for n in map(int, stdin.read().split()):
    if n < 0: quit()
    a, b = 1, 3
    for _ in range(n-2):
        a, b = b, a*2 + b
    if n < 2:
        print(1)
    else:
        print(b)