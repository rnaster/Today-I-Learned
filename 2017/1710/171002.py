# BOJ - 1038
def foo():
    from sys import stdout
    n = int(input())
    if n > 1022:
        stdout.write(str(-1))
    else:
        l = [str(i) for i in range(10)]
        tp = tuple(l)
        for _ in range(2, 11):
            temp = []
            for i in range(0, 10):
                for val in tp:
                    if str(i) > val:
                        temp.append(str(i)+val)
                    else: break
            l.extend(temp)
            tp = tuple(temp)
            del temp
        stdout.write(str(l[n]))

    # BOJ - 2410
    from sys import stdout
    from array import array
    n = int(input())
    arr = array('l', [1 for _ in range(n+1)])
    coin = array('l', [])
    num = 2
    while num <= n:
        coin.append(num)
        num *= 2
    for c in coin:
        for i in range(c, n+1):
            arr[i] = (arr[i-c] + arr[i]) % 1000000000
    stdout.write(str(arr[-1]))

    # n = int(input())//2
    # a = [0]*(n+1)
    # a[0] = 1
    # for i in range(1,n+1):
    #     a[i] = (a[i-1]+a[i//2])%1000000000
    # print(a)