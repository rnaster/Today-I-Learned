# BOJ - 18258
from sys import stdin, stdout
from collections import deque
read = stdin.readline
write = lambda x: stdout.write('%s\n' % x)
q = deque()
s = 0
def push(a):
    global s
    q.append(a[0])
    s += 1
def front(_):
    if s > 0:
        write(q[0])
        return
    write(-1)
def back(_):
    global s
    if s > 0:
        write(q[-1])
        return
    write(-1)
def empty(_):
    if s > 0:
        write(0)
        return
    write(1)
def size(_):
    write(s)
def pop(_):
    global s
    if s > 0:
        write(q.popleft())
        s -= 1
        return
    write(-1)
d = {'push': push, 'pop': pop, 'size': size, 'empty': empty,
     'back': back, 'front': front}
for _ in range(int(read())):
    a, *b = read().split()
    d[a](b)
"""
15
push 1
push 2
front
back
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
front
"""