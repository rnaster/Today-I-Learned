#BOJ - 5557
def foo():
    from sys import stdin
    from array import array
    read = lambda: stdin.readline().rstrip()
    n = int(read())
    tp = tuple(map(int, read().split()))
    arr = array('H',[0 for _ in range(21)])
    arr[tp[0]] = 1
    for i in tp[1:-1]:
        temp = array('H', [0 for _ in range(21)])
        for j in range(21):
            if arr[j] == 0: continue
            else:
                if 0 <= j - i <= 20: temp[j-i] += arr[j]
                if 0 <= j + i <= 20: temp[j+i] += arr[j]
        arr = temp[:]
    print(arr[tp[-1]])

    #BOJ - 2240
    from sys import stdin
    from array import array
    read = lambda: stdin.readline().rstrip()
    t, w = map(int, read().split())
    arr = array('H',[0 for _ in range(w+1)])
    idx = 2
    for _ in range(t):
        a = int(read())
        temp = arr[:]
        for i in range(idx):
            pos = i % 2 + 1
            if i == 0:
                if pos == a: temp[0] += 1
            elif pos == a:
                temp[i] = max(arr[i], arr[i-1]) + 1
            else:
                temp[i] = max(arr[i], arr[i-1])
        if idx <= w:
            idx += 1
        arr = temp[:]
    print(max(arr))
