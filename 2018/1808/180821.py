# BOJ - 15954
# l = list(range(1, 1000001))
# v = sum(map(lambda x: x ** 2, l)) / len(l) - (sum(l) / len(l)) ** 2
# print(v / len(l))
ans = 83334
n, k = map(int, input().split())
if k == 1: print(0); exit()
tp = tuple(map(int, input().split()))
for i in range(n-k+1):
    m = sum(tp[i:i+k]) / k
    v = sum(map(lambda x: x ** 2, tp[i:i+k])) / k - m ** 2
    ans = min(ans, v ** (0.5))

print(ans)
"""
5 3
1 2 3 4 5
10 1
1 4 1 5 9 2 6 5 3 5
0.9428090415820655
"""