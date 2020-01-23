# BOJ - 1874
import sys
read = sys.stdin.readline
ans, l = [], []
a = 1
for _ in range(int(input())):
    b = int(read())
    if a <= b:
        l.extend([i for i in range(a, b)])
        ans.extend(['+'] * (b-a+1) + ['-'])
        a = b + 1
    elif l[-1] == b:
        l.pop();ans.append('-')
    else:
        print('NO')
        exit()
print(*ans, sep='\n')
"""
8
4
3
6
8
7
5
2
1
"""
exit()

# BOJ - 2479
n, k = map(int, input().split())
l = [int(input(), 2) for _ in range(n)]
arr = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(i+1, n):
        x = l[i] ^ l[j]
        arr[i][j] = arr[j][i] = x & (x-1) < 1
c, d = map(int, input().split())
q = [c]
visit = [0] * n
visit[c-1] = 99
while q:
    tmp = []
    for i in q:
        for j in range(n):
            if arr[i-1][j] and visit[j] < 1:
                visit[j] = i
                tmp.append(j+1)
    q = tmp
if visit[d-1] < 1: print(-1);exit()
ans = []
a = d
while a != c:
    ans.append(a)
    a = visit[a-1]
ans.append(a)
for i in range(1, len(ans) + 1):
    print(ans[-i], end=' ')
"""
5 3
000
111
010
110
001
1 2
"""