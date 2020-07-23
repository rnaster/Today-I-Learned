# BOJ - 1197
import sys
sys.setrecursionlimit(1000000)
read = sys.stdin.readline
n, m = map(int, read().split())
arr = sorted([[*map(int, read().split())] for _ in range(m)],
             key=lambda x: x[-1])
l = [-1] * (n+1)
def find(a):
    if l[a] < 0:
        return a
    l[a] = find(l[a])
    return l[a]
ans = 0
for a, b, c in arr:
    if n == 1: break
    aa = find(a)
    bb = find(b)
    if aa == bb: continue
    l[bb] = aa
    ans += c
print(ans)
"""
3 3
1 2 1
2 3 2
1 3 3
"""
exit()

# BOJ - 1717
import sys
sys.setrecursionlimit(1000000)
read = sys.stdin.readline
n, m = map(int, read().split())
arr = [-1] * (n+1)
def union(a, b):
    aa = find(a)
    bb = find(b)
    if aa == bb: return
    arr[bb] = aa
    return
def find(a):
    if arr[a] < 0:
        return a
    arr[a] = find(arr[a])
    return arr[a]
for _ in range(m):
    a, b, c = map(int, read().split())
    if a == 0:
        union(b, c)
    else:
        print("yes" if find(b) == find(c) else "no")
"""
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1
"""