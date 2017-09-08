def foo():
    #BOJ - 2965.
    a, b, c = map(int, input().split())
    count = 0
    while not (abs(a-b) == 1 and abs(b-c) == 1):
        if abs(a-b) < abs(b-c):
            a, b = b, c-1; count += 1
        else:
            b, c = a+1, b; count += 1
    print(count)

    #BOJ - 9084
    from sys import stdin
    from array import array
    read = lambda: stdin.readline().rstrip()
    for _ in range(int(read())):
        n = int(read())
        coin = tuple(map(int, read().split()))
        m = int(read())
        arr = array('L', [1] + [0 for _ in range(m)])
        for c in coin:
            for i in range(c, m+1):
                arr[i] += arr[i-c]
        print(arr[-1])

#BOJ - 11060
from sys import stdin
from array import array
read = lambda: stdin.readline().rstrip()
n = int(read())
tp = tuple(map(int, read().split()))
arr = array('L', [0 for _ in range(n+100)])
for i in range(1, tp[0]+1):
    arr[i] += 1
for i in range(1, n):
    for t in range(i+1, i + tp[i]+1):
        if arr[t] == 0:
            if arr[i] == 0: continue
            arr[t] = arr[i] + 1
        else:
            arr[t] = min(arr[i]+1, arr[t])
if tp[0] == 0: print(0)
else: print(arr[n-1])