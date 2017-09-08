#BOJ - 3012
from sys import stdin
from array import array
read = lambda: stdin.readline().rstrip()
n, m = map(int, read().split())
tp = tuple(map(int, read().split()))
arr1 = array('l', [0 for _ in range(m)])
arr2 = array('l', [0 for _ in range(m)])
for i in range(m):
    arr1[i] = sum(tp[:i+1])
for _ in range(m-1):
    tp = tuple(map(int, read().split()))

print(arr2)
'''
 10   38   42   50   63
 |    |    |    |    |
 * <- @ <- @ <- @ <- @
'''