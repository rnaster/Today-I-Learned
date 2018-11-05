# BOJ - 1966
from sys import stdin, stdout
from collections import deque
read = lambda: stdin.readline().rstrip()
write = lambda x: stdout.write(x)
for _ in range(int(read())):
    n, m = map(int, read().split())
    q = deque(map(int, read().split()))
    l = deque([0] * n); l[m] = 1
    if n == 1: write('1\n'); continue
    ans, t_o, m_o = 0, q[m], max(q)
    while True:
        a, b = q.popleft(), l.popleft()
        if a == m_o:
            ans += 1
            if b == 1:
                write(str(ans) + '\n'); break
            m_o = max(q)
        else:
            q.append(a); l.append(b)

"""
4
1 0
5
4 2
1 2 3 4
6 0
1 1 9 1 1 1
2 1
99 98
"""