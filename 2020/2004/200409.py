# BOJ - 1960
n = int(input())
a = [*map(int, input().split())]
b = [*map(int, input().split())]
bbb = sum(b)
if sum(a) != bbb: print(-1);exit()
arr = [[''] * n for _ in range(n)]
for i, aa in sorted(enumerate(a), key=lambda x: x[1], reverse=True):
    for j, _ in sorted(enumerate(b), key=lambda x: x[1], reverse=True):
        if aa > 0 and b[j] > 0:
            b[j] -= 1
            aa -= 1
            bbb -= 1
            arr[i][j] = '1'
        else:
            arr[i][j] = '0'
    if aa > 0: print(-1);exit()
if bbb > 0: print(-1)
else: print(1, *map(lambda x: ''.join(x), arr), sep='\n')
"""
4
2 3 2 0
1 1 4 1

3
1 1 1
1 0 2
"""
exit()

# BOJ - 1817
n, m = map(int, input().split())
if n == 0: print(0);exit()
ans, a = 1, m
for i in map(int, input().split()):
    if a < i:
        a = m - i
        ans += 1
    else: a -= i
print(ans)
"""
6 10
5 5 5 5 5 5

0 10
"""
exit()

# BOJ - 2036
import sys
read = sys.stdin.readline
a, b = [], []
ans = 0
for _ in range(int(input())):
    n = int(read())
    if n > 0:
        if n == 1:
            ans += 1
        else:
            a.append(n)
    else: b.append(n)
a.sort(reverse=True)
b.sort()
ans += a[-1] if len(a) % 2 else 0
for i in range(len(a)//2):
    ans += a[i*2] * a[i*2+1]
ans += b[-1] if len(b) % 2 else 0
for i in range(len(b)//2):
    ans += b[i*2] * b[i*2+1]
print(ans)
"""
5
-1
5
-3
5
1

5
-4
3
1
0
-8
"""