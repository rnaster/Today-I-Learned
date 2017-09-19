def foo():
    # BOJ - 9498
    from bisect import bisect_left as left
    g = ['F', 'D', 'C', 'B', 'A']
    l = [59, 69, 79, 89, 100]
    print(g[left(l, int(input()))])

    # BOJ - 1924
    l = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    d = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    x, y = map(int, input().split())
    print(d[(sum(l[:x-1]) + y) % 7 -1])

    # BOJ - 10871
    n, X = map(int, input().split())
    tp = tuple(map(int, input().split()))
    print(*tuple(filter(lambda x: x<X, tp)))

    # BOJ - 2839
    from array import array
    n = int(input())
    arr = array('l', [0 for _ in range(n+1)])
    idx = 3
    while idx <= n:
        arr[idx] += arr[idx-3] + 1
        idx += 3
    if n >= 5:
        arr[5] = 1
        for i in range(6, n+1):
            if arr[i-5] != 0 and arr[i-3] != 0: arr[i] = min(arr[i-5], arr[i-3]) + 1
            elif arr[i-3] == 0 and arr[i-5] != 0: arr[i] += arr[i-5] + 1
    if arr[-1] == 0: print(-1)
    else: print(arr[-1])