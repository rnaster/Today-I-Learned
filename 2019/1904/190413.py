# BOJ - 16236
n = int(input())
arr, q = [], []
search = True
for i in range(n):
    t = list(map(int, input().split()))
    arr.append(t)
    if search:
        for j in range(n):
            if t[j] > 6: q.append((i, j));search = False;break
ans = 0
visit = [[-1] * n for _ in range(n)]
visit[q[0][0]][q[0][1]] = 0
arr[q[0][0]][q[0][1]] = 0
s = 2
count = 0
t = 1
di = ((-1, 0), (0, -1), (0, 1), (1, 0))
while q:
    temp = []
    candidate = []
    for x, y in q:
        for dx, dy in di:
            if -1 < x+dx < n and -1 < y+dy < n:
                if visit[x+dx][y+dy] > -1 or arr[x+dx][y+dy] > s: continue
                visit[x+dx][y+dy] = 0
                if 0 < arr[x+dx][y+dy] < s:
                    candidate.append((x+dx, y+dy))
                    break
                elif arr[x+dx][y+dy] == 0 or arr[x+dx][y+dy] == s:
                    temp.append((x+dx, y+dy))
    if candidate:
        candidate.sort()
        x, y = candidate[0]
        count += 1
        arr[x][y] = 0
        ans += t
        t = 1
        if count == s: s += 1; count = 0
        visit = [[-1] * n for _ in range(n)]
        visit[x][y] = 0
        q = [(x, y)]
    else: q = temp; t += 1
print(ans)
"""
4
4 3 2 1
0 0 0 0
0 0 9 0
1 2 3 4

3
0 0 0
0 0 0
0 9 0

3
0 0 1
0 0 0
0 9 0

6
5 4 3 2 3 4
4 3 2 3 4 5
3 2 9 5 6 6
2 1 2 3 4 5
3 2 1 6 5 4
6 6 6 6 6 6

6
6 0 6 0 6 1
0 0 0 0 0 2
2 3 4 5 6 6
0 0 0 0 0 2
0 2 0 0 0 0
3 9 3 0 0 1

6
1 1 1 1 1 1
2 2 6 2 2 3
2 2 5 2 2 3
2 2 2 4 6 3
0 0 0 0 0 6
0 0 0 0 0 9
"""