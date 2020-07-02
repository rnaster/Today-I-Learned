# programmers - 2020 kakao blind 가사 검색
words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
import sys
sys.setrecursionlimit(1000000)
def solution(words, queries):
    arr = [[-1] * 27]
    arr[0][-1] = 0
    cur = 1
    for word in words:
        i = 0
        for w in word:
            j = ord(w)-97
            if arr[i][j] > -1:
                i = arr[i][j]
            else:
                arr[i][j] = cur
                i = cur
                cur += 1
                arr.append([-1] * 27)
                arr[-1][-1] = 0
        arr[i][-1] = 1
    def func(query, idx, n):
        if n == len(query):
            return arr[idx][-1]
        cnt = 0
        if query[n] == '?':
            for i in range(26):
                if arr[idx][i] > -1:
                    cnt += func(query, arr[idx][i], n+1)
        else:
            t = arr[idx][ord(query[n])-97]
            if t > -1:
                cnt = func(query, t, n+1)
        return cnt
    ans = []
    cache = {}
    for query in queries:
        if query in cache:
            ans.append(cache[query])
        else:
            cache[query] = val = func(query, 0, 0)
            ans.append(val)
    return ans
print(solution(words, queries))
exit()

# BOJ - 2632
import sys
read = sys.stdin.readline
k = int(input())
n, m = map(int, input().split())
l1 = [int(read()) for _ in range(n)]
l2 = [int(read()) for _ in range(m)]
s1, s2 = {0: 1, sum(l1): 1}, {0: 1, sum(l2): 1}
for i in range(n):
    t = 0
    for j in range(n-1):
        t += l1[(i+j) % n]
        if t > k: break
        s1[t] = s1.get(t, 0) + 1
for i in range(m):
    t = 0
    for j in range(m-1):
        t += l2[(i+j) % m]
        if t > k: break
        s2[t] = s2.get(t, 0) + 1
ans = 0
for s in s1:
    if k-s in s2:
        ans += s1[s] * s2[k-s]
print(ans)
"""
7
5 3
2
2
1
7
2
6
8
3

4
1 3
1
1
1
1

"""
exit()

# BOJ - 2623
from collections import deque
n, m = map(int, input().split())
arr = [[] for _ in range(n)]
d = [0] * n
for _ in range(m):
    l = map(int, input().split())
    if next(l) < 2: continue
    i = next(l)
    for j in l:
        arr[i-1].append(j-1)
        d[j-1] += 1
        i = j
q = deque([i for i, v in enumerate(d) if v == 0])
ans = []
while q:
    a = q.popleft()
    ans.append(a)
    for i in arr[a]:
        d[i] -= 1
        if d[i] == 0: q.append(i)
if len(ans) != n: print(0)
else:
    for a in ans:
        print(a+1)
"""
6 3
3 1 4 3
4 6 2 5 4
2 2 3
"""
exit()

# BOJ - 19238
n, m, k = map(int, input().split())
arr = [[*map(int, input().split())] for _ in range(n)]
l = [0] * m
x, y = map(int, input().split())
x, y = x-1, y-1
for i in range(m):
    a, b, c, d = map(int, input().split())
    arr[a-1][b-1] = i+2
    l[i] = (c-1, d-1)
def dist(a, b):
    yield a+1, b
    yield a-1, b
    yield a, b+1
    yield a, b-1
for _ in range(m):
    q = [(x, y)]
    visit = [[True] * n for _ in range(n)]
    visit[x][y] = False
    ll = []
    d = 0
    if arr[x][y] > 1: ll.append((x, y))
    while not ll and q:
        tmp = []
        for a, b in q:
            for aa, bb in dist(a, b):
                if -1 < aa < n and -1 < bb < n and visit[aa][bb]:
                    visit[aa][bb] = False
                    if arr[aa][bb] > 1: ll.append((aa, bb))
                    elif arr[aa][bb] == 0: tmp.append((aa, bb))
        q = tmp
        d += 1
    if not ll: print(-1);exit()
    a, b = min(ll)
    if k < d: print(-1);exit()
    k -= d
    x, y = l[arr[a][b]-2]
    arr[a][b] = 0
    q = [(a, b)]
    visit = [[True] * n for _ in range(n)]
    visit[a][b] = False
    e = 0
    while 1:
        tmp = []
        flag = False
        for c, d in q:
            if (c, d) == (x, y): flag = True;break
            for cc, dd in dist(c, d):
                if -1 < cc < n and -1 < dd < n and visit[cc][dd]:
                    visit[cc][dd] = False
                    if arr[cc][dd] != 1: tmp.append((cc, dd))
        if flag: break
        if tmp:
            q = tmp
            e += 1
        else: print(-1);exit()
    if k < e: print(-1);exit()
    k += e
print(k)
"""
6 3 15
0 0 1 0 0 0
0 0 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 1 0
0 0 0 1 0 0
6 5
2 2 5 6
5 4 1 6
4 2 3 5

6 4 15
0 0 0 0 0 0
0 0 1 0 0 0
0 0 1 0 0 0
1 1 0 1 0 0
0 0 0 0 0 0
0 0 0 0 0 0
4 3
3 2 4 3
3 4 4 3
5 2 4 3
5 4 4 3

6 4 15
0 0 1 0 0 0
0 0 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 1 0
0 0 0 1 0 0
6 5
2 2 5 6
5 4 1 6
4 2 3 5
1 6 5 4
"""