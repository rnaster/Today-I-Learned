# BOJ - 10253
from sys import stdin, stdout
read = lambda: stdin.readline().rstrip()
write = lambda x: stdout.write(str(x) + '\n')
for _ in range(int(read())):
    a, b = map(int, read().split())
    while True:
        x = b / a
        if int(x) == x: write(int(x));break
        else:
            x = int(x) + 1
            a, b = a * x - b, b * x
"""
3
4 23
5 7
8 11
"""