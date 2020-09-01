# BOJ - 1342
import math
from itertools import permutations
from collections import Counter
a = input()
ans = 0
for permu in permutations(a):
    flag = 1
    for i in range(len(a)-1):
        if permu[i] == permu[i+1]:
            flag = 0
            break
    ans += flag
for _, v in Counter(a).items():
    ans //= math.factorial(v)
print(ans)
exit()

# BOJ - 3980
import sys
read = sys.stdin.readline
arr = []
def func(a, b):
    val = -99999
    if a == 10:
        for i in range(11):
            if arr[a][i] > 0 and not b & 1 << i:
                val = max(val, arr[a][i])
        return val
    for i in range(11):
        if arr[a][i] > 0 and not b & 1 << i:
            val = max(val, arr[a][i] + func(a+1, b | 1 << i))
    return val
for _ in range(int(read())):
    arr = [[*map(int, read().split())] for _ in range(11)]
    print(func(0, 0))
"""
1
100 0 0 0 0 0 0 0 0 0 0
0 80 70 70 60 0 0 0 0 0 0
0 40 90 90 40 0 0 0 0 0 0
0 40 85 85 33 0 0 0 0 0 0
0 70 60 60 85 0 0 0 0 0 0
0 0 0 0 0 95 70 60 60 0 0
0 45 0 0 0 80 90 50 70 0 0
0 0 0 0 0 40 90 90 40 70 0
0 0 0 0 0 0 50 70 85 50 0
0 0 0 0 0 0 66 60 0 80 80
0 0 0 0 0 0 50 50 0 90 88
"""