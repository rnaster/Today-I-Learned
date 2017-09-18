# BOJ - 10164
def foo():
    from sys import stdout, stdin
    read = lambda: stdin.readline().rstrip()
    m, n, k = map(int, read().split())
    def func(a, b):
        f = 1
        if a > b: a, b = b, a
        for i in range(1, a+1):
            f *= (a+b-i+1)
            f //= i
        return f
    if k == 0: stdout.write(str(func(m-1, n-1)) + '\n')
    elif k == n or k == (m-1)*n+1: stdout.write('1\n')
    elif k % n == 0: a = k // n; stdout.write(str(func(a-1, n-1)) + '\n')
    else:
        a = k // n
        b = k % n
        stdout.write(str(func(a, b-1) * func(m-a-1, n-b)) + '\n')

    # BOJ - 3943
    from sys import stdout, stdin
    read = lambda: stdin.readline().rstrip()
    for _ in range(int(read())):
        M = 1
        n = int(read())
        while n != 1:
            M = max(M, n)
            if n % 2: n = n*3 + 1
            else: n //= 2
        stdout.write(str(M) + '\n')

# BOJ - 1660
from sys import stdout, stdin
from array import array
read = lambda: stdin.readline().rstrip()
arr = array('l', [i*(i+1)*(i+2)//6 for i in range(120, 0, -1)])
# n = int(read())
# count = 0
# while arr:
#     print(n)
#     if n >= arr[0]: n -= arr[0]; count += 1
#     arr = arr[1:]
# print(n)
# stdout.write(str(count)+'\n')