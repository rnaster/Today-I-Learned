# BOJ - 1244
n = int(input())
arr = [*map(int, input().split())]
def func(i):
    a = b = i
    while arr[a] == arr[b]:
        if a > 0 and b < n-1:
            a -= 1
            b += 1
        else:
            break
    if arr[a] == arr[b]:
        return a, b
    return a + 1, b - 1
for _ in range(int(input())):
    a, b = map(int, input().split())
    if a == 1:
        for i in range(b-1, n, b):
            arr[i] = 1 - arr[i]
    else:
        c, d = func(b-1)
        for i in range(c, d+1):
            arr[i] = 1 - arr[i]
for i in range(1, n+1):
    if i % 20 == 0:
        print(arr[i-1])
    else:
        print(arr[i-1], end=" ")
"""
24
0 1 0 1 0 0 0 1 0 1 0 1 0 0 0 1 0 1 0 1 0 0 0 1
1
2 4


"""