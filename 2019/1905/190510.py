# BOJ - 1072
import math
x, y = map(int, input().split())
if (x-y)*100 - x <= 0: print(-1);exit()
print(math.ceil(x / (99-100*y/x)))
exit()

# BOJ - 4344
import sys
read = lambda: sys.stdin.readline().rstrip()
for _ in range(int(read())):
    arr = [*map(int, read().split())]
    m = sum(arr[1:]) / arr[0]
    for i in range(arr[0]):
        if arr[i] > m: print(i)
    print("%.3f%%" % round(sum([1 for a in arr[1:] if a > m]) / arr[0] * 100, 3))
"""
6
5 50 50 70 80 100
7 100 95 90 80 70 60 50
3 70 90 80
3 70 90 81
9 100 99 98 97 96 95 94 93 91
3 0 0 0
"""