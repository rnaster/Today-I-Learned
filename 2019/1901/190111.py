# BOJ - 2979
l = tuple(map(int, input().split()))
cache = [0]*101
for _ in range(3):
    a, b = map(int, input().split())
    for i in range(a, b):
        cache[i] += 1
ans = 0
print(cache)
for c in cache:
    if c != 0:
        ans += l[c-1]*c
print(ans)
"""
5 3 1
1 6
3 5
2 8
"""
exit()

# BOJ - 5624
n = int(input())
tp = tuple(map(int, input().split()))
if n == 1:
    if tp[0] == 0: print(1)
    else: print(0)
    exit()
cache = {tp[0]*2}
ans = 0
for i in range(1, n):
    for t in tp[:i]:
        cache.add(tp[i]+t)
    for j in range(i):
        if tp[i] - tp[j] in cache: ans += 1;break
print(ans,'####')
"""
6
1 2 3 5 7 10
"""
exit()

# BOJ - 2037
p, w = map(int, input().split())
word = tuple(input())
d = {' ':(p,1),
     'A':(p,2),'B':(p*2,2),'C':(p*3,2),
     'D':(p,3),'E':(p*2,3),'F':(p*3,3),
     'G':(p,4),'H':(p*2,4),'I':(p*3,4),
     'J':(p,5),'K':(p*2,5),'L':(p*3,5),
     'M':(p,6),'N':(p*2,6),'O':(p*3,6),
     'P':(p,7),'Q':(p*2,7),'R':(p*3,7),'S':(p*4,7),
     'T':(p,8),'U':(p*2,8),'V':(p*3,8),
     'W':(p,9),'X':(p*2,9),'Y':(p*3,9),'Z':(p*4,9)}
ans, n = d[word[0]]
for ww in word[1:]:
    ans += d[ww][0]
    if d[ww][1] == n:
        if n != 1:
            ans += w
    n = d[ww][1]
print(ans)
"""
2 10
ABBAS  SALAM
"""