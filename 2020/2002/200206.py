# BOJ - 2529
n = int(input())
arr = input().split()
def func(a, l, b):
    ans = [-1] * (n + 1)
    i, j = 0, 0
    while j < n:
        if arr[j] == a:
            for k in range(j, i - 1, -1):
                ans[k] = l
                l += b
            i = j + 1
        j += 1
    for k in range(j, i - 1, -1):
        ans[k] = l
        l += b
    for i in range(n + 1):
        if ans[i] < 0:
            ans[i] = l
            l += b
    print(''.join(map(str, ans)))
    return
func('>', 9, -1)
func('<', 0, 1)
"""
2
< > 

9
< < < > < < > < >

3
< < <

4
> > > <
"""
exit()

# BOJ - 1946
import sys
read = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    arr = [[*map(int, read().split())] for _ in range(n)]
    arr.sort()
    ans = 1
    a = arr[0][1]
    for i in range(1, n):
        if a == 1: break
        _, b = arr[i]
        if a > b:
            ans += 1
            a = b
    print(ans)
"""
2
5
3 2
1 4
4 1
2 3
5 5
7
3 6
7 3
4 2
1 4
5 7
2 5
6 1
"""