# BOJ - 1260
from sys import stdin
from array import array
read = lambda: stdin.readline().rstrip()
n, m, v = map(int, read().split())
dic = {i:set() for i in range(1, n+1)}
for _ in range(m):
    i, j = map(int, read().split())
    dic[i].add(j)
for i in dic:
    dic[i] = sorted(list(dic[i]), reverse=True)
s, q = list(dic[v]), list(dic[v])
d_ans, b_ans = [v], [v]
d_hash, b_hash = array('B', [0 for _ in range(n+1)]), array('B', [0 for _ in range(n+1)])
d_hash[v], b_hash[v] = 1, 1
while s+q:
    if s:
        s_val = s.pop()
        if d_hash[s_val] == 0: d_ans.append(s_val); d_hash[s_val] = 1
        for i in dic[s_val]:
            if d_hash[i] == 0: s.append(i)
    t = []
    while q:
        q_val = q.pop()
        if b_hash[q_val] == 0: b_ans.append(q_val); b_hash[q_val] = 1
        for i in dic[q_val]:
            if b_hash[i] == 0: t.append(i)
    q = sorted(t[:], reverse=True)
    print(s, q)
print(*d_ans)
print(*b_ans)
