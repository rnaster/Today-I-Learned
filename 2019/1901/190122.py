# BOJ - 10828
from sys import stdin
read = lambda: stdin.readline().rstrip()
s = []
size = 0
for _ in range(int(read())):
    c = read().split()
    if len(c) == 1:
        if c[0] == 'top':
            if size == 0: print(-1)
            else: print(s[-1])
        elif c[0] == 'size':
            print(size)
        elif c[0] == 'pop':
            if size == 0: print(-1)
            else: print(s.pop()); size += -1
        else:
            if size == 0: print(1)
            else: print(0)
    else:
        s.append(c[1])
        size += 1
"""
14
push 1
push 2
top
size
empty
pop
pop
pop
size
empty
pop
push 3
empty
top

7
pop
top
push 123
top
pop
top
pop
"""
exit()

# BOJ - 5612
from sys import stdin
read = lambda: stdin.readline().rstrip()
n, m = int(read()), int(read())
ans = 0
for _ in range(n):
    i, o = map(int, read().split())
    m += i - o
    ans = max(ans, m)
    if m < 0: print(0);exit()
print(ans)
"""
3
2
2 3
2 3
4 1
"""
exit()

# BOJ - 9252
s1, s2 = input(), input()
ss1 = len(s1)
ss2 = len(s2)
dp = [[0] * (ss1 + 1) for _ in range(ss2+1)]
dp_s = [[''] * (ss1 + 1) for _ in range(ss2+1)]
for i in range(1, ss2+1):
    for j in range(1, ss1+1):
        if s2[i-1] == s1[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
            dp_s[i][j] = dp_s[i-1][j-1] + s1[j-1]
        else:
            if dp[i-1][j] >= dp[i][j-1]:
                dp[i][j] = dp[i-1][j]
                dp_s[i][j] = dp_s[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]
                dp_s[i][j] = dp_s[i][j-1]
print(dp[-1][-1], dp_s[-1][-1], sep='\n')
"""
ACAYKP
CAPCAK

AAA
AA
"""