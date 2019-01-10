# BOJ - 2810
n = int(input())
a = input()
if n == 1: print(1);exit()
ans = 0
s = 0
for aa in a:
    if aa == 'S': s += 1
ans += s + (n-s) // 2 + 1
print(min(ans, n))
"""
9
SLLLLSSLL

10
SLLLLSSLLS

3
SSS

2
LL
"""