# BOJ - 1976
n = int(input())
m = int(input())
l = [-1] * n
def find(a):
    if l[a] == -1:
        return a
    l[a] = find(l[a])
    return l[a]
for i in range(n):
    ii = find(i)
    for j, k in enumerate(map(int, input().split())):
        if k == 0: continue
        jj = find(j)
        if ii == jj: continue
        l[jj] = ii
arr = [*map(int, input().split())]
a = find(arr[0]-1)
ans = True
for i in arr:
    if a == find(i-1): continue
    ans = False
    break
print("YES" if ans else "NO")
"""
3
3
0 1 0
1 0 1
0 1 0
1 2 3
"""