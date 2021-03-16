# BOJ - 2758
arr = [[0] * 2001 for _ in range(11)]
arr[1] = [1] * 2001
for i in range(1, 10):
    for j in range(1, 2001):
        for k in range(2*j, 2001):
            arr[i+1][k] += arr[i][j]
for i in range(1, 11):
    for j in range(2, 2001):
        arr[i][j] += arr[i][j-1]
for _ in range(int(input())):
    a, b = map(int, input().split())
    print(arr[a][b])
"""
1
4 10
"""

