# BOJ - 1398
import sys
from bisect import bisect_right as bi
read = sys.stdin.readline
l = [10**i for i in range(16)] + [25*100**i for i in range(7)]
l.sort()
for _ in range(int(input())):
    a = int(read())
    ans = 0
    i = bi(l, a) - 1
    while a > 0:
        p, a = divmod(a, l[i])
        ans += p
        i = bi(l, a) - 1
    print(ans)
"""
2
9981
1000000000000000
"""
exit()

# BOJ - 2885
import math
k = int(input())
ans = n = 2 ** math.ceil(math.log2(k))
ans2 = 0
while k > 0:
    if k >= n:
        k -= n
    else:
        n //= 2
        ans2 += 1
print(ans, ans2)
"""
6
"""