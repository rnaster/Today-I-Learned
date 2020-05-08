# BOJ - 12934
x, y = map(int, input().split())
z = (x + y)*2
a, b = 1, 3_000_000
c = (a + b) // 2
while a < c < b:
    cc = c*(c+1)
    if cc == z:
        break
    elif cc > z:
        b = c
    else:
        a = c
    c = (a + b) // 2
if c*(c+1) != z: print(-1);exit()
cc = c*(c+1) // 2
i, j = 1, c
k = (i + j) // 2
while i < k < j:
    kk = k*(k+1) // 2
    t = cc - kk
    if abs(t-x) < k:
        break
    elif t >= x + c:
        i = k
    elif x >= t + k:
        j = k
    else:
        c -= 1
        break
    k = (i + j) // 2
print(c - k + 1)
# print(x - k*(k+1)//2, k, c, c-k, sep='\n')
"""
932599670050 67400241741
"""
exit()

# BOJ - 11497
import sys
read = sys.stdin.readline
for _ in range(int(input())):
    n = int(read())
    arr = sorted(map(int, read().split()))
    l = arr[0:n:2]
    l2 = arr[1:n:2]
    ans = arr[-1] - arr[-2]
    ans = max(ans,
              *[l[i]-l[i-1] for i in range(1, n - n//2)],
              *[l2[i] - l2[i-1] for i in range(1, n//2)])
    print(ans)
"""
3
7
13 10 12 11 10 11 12
5
2 4 5 7 9
8
6 6 6 6 6 6 6 6
"""
exit()

# BOJ - 4889
import sys
read = sys.stdin.readline
i = 1
while 1:
    s = read().strip()
    if s[0] == '-': break
    ans = 0
    a = 0
    for ss in s:
        if ss == '{':
            a += 1
        elif a < 1:
            ans += 1
            a = 1
        else:
            a -= 1
    ans += a // 2
    print('%d. %d' % (i, ans))
    i += 1
"""
}{
{}{}{}
{{{}
---
"""
exit()

# BOJ - 3042
n = int(input())
arr = [input() for _ in range(n)]
ans = 0
def func(a, b):
    if b+2 < n:
        yield ((a, b+i) for i in range(3))
        if a + 2 < n:
            yield ((a + i, b + i) for i in range(3))
    if a + 2 < n:
        yield ((a + i, b) for i in range(3))
        if 1 < b:
            yield ((a + i, b - i) for i in range(3))
for i in range(n):
    for j in range(n):
        for l in func(i, j):
            flag = True
            for aa, bb in l:
                if arr[aa][bb] == '.':
                    flag = False
                    break
            if flag: ans += 2
print(ans)
"""
4
...D
..C.
.B..
A...
"""