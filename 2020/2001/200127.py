# BOJ - 2493
n = int(input())
l = []
ans = [0] * n
for i, j in enumerate(map(int, input().split()), 1):
    if len(l) < 1:
        l.append((i, j))
    elif l[-1][1] >= j:
        ans[i-1] = l[-1][0]
        l.append((i, j))
    else:
        while l:
            if l[-1][1] < j:
                l.pop()
            else:
                break
        if l:
            ans[i-1] = l[-1][0]
        l.append((i, j))
print(*ans)
"""
5
6 9 5 7 4
"""
exit()

# BOJ - 2502
n, m = map(int, input().split())
p, q = 1, 1
for _ in range(n-3):
    p, q = q, p + q
i = 1
while 1:
    if (m - p*i) % q == 0:
        print(i, (m-p*i) // q, sep='\n')
        break
    i += 1
"""
6 41
"""
exit()

# BOJ - 2589
n, m = map(int, input().split())
arr = [input() for _ in range(n)]
d = ((0, 1), (0, -1), (1, 0), (-1, 0))
def func(a, b):
    ans = -1
    visit = [[0] * m for _ in range(n)]
    visit[a][b] = 1
    q = [(a, b)]
    while q:
        tmp = []
        for x, y in q:
            for dx, dy in d:
                if -1 < x + dx < n \
                        and -1 < y + dy < m \
                        and visit[x+dx][y+dy] < 1 \
                        and arr[x+dx][y+dy] == 'L':
                    visit[x+dx][y+dy] = 1
                    tmp.append((x+dx, y+dy))
        q = tmp
        ans += 1
    return ans
ans = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'L':
            ans = max(ans, func(i, j))
print(ans)
"""
5 7
WLLWWWL
LLLWLLL
LWLWLWW
LWLWLLL
WLLWLWW
"""