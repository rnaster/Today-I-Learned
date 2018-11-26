# BOJ - 11568
n = int(input())
arr = tuple(map(int, input().split()))
def func(l, num):
    size = len(l)
    a, b = 0, size-1
    c = (a+b) // 2
    while a <= c < b:
        if l[c] < num:
            a = c+1
        else:
            b = c
        c = (a + b) // 2
    return c
l = [arr[0]]
for i in arr[1:]:
    if l[-1] < i: l.append(i)
    elif l[-1] > i: l[func(l, i)] = i
print(l)
"""
8
5 4 3 2 1 6 7 8
5
8 9 1 2 10
"""