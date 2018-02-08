# BOJ - 10942
from sys import stdin, stdout
from array import array
read = lambda: stdin.readline().rstrip()
n = int(read())
arr = array('B', [0 for _ in range(n*n)])
def get_elem(two_d_array, a, b, width=n):
    return two_d_array[a*width + b]
def set_elem(two_d_array, a, b, value, width=n):
    two_d_array[a*width + b] = value
tp = tuple(map(int, read().split()))
for i in range(n):
    set_elem(arr, i, i, 1)
    u, d = i, i
    while 0 <= u < n and 0 <= d < n:
        if tp[u] != tp[d]: break
        else:
            set_elem(arr, u, d, 1)
            u -= 1; d += 1
for i in range(n-1):
    u, d = i, i+1
    while 0 <= u < n and 0 <= d < n:
        if tp[u] != tp[d]: break
        else:
            set_elem(arr, u, d, 1)
            u -= 1; d += 1
for _ in range(int(read())):
    s, e = map(int, read().split())
    stdout.write(str(get_elem(arr, s-1, e-1) or get_elem(arr, e-1, s-1))+'\n')