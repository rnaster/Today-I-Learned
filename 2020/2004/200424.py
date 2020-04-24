# BOJ - 1930
import sys
read = sys.stdin.readline
def func(a, b):
    for _ in range(3):
        b = [b[1], b[2], b[0]]
        flag = True
        for aa, bb in zip(a, b):
            if aa != bb:
                flag = False
                break
        if flag:
            return True
    return False
def func2(b):
    yield b
    yield [b[2], b[0], b[1], b[3]]
    yield [b[1], b[3], b[2], b[0]]
    yield [b[3], b[0], b[2], b[1]]
for _ in range(int(input())):
    a = [*map(int, read().split())]
    a, b = a[:4], a[4:]
    flag = False
    if set(a) != set(b): print(0);continue
    for bb in func2(b):
        if a[0] == bb[0] and func(a[1:], bb[1:]):
            flag = True
            break
    if flag: print(1)
    else: print(0)
"""
4
1 2 3 4 1 2 3 4
4 1 2 3 4 3 2 1
1 2 3 4 3 4 1 2
4 4 1 1 4 4 4 1
"""
exit()

# BOJ - 1195
a = input();b = input()
ans = len(a) + len(b)
for i in range(len(b)):
    flag = True
    for aa, bb in zip(a, b[i:]):
        if aa == bb == '2':
            flag = False
            break
    if flag:
        ans = min(ans, max(i+len(a), len(b)))
        break
for i in range(len(a)):
    flag = True
    for aa, bb in zip(a[i:], b):
        if aa == bb == '2':
            flag = False
            break
    if flag:
        ans = min(ans, max(i+len(b), len(a)))
        break
print(ans)
"""
2212112
2112112
2111
2222
"""