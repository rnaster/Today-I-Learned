#BOJ - 3012
from sys import stdin
from array import array
read = lambda: stdin.readline().rstrip()
n, m = map(int, read().split())
tp = tuple(map(int, read().split()))
arr1 = array('l', [-101 for _ in range(m)])
arr2 = array('l', [-101 for _ in range(m)])
for i in range(m):
    arr1[i] = sum(tp[:i+1])
for _ in range(m-1):
    tp = array('l', tuple(map(int, read().split())))
    for i in range(m):
        # arr2[i] = max(array('i', [sum(array('l', tp[j:i + 1]) + arr1[j:j + 1]) for j in range(i + 1)] +
        #               [sum(array('l', tp[i:j + 1]) + arr1[j:j + 1]) for j in range(i + 1, m)]))
        for j in range(i+1):
            arr2[i] = max(arr2[i], sum(tp[j:i + 1] + arr1[j:j + 1]))
        for j in range(i+1, m):
            arr2[i] = max(arr2[i], sum(tp[i:j + 1] + arr1[j:j + 1]))
    print(arr1,'*')
    print(arr2,'**')
    arr1 = arr2[:]
print(arr2[-1])

'''
 10   38   42   50   63
 |    |    |    |    |
 * <- @ <- @ <- @ <- @
'''