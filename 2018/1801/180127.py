# BOJ - 2533
from sys import stdin
from array import array
read = lambda: stdin.readline().rstrip()
n = int(read())
dp = array('H', [0])
floor = array('H', [0])
s = set(range(1, n+1))
d = {i: [] for i in range(1, n+1)}
for _ in range(n-1):
    a, b = map(int, read().split())
    d[a].append(b)
    s.discard(b)
q = list(s)
floor.append(len(q))
dp.append(len(q))
while True:
    tmp = set()
    while q:
        a = q.pop()
        tmp.update(set(d[a]))
    if not tmp: break
    q = list(tmp)
    floor.append(len(q))
    dp.append(min(floor[-1]+dp[-1], sum(floor[::-2]), sum(floor[:-1][::-2])))
print(dp)
print(floor)
print(dp[-1])
'''
8
1 2
1 3
1 4
2 5
2 6
4 7
4 8

16
1 2
1 3
1 4
2 5
2 6
4 7
4 8
5 9
8 10
13 14
12 13
9 11
10 12
15 12
16 12

15
1 2
1 3
3 4
1 5
5 6
6 7
7 8
8 9
9 10
10 11
11 12
12 13
13 14
14 15

16
1 2
1 3
1 4
1 5
1 6
2 7
3 8
4 9
5 10
8 11
9 12
9 13
9 14
9 15
9 16
'''