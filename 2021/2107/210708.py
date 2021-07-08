# BOJ - 10775
import sys
sys.setrecursionlimit(1000000)
read = sys.stdin.readline
g = int(read())
arr = [[-1] * (g+1), [1] * (g+1)]
arr[1][0] = 0
def find(i):
    if arr[0][i] == -1:
        return i
    arr[0][i] = find(arr[0][i])
    return arr[0][i]
ans = 0
for _ in range(int(read())):
    a = int(read())
    if arr[1][a]:
        ans += 1
        arr[1][a] = 0
        arr[0][a] = a-1
    else:
        i = find(a)
        if arr[1][i]:
            ans += 1
            arr[1][i] = 0
            arr[0][i] = i-1
        else:
            break
print(ans)
"""
4
6
2
2
3
3
4
4
"""
exit()

# BOJ - 1715
import sys
from heapq import *
read = sys.stdin.readline
arr = [int(read()) for _ in range(int(read()))]
heapify(arr)
ans = 0
t = -1
while arr:
    if t < 0:
        t = heappop(arr)
    else:
        t += heappop(arr)
        heappush(arr, t)
        ans += t
        t = -1
print(ans)
"""
3
10
20
40
"""