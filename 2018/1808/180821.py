# BOJ - 15954
# l = list(range(1, 1000001))
# v = sum(map(lambda x: x ** 2, l)) / len(l) - (sum(l) / len(l)) ** 2
# print(v / len(l))
import math
ans = math.inf
n, k = map(int, input().split())
tp = tuple(map(int, input().split()))
tp_ = tuple(map(lambda x: x * x, tp))
for i in range(n-k+1):
    for j in range(k):
        m = sum(tp[i:i+k+j]) / (k + j)
        v = sum(tp_[i:i+k+j]) / (k + j) - m * m
        ans = min(ans, math.sqrt(v))
print(ans)
"""
5 3
1 2 3 4 5
10 3
1 4 1 5 9 2 6 5 3 5
0.9428090415820655
"""