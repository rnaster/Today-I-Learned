# BOJ - 14500
n, m = map(int, input().split())
arr = [[0]*m for _ in range(2)]
cache0 = [[0]*(m-1) for _ in range(2)]
cache1 = [[0]*m for _ in range(2)]
ans = 0
for i in range(2, n+2):
    arr.append(tuple(map(int, input().split())))
    cache0.append([arr[i][j] + arr[i][j+1] for j in range(m-1)])
    cache1.append([arr[i-1][j] + arr[i][j] for j in range(m)])
    ans = max(ans,
              *[cache0[i][j] + cache0[i][j+2] for j in range(m-3)],
              *[cache1[i-2][j] + cache1[i][j] for j in range(m)],
              *[cache0[i-1][j] + cache0[i][j] for j in range(m-1)],
              *[cache0[i][j] + cache1[i-1][j] for j in range(m-1)],
              *[cache0[i][j] + cache1[i][j+2] for j in range(m-2)],
              *[cache1[i][j] + cache0[i][j+1] for j in range(m-2)],
              *[cache0[i-2][j] + cache1[i][j+1] for j in range(m-2)],
              *[cache0[i][j] + cache1[i-1][j+1] for j in range(m-1)],
              *[cache0[i-2][j] + cache1[i][j] for j in range(m-1)],
              *[cache1[i][j] + cache0[i-1][j+1] for j in range(m-2)],
              *[cache0[i-1][j] + cache1[i][j+2] for j in range(m-2)],
              *[cache1[i-1][j] + cache1[i][j+1] for j in range(m-1)],
              *[cache1[i][j] + cache1[i-1][j+1] for j in range(m-1)],
              *[cache0[i-1][j] + cache0[i][j+1] for j in range(m-2)],
              *[cache0[i][j] + cache0[i-1][j+1] for j in range(m-2)],
              *[arr[i-1][j] + arr[i-1][j+1] + arr[i-2][j+1] + arr[i][j+1] for j in range(m-1)],
              *[arr[i-1][j] + arr[i-1][j+1] + arr[i-1][j+2] + arr[i][j+1] for j in range(m-2)],
              *[arr[i][j] + arr[i-1][j] + arr[i-2][j] + arr[i-1][j+1] for j in range(m-1)],
              *[arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i-1][j+1] for j in range(m-2)]
              )
print(ans)
print(*cache0, sep='\n')
print()
print(*cache1, sep='\n')
"""
5 5
1 2 3 4 5
5 4 3 2 1
2 3 4 5 6
6 5 4 3 2
1 2 1 2 1
# 19

4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
# 20

4 10
1 2 1 2 1 2 1 2 1 2
2 1 2 1 2 1 2 1 2 1
1 2 1 2 1 2 1 2 1 2
2 1 2 1 2 1 2 1 2 1
# 7

4 4
1 2 3 4
1 2 3 4
1 2 3 4
1 2 3 4
# 16

5 5
100 2 3 4 5
100 100 3 2 1
100 3 4 5 6
6 5 4 3 2
1 2 1 2 1
# 400

4 4
2 2 1 1
2 1 1 1
2 1 1 1
1 1 1 1
# 8

5 10
1 2 1 2 1 2 1 2 1 1
2 1 2 1 2 1 2 1 2 1
1 2 1 2 1 2 1 2 1 1
2 1 2 1 2 1 1 1 1 1
1 1 1 1 1 1 10 10 10 10
# 40

5 10
1 2 1 2 1 2 1 2 1 1
2 1 2 1 2 1 2 1 2 10
1 2 1 2 1 2 1 2 1 10
2 1 2 1 2 1 1 1 1 10
1 1 1 1 1 1 1 1 1 10

"""