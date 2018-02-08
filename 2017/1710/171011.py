# BOJ - 1915
import numpy as np
from sys import stdin
read = lambda: stdin.readline().rstrip()
n, m = map(int, read().split())
arr = []
for _ in range(n):
    arr.append(list(read()))
arr = np.array(arr).astype(int)
def rectangle(i, j, n):
    if arr[i-n+1:i+1, j-n+1:j+1].sum() == n**2: return n**2
    else: return 0
ans = 0
for i in range(n):
    for j in range(m):
        if arr[i, j] == 0: continue
        for N in range(1, min(i+1, j+1)+1):
            ans = max(ans, rectangle(i, j, N))
print(ans)
'''
3 7
0110111
0001111
0110011

7 3
000
101
101
010
111
111
111

4 4
1100
1111
0111
0111

6 6
111110
111110
111111
111111
111111
001111

5 10
1111111111
0000000010
0000010110
0000010100
0000000000

'''