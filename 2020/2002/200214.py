# BOJ - 6549
import sys
read = sys.stdin.readline
def func(l):
    return max(i * l[-i] for i in range(1, len(l)+1))
while 1:
    arr = [*map(int, read().split())]
    if arr[0] == 0 and len(arr) == 1: break
    l = [0]
    ans = 0
    for i in arr:
        if l[-1] > i:
            ans = max(ans, i, func(l))
            l = [0]
        else:
            l.append(i)
    ans = max(ans, func(l))
    print(ans)
"""
7 2 1 4 5 1 3 3
4 1000 1000 1000 1000
0
"""
exit()

# BOJ - 9935
a = input(); b = input()
ans = []
for i in a:
    ans.append(i)
    if i == b[-1] and len(ans) >= len(b):
        flag = True
        for j in range(len(b), 0, -1):
            if ans[-j] != b[-j]:flag = False; break
        if flag:
            for _ in b:
                ans.pop()
if len(ans) < 1:
    print('FRULA')
else:
    print(''.join(ans))
"""
mirkovC4nizCC44
C4

12ab112ab2ab
12ab
"""