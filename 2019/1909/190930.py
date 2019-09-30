# BOJ - 1107
# import random
# n = ''.join([str(random.randint(0, 9))
#              for _ in range(random.randint(1, 5))])
# if n[0] == '0':
#     n = n[1:] + '%s' % random.randint(0, 9)
# arr = [1] * 10
# for i in [random.randint(0, 9) for _ in range(12)]:
#     arr[i] = 0
# print(n)
# for i in range(10):
#     if arr[i] > 0:
#         print(i, end=' ')
# print()

n = input(); input()
arr = [1] * 10
for i in map(int, input().split()):
    arr[i] = 0

ans = abs(int(n) - 100)

if sum(arr) == 0: print(ans); exit()
if sum(arr) == 1:
    a = ''
    for i in range(10):
        if arr[i] > 0:
            a = str(i)
            break
    ans = min(
        ans,
        abs(int(n) - int(a * len(n))) + len(n)
    )
    if len(n) > 1:
        ans = min(ans,
                  abs(int(n) - int(a * (len(n)-1))) + len(n) -1)
    print(ans, '#')
    exit()
def func1(a):
    for i in range(9, -1, -1):
        if arr[i] > 0:
            return str(i) * a
def func2(a):
    for i in range(10):
        if arr[i] > 0:
            return str(i) * a
if arr[int(n[0])] == 0:
    if n[0] == '1':
        if len(n) > 1:
            ans = min(ans,
                      abs(int(n) - int(func1(len(n) - 1))) + len(n) - 1)
        else:
            ans = min(ans,
                      abs(int(n) - int(func2(1))) + 1)
        print(ans); exit()
    elif n[0] == '9':
        if len(n) > 1:
            ans = min(ans,
                      abs(int(n) - int(func2(len(n) + 1))) + len(n) + 1)
        else:
            ans = min(ans,
                      abs(int(n) - int(func1(1))) + 1)
        print(ans); exit()
a = ''
for i, nn in enumerate(n, 1):
    if arr[int(nn)] > 0:
        a += nn
    else:
        for j in range(1, 10):
            b = True
            if int(a + nn) - j < 0:
                break
            for k in str(int(a + nn) - j):
                if arr[int(k)] == 0:
                    b = False
                    break
            if b:
                _a = str(int(a + nn) - j)
                ans = min(ans,
                          len(n) + abs(int(n) - int(_a + func1(len(n) - len(_a))))
                          )
                break
        for j in range(1, 10):
            c = True
            for k in str(int(a + nn) + j):
                if arr[int(k)] == 0:
                    c = False
                    break
            if c:
                _a = str(int(a + nn) + j)
                ans = min(ans,
                          len(_a + func2(len(n) - i)) + abs(int(n) - int(_a + func2(len(n) - i)))
                          )
                break
        print(ans); exit()
print(min(ans, len(n) + abs(int(n) - int(a))))
"""
500000
8
0 2 3 4 6 7 8 9

59180
6
1 3 4 5 7 8

624
6
0 1 4 5 6 7

7
5
1 2 3 5 9

984
6
3 4 6 7 8 9

1084
6
0 2 8 7 6 1

2
8
1 2 3 4 5 6 7 9
"""