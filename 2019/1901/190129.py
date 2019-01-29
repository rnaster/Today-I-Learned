# BOJ - 2775
from sys import stdin
read = lambda: stdin.readline().rstrip()
cache = [[0] * 15 for _ in range(15)]
for i in range(15):
    cache[0][i] = i
for i in range(1, 15):
    for j in range(1, 15):
        cache[i][j] = cache[i-1][j] + cache[i][j-1]
for _ in range(int(read())):
    k, n = int(read()), int(read())
    print(cache[k][n])
"""
2
1
3
2
3
"""
exit()
# BOJ - 2438
n = int(input())
for i in range(1, n+1):
    for j in range(1, i+1):
        print('*', end='')
    print()
exit()
# BOJ - 2749
n = int(input()) % 1500000
a, b = 0, 1
for _ in range(n-1):
    a, b = b, (a+b) % 1000000
print(b)
