# BOJ - 13398
from sys import stdin
from array import array
read = lambda : stdin.readline().rstrip()
n = int(read())
tp = tuple(map(int, read().split()))
if n < 2: print(tp[0]); quit()
dp_0 = array('l', [0 for _ in range(n)])
dp_1 = array('l', [0 for _ in range(n)])
dp_0[0] = tp[0]
dp_0[1] = max(dp_0[0] + tp[1], tp[1])
dp_1[1] = dp_0[0]
ans = max(dp_1[1], dp_0[1])
for i in range(2, n):
    dp_0[i] = max(dp_0[i-1] + tp[i], tp[i])
    dp_1[i] = max(dp_1[i-1] + tp[i], dp_0[i-2] + tp[i], tp[i])
    ans = max(ans, dp_0[i], dp_1[i])
print(ans)
'''
10
10 -4 3 1 5 6 -35 12 21 -1
'''