# BOJ - 2591
N = input()
if N[0] == '0': print(0); exit()
if len(N) == 1: print(1); exit()
if N[:2] in ('10', '20', '30'): a, b = 0, 1
elif '11' <= N[:2] <= '34': a, b = 1, 2
else: a, b = 1, 1
for i in range(2, len(N)):
    temp = 0
    if N[i] != '0': temp += b
    if '10' <= N[i-1:i+1] <= '34': temp += a
    a, b = b, temp
print(b)
"""
27123
"""