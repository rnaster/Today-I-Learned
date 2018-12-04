# BOJ - 8979
from sys import stdin
read = lambda: stdin.readline().rstrip()
n, k = map(int, read().split())
l = []
ans = 0
for _ in range(n):
    i, g, s, b = map(int, read().split())
    l.append((g, s, b))
    if i == k: g_k, s_k, b_k = g, s, b
s_l = []
for i in range(n):
    if l[i][0] > g_k: ans += 1
    if l[i][0] == g_k: s_l.append(i)
if s_l == []: print(ans + 1);exit()
b_l = []
for i in s_l:
    if l[i][1] > s_k: ans += 1
    if l[i][1] == s_k: b_l.append(i)
if b_l == []: print(ans+1);exit()
for i in b_l:
    if l[i][2] > b_k: ans += 1
print(ans + 1)
"""
4 3
2 0 1 0
3 0 1 0
1 1 2 0
4 0 0 1

6 3
1 
"""