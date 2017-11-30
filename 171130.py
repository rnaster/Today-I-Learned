from sys import stdin
from array import array
read = lambda: stdin.readline().rstrip()
def BOJ2178():
    # BOJ - 2178
    n, m = map(int, input().split())
    arr = []
    for _ in range(n):
        arr.append(input())
    q = [[0, 0]]
    cache = [[-1 for _ in range(m)] for _ in range(n)]
    ans = 0
    while True:
        temp = []
        for lst in q:
            x, y = lst
            if lst == (n-1, m-1): print(ans+1); quit()
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if 0 <= x + dx < n and 0 <= y + dy < m:
                    if cache[x+dx][y+dy] == -1 and arr[x+dx][y+dy] == '1':
                        temp.append((x+dx, y+dy))
                        cache[x+dx][y+dy] = 0
        ans += 1
        q = temp[:]

# BOJ - 14500
ans = 0
n, m = map(int, read().split())
dp_2 = array('L', [0 for _ in range(m)])
dp_2_ = array('L', [0 for _ in range(m)])
dp_3 = array('L', [0 for _ in range(m)])
def arr1(arr_1):
    global ans
    for i in range(m-3):
        ans = max(ans, sum(arr_1[i:i+4]))
def arr2_1(arr_2_0, arr_2_1):
    global ans, dp_2
    for i in range(m):
        dp_2[i] = arr_2_0[i] + arr_2_1[i]
        if i >= 1:
            ans = max(ans, dp_2[i-1] + dp_2[i])  # 2x2, num:1
def arr2_2(arr_2_0, arr_2_1):
    global ans, dp_2
    for i in range(m-2):
        ans = max(ans, dp_2[i] + sum(arr_2_0[i + 1:i + 3]), dp_2[i] + sum(arr_2_1[i + 1:i + 3]),
                  arr_2_1[i] + dp_2[i + 1] + arr_2_0[i + 2], arr_2_0[i] + dp_2[i + 1] + arr_2_1[i + 2],
                  arr_2_1[i] + dp_2[i + 1] + arr_2_1[i + 2], arr_2_0[i] + dp_2[i + 1] + arr_2_0[i + 2],
                  sum(arr_2_0[i:i + 2]) + dp_2[i + 2], sum(arr_2_1[i:i + 2]) + dp_2[i + 2])
def arr3(arr_3_0, arr_3_1, arr_3_2):
    global ans, dp_3, dp_2, dp_2_
    for i in range(m):
        dp_2_[i] = arr_3_0[i] + arr_3_1[i]
        dp_3[i] = arr_3_2[i] + dp_2_[i]
    for i in range(m-1):
        ans = max(ans, dp_2[i] + dp_2_[i+1], dp_2_[i] + dp_2[i+1],
                  dp_3[i] + arr_3_2[i + 1], dp_3[i] + arr_3_1[i + 1], dp_3[i] + arr_3_0[i + 1],
                  arr_3_0[i] + dp_3[i + 1], arr_3_1[i] + dp_3[i + 1], arr_3_2[i] + dp_3[i + 1])
def arr4(arr_4_0):
    global ans, dp_3
    for i in range(m):
        ans = max(ans, dp_3[i]+arr_4_0[i])
array_1, array_2 = tuple(), tuple()
for j in range(1, n+1):
    array_0 = tuple(map(int, read().split()))
    arr1(array_0)
    if j >= 2: arr2_1(array_0, array_1); arr2_2(array_0, array_1)
    if j >= 3: arr3(array_0, array_1, array_2)
    if j >= 4: arr4(array_0)
    array_1, array_2 = array_0, array_1

print(ans)

# arr_2 = [[1,2,3,4,5],[5,4,3,2,1]]


'''
5 5
1 2 3 4 5
5 4 3 2 1
2 3 4 5 6
6 5 4 3 2
1 2 1 2 1

5 5
1 1 1 1 1
99 1 1 1 1
1 1 99 1 1
1 1 1 1 98
1 99 1 1 1

4 4
2 2 1 1
2 1 1 1
2 1 1 1
1 1 1 1

5 5
100 2 3 4 5
100 100 3 2 1
100 3 4 5 6
6 5 4 3 2
1 2 1 2 1
'''
