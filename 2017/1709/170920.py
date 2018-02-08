# BOJ - 11055
def foo():
    from array import array
    from sys import stdout, stdin
    read = lambda: stdin.readline().rstrip()
    n = int(read())
    tp = tuple(map(int, read().split()))
    arr = array('L', [tp[0]] + [0 for _ in range(n-1)])
    M = arr[0]
    for i in range(1, n):
        if tp[i-1] < tp[i]: arr[i] += tp[i] + arr[i-1]
        else:
            for j in range(i-1, -1, -1):
                if tp[j] < tp[i]: arr[i] += arr[j] + tp[i]; break
            if arr[i] == 0: arr[i] = tp[i]
        M = max(M, arr[i])
    stdout.write(str(M))
