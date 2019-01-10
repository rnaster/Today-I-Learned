# BOJ - 1024
n, l = map(int, input().split())
while True:
    t = n - l*(l-1)/2
    if t < 0: print(-1);exit()
    t /= l
    if int(t) == t: break
    if t < 1: print(-1);exit()
    l += 1
    if l > 100: print(-1);exit()
t = int(t)
for i in range(l):
    print(t+i, end=' ')
"""
18 2
"""