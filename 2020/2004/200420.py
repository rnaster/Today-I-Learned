# BOJ - 2072
n = int(input())
arr = [[0] * 19 for _ in range(19)]
def func1(a, b, c):
    cnt = 1
    aa = a - 1
    while -1 < aa and arr[aa][b] == c:
        aa += -1
        cnt += 1
    aa = a + 1
    while aa < 19 and arr[aa][b] == c:
        aa += 1
        cnt += 1
    return cnt
def func2(a, b, c):
    cnt = 1
    bb = b + 1
    while bb < 19 and arr[a][bb] == c:
        bb += 1
        cnt += 1
    bb = b - 1
    while -1 < bb and arr[a][bb] == c:
        bb += -1
        cnt += 1
    return cnt
def func3(a, b, c):
    cnt = 1
    aa, bb = a - 1, b + 1
    while -1 < aa and bb < 19 and arr[aa][bb] == c:
        aa += -1
        bb += 1
        cnt += 1
    aa, bb = a + 1, b - 1
    while aa < 19 and -1 < bb and arr[aa][bb] == c:
        aa += +1
        bb += -1
        cnt += 1
    return cnt
def func4(a, b, c):
    cnt = 1
    aa, bb = a - 1, b - 1
    while -1 < aa and -1 < bb and arr[aa][bb] == c:
        aa += -1
        bb += -1
        cnt += 1
    aa, bb = a + 1, b + 1
    while aa < 19 and bb < 19 and arr[aa][bb] == c:
        aa += 1
        bb += 1
        cnt += 1
    return cnt
for i in range(n):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    if i % 2:
        arr[a][b] = 2
        c = 2
    else:
        arr[a][b] = 1
        c = 1
    for f in [func1, func2, func3, func4]:
        if f(a, b, c) == 5:
            print(i+1)
            exit()
print(-1)
"""
25
3 3
2 3
3 4
2 2
3 2
3 1
3 5
2 4
2 5
2 1
1 5
4 1
4 5
5 5 
1 4 
5 1
1 3 
1 1 
5 3 
5 2 
1 2 
5 4 
4 2 
4 4 
4 3
"""