# programmers - 2019 kakao blind
node_info = [[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]
import sys
sys.setrecursionlimit(10000)
def solution(node_info):
    n = len(node_info)
    l = sorted(enumerate(node_info), key=lambda x: (-x[1][1], x[1][0]))
    arr = [[-1] * n for _ in range(3)]
    i = 0
    arr[0][0] = l[0][0]
    def search(a):
        if node_info[arr[0][a]][0] > l[i][1][0]:
            if arr[1][a] == -1:
                arr[1][a] = i
                arr[0][i] = l[i][0]
            else:
                search(arr[1][a])
        else:
            if arr[2][a] == -1:
                arr[2][a] = i
                arr[0][i] = l[i][0]
            else:
                search(arr[2][a])
        return
    for i in range(1, n):
        search(0)
    pre = []
    def func1(a):
        pre.append(arr[0][a] + 1)
        if arr[1][a] > -1:
            func1(arr[1][a])
        if arr[2][a] > -1:
            func1(arr[2][a])
        return
    post = []
    def func2(a):
        if arr[1][a] > -1:
            func2(arr[1][a])
        if arr[2][a] > -1:
            func2(arr[2][a])
        post.append(arr[0][a] + 1)
        return
    func1(0);func2(0)
    return [pre, post]
print(solution(node_info))
exit()

# BOJ - 1991
import string
n = int(input())
arr = [[-1] * 26 for _ in range(2)]
for _ in range(n):
    a, b, c = map(ord, input().split())
    if b >= 65:
        arr[0][a - 65] = b - 65
    if c >= 65:
        arr[1][a - 65] = c - 65
s = string.ascii_uppercase
pre_order = []
def func1(a):
    pre_order.append(s[a])
    if arr[0][a] > -1:
        func1(arr[0][a])
    if arr[1][a] > -1:
        func1(arr[1][a])
    return
in_order = []
def func2(a):
    if arr[0][a] > -1:
        func2(arr[0][a])
    in_order.append(s[a])
    if arr[1][a] > -1:
        func2(arr[1][a])
    return
post_order = []
def func3(a):
    if arr[0][a] > -1:
        func3(arr[0][a])
    if arr[1][a] > -1:
        func3(arr[1][a])
    post_order.append(s[a])
    return
func1(0)
func2(0)
func3(0)
print(''.join(pre_order))
print(''.join(in_order))
print(''.join(post_order))
"""
7
A B C
B D .
C E F
E . .
F . G
D . .
G . .
"""
