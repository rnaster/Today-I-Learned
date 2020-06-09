# BOJ - 1028
import sys
read = sys.stdin.readline
# n, m = map(int, read().split())
# arr = [read() for _ in range(n)]
import random
n, m = 5, 7
arr = [[random.choice(['0', '1']) for _ in range(m)] for _ in range(n)]
# arr = ['1' * m for _ in range(n)]
# arr = [['1', '1', '0'], ['0', '0', '1'], ['0', '1', '0'], ['1', '1', '1'], ['1', '1', '1'], ['0', '0', '1'], ['0', '0', '0']]
print(*arr, sep='\n')
l1 = [[0] * (m+1) for _ in range(n+1)]
l2 = [[0] * (m+1) for _ in range(n+1)]
l3 = [[0] * (m+1) for _ in range(n+1)]
l4 = [[0] * (m+1) for _ in range(n+1)]
for j in range(m):
    i = 1
    ii = -1
    jj = j
    for k in range(min(j+1, n)):
        if arr[i-1][j] == '1':
            l1[i][j] = l1[i-1][j+1] + 1
        if arr[ii][j] == '1':
            l2[ii][j] = l2[ii+1][j+1] + 1
        i += 1
        j -= 1
        ii -= 1
    i = 0
    ii = -1
    for k in range(min(n, m-jj)):
        if arr[i][jj] == '1':
            l3[i+1][jj] = l3[i][jj-1] + 1
        if arr[ii][jj] == '1':
            l4[ii][jj] = l4[ii+1][jj-1] + 1
        i += 1
        jj += 1
        ii -= 1
for i in range(1, n):
    j = m-1
    ii = -i-1
    iii = i
    for k in range(min(n-i, m)):
        if arr[i][j] == '1':
            l1[i+1][j] = l1[i][j+1] + 1
        if arr[ii][j] == '1':
            l2[ii][j] = l2[ii+1][j+1] + 1
        i += 1
        j -= 1
        ii -= 1
    j = 0
    for k in range(min(n-iii, m)):
        if arr[iii][j] == '1':
            l3[iii+1][j] = l3[iii][j-1] + 1
        if arr[-iii-1][j] == '1':
            l4[-iii-1][j] = l4[-iii][j-1] + 1
        iii += 1
        j += 1
ans = 0
for i in range(n):
    for j in range(m):
        t = min(l1[i+1][j], l2[i+1][j])
        for k in range(t, 0, -1):
            if j+2*k-2 < m:
                ans = max(ans, min(k, l3[i+1][j+2*k-2], l4[i+1][j+2*k-2]))
                break
        t = min(l3[i+1][j], l4[i+1][j])
        for k in range(t, 0, -1):
            if -1 < j - 2*t+2:
                ans = max(ans, min(k, l1[i+1][j-2*t+2], l2[i+1][j-2*t+2]))
                break
print(ans)
# print(*l1, '', sep='\n')
# print(*l2, '', sep='\n')
"""
1,406,114

5 5
11101
01011
11111
01111
11111

5 5
00101
01011
11010
00011
00111

2 2
11
11

6 5
11101
01011
11111
01111
11111
11111

3 6
111111
111111
111111
"""