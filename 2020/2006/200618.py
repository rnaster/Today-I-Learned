# BOJ - 6549
import sys
read = sys.stdin.readline
while 1:
    arr = map(int, read().split())
    n = next(arr)
    if n == 0: break
    ans = 0
    l = []
    b = -1
    for i, a in enumerate(arr):
        if a < b:
            jj = 0
            while l:
                j, c = l[-1]
                if a < c:
                    ans = max(ans, a * (i - j + 1), c * (i - j))
                    l.pop()
                    jj = j
                else:
                    break
            l.append((jj, a))
        else:
            l.append((i, a))
        b = a
    while l:
        j, c = l.pop()
        ans = max(ans, c * (n - j))
    print(ans)
"""
7 2 1 4 5 1 3 3
4 1000 1000 1000 1000
7 0 5 2 1 2 10 1
5 0 1 0 0 2
4 1 4 3 3
10 1 2 3 4 5 0 4 3 2 1
6 3 2 1 1 2 3
0
"""
