# BOJ - 17129
import sys
read = lambda: sys.stdin.readline().rstrip()
n, m = map(int, read().split())
arr = []
q = []
find = True
for i in range(n):
    t = read()
    arr.append(t)
    if find:
        for j in range(m):
            if t[j] == '2': q.append((i, j));find = False
visit = [[-1]*m for _ in range(n)]
visit[q[0][0]][q[0][1]] = 1
ans = 0
while q:
    t = []
    for a, b in q:
        if arr[a][b] in ['3', '4', '5']:
            print('TAK')
            print(ans)
            exit()
        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            if -1 < a + dx < n and -1 < b + dy < m:
                if visit[a + dx][b + dy] < 0 and arr[a + dx][b + dy] != '1':
                    t.append((a + dx, b + dy))
                    visit[a + dx][b + dy] = 1
    q = t
    ans += 1
print('NIE')
"""
3 3
200
003
045

3 3
210
113
045

3 1
2
0
3
"""
exit()

# BOJ - 17128
import sys
read = lambda: sys.stdin.readline().rstrip()
write = lambda x: sys.stdout.write(str(x)+'\n')
n, q = map(int, read().split())
arr = list(map(int, read().split()))
tp = tuple(map(int, read().split()))
total = 0
cache = [0]*n
for i in range(n):
    cache[i] = arr[i]*arr[(i+1)%n]*arr[(i+2)%n]*arr[(i+3)%n]
    total += cache[i]
for i in tp:
    i -= 1
    arr[i] *= -1
    for j in [i, (i-1)%n, (i-2)%n, (i-3)%n]:
        total -= cache[j]
        cache[j] = arr[j]*arr[(j + 1) % n]*arr[(j + 2) % n]*arr[(j + 3) % n]
        total += cache[j]
    write(total)
"""
8 5
-2 3 5 -6 10 -8 7 6
3 5 2 7 7
"""
exit()

# BOJ - 17127
n = int(input())
arr = tuple(map(int, input().split()))
cache = [[1]*n for _ in range(n)]
cache[0][0] = arr[0]
dp = [[-1]*n for _ in range(4)]
for i in range(1, n):
    cache[0][i] = cache[0][i-1]*arr[i]
for i in range(1, n):
    for j in range(i, n):
        cache[i][j] = cache[i-1][j] // cache[i-1][i-1]
def main(a, b):
    if a == 0:
        dp[a][b] = cache[0][b]
        return dp[a][b]
    else:
        v = 0
        for i in range(b, a-1, -1):
            t = dp[a-1][i-1] if dp[a-1][i-1] > 0 else main(a-1, i-1)
            v = max(v, t+cache[i][b])
        dp[a][b] = v
        return dp[a][b]
print(main(3, n-1))
print(*dp, sep='\n')
print('#'*10)
print(*cache, sep='\n')
"""
7
2 5 3 1 4 2 3

5
1 1 2 1 1
"""
