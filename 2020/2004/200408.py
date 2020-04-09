# BOJ - 2467
n = int(input())
arr = [*map(int, input().split())]
def func(i):
    a, b = i, n-1
    c = b
    while a < c < b:
        s = arr[i] + arr[c]
        if s == 0: break
        elif s > 0: b = c-1
        else: a = c
        c = (a+b+1) // 2
    return c
s = 2_000_000_001
a, b = 0, 1
for i in range(n-1):
    j = func(i)
    print(i, j)
    t = abs(arr[i] + arr[j])
    if s > t:
        a, b = i, j
        s = t
print(arr[a], arr[b])
"""
8
-1000000 -99 99 100 101 102 103 104 105

6
-100 -99 -98 -97 1 2

6
100 99 98 97 -1 -2

5
-1 -2 -3 -4 -5
"""