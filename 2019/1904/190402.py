# BOJ - 14503
n, m = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
arr[r][c] = 2
ans = 1
direction = {0:(-1, 0),1:(0, 1),2:(1, 0),3:(0, -1)}
opposite = {0:2,1:3,2:0,3:1}
while True:
    back = True
    for _ in range(4):
        d = (d-1) % 4
        dx, dy = direction[d]
        if -1 < r+dx < n and -1 < c+dy < m:
            if arr[r+dx][c+dy] < 1:
                r, c = r+dx, c+dy
                arr[r][c] = 2
                ans += 1
                back = False
                break
    if back:
        oppo = opposite[d]
        dx, dy = direction[oppo]
        if -1 < r+dx < n and -1 < c+dy < m:
            if arr[r+dx][c+dy] > 1:
                r, c = r+dx, c+dy
            else: break
        else: break
print(ans)
"""
3 3
1 1 0
1 1 1
1 0 1
1 1 1

11 10
7 4 0
1 1 1 1 1 1 1 1 1 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 1 1 1 1 0 1
1 0 0 1 1 0 0 0 0 1
1 0 1 1 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1
"""