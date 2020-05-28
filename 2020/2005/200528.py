# BOJ - 1241
import sys
read = sys.stdin.readline
write = sys.stdout.write
n = int(input())
arr = {}
ans = {}
l = [0] * n
for i in range(n):
    l[i] = a = int(read())
    arr[a] = arr.get(a, 0) + 1
for i, v in arr.items():
    ans[i] = ans.get(i, 0) + v-1
    for j in range(2*i, 1_000_001, i):
        if j in arr:
            ans[j] = ans.get(j, 0) + v
for i in l:
    write('%s\n' % ans[i])
"""
5
2
1
2
3
4
"""