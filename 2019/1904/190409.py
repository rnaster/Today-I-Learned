# BOJ - 1722
import math
n, arr = int(input()), tuple(map(int, input().split()))
def func1(a, b):
    cache = [0] * (n+1)
    for i in range(a-1, -1, -1):
        p, b = divmod(b, math.factorial(i))
        for j in range(1, n+1):
            if cache[j] == 0:
                if p > 0: p -= 1
                else: print(j, end=' '); cache[j] = 1; break
def func2(a, tp):
    ans = 0
    cache = [0]*(n+1)
    for i in tp:
        k = 0
        cache[i] = 1
        for j in range(1, i):
            if cache[j] < 1: k += 1;
        a -= 1
        ans += k*math.factorial(a)
    return ans + 1
if arr[0] > 1: print(func2(n, arr[1:-1]))
else: func1(n, arr[1]-1)
"""
4
2 2 4 1 3

4
2 1 4 3 2

4
1 3
"""