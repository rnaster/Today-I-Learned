# BOJ - 2748
n = int(input())
if n < 2: print(n);exit()
a, b = 0, 1
for _ in range(n-1):
    a, b = b, a + b
print(b)
exit()

# BOJ - 9012
from sys import stdin
read = lambda: stdin.readline().rstrip()
for i in range(int(read())):
    a, b = 0, True
    for c in read():
        if c == '(':
            a += 1
        else:
            if a > 0:
                a -= 1
            else:
                print('NO')
                b = False
                break
    if b:
        if a > 0: print('NO')
        else: print('YES')
"""
6
(())())
(((()())()
(()())((()))
((()()(()))(((())))()
()()()()(()()())()
(()((())()(
"""