# BOJ - 18808
import sys
read = sys.stdin.readline
n, m, k = map(int, read().split())
ans, a, b, l = 0, 0, 0, []
arr = [[0] * m for _ in range(n)]
def func():
    global ans
    for i in range(n-a+1):
        for j in range(m-b+1):
            flag = True
            for aa in range(a):
                for bb in range(b):
                    if arr[i+aa][j+bb] + l[aa][bb] > 1:
                        flag = False
                        break
                    if not flag: break
            if flag:
                for aa in range(a):
                    for bb in range(b):
                        arr[i+aa][j+bb] += l[aa][bb]
                        ans += l[aa][bb]
                return False
    return True
def rotate(l):
    ll = [[0] * a for _ in range(b)]
    for aa in range(a):
        for bb in range(b):
            ll[bb][-(aa+1)] = l[aa][bb]
    return ll
for _ in range(k):
    if ans == n * m: break
    a, b = map(int, read().split())
    l = [[*map(int, read().split())] for _ in range(a)]
    for _ in range(4):
        if func():
            l = rotate(l)
            a, b = b, a
        else:
            break
print(ans)
"""
5 4 4
3 3
1 0 1
1 1 1
1 0 1
2 5
1 1 1 1 1
0 0 0 1 0
2 3
1 1 1
1 0 1
3 3
1 0 0
1 1 1
1 0 0
"""