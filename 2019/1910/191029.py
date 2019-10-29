# BOJ - 17779
n = int(input())
arr = [[*map(int, input().split())] for _ in range(n)]
ans = 987654321
for d1 in range(1, n - 1):
    for d2 in range(1, n - 1):
        if d1 + d2 >= n: break
        for x in range(n - d1 - d2):
            for y in range(d1, n - d2):
                l = [0] * 5
                l[4] += arr[x][y]
                l[0] += sum([sum(arr[i][:y + 1]) for i in range(x)])
                l[1] += sum([sum(arr[i][y + 1:]) for i in range(x)])
                l[0] += sum(arr[x][:y])
                l[1] += sum(arr[x][y + 1:])
                _x_, _y, y_ = x, y, y
                if d1 == d2:
                    for _ in range(d1-1):
                        _x_, _y, y_ = _x_+1, _y - 1, y_ + 1
                        l[0] += sum(arr[_x_][:_y])
                        l[4] += sum(arr[_x_][_y:y_+1])
                        l[1] += sum(arr[_x_][y_+1:])
                    _x_, _y, y_ = _x_ + 1, _y - 1, y_ + 1
                    l[2] += sum(arr[_x_][:_y])
                    l[4] += sum(arr[_x_][_y:y_+1])
                    l[1] += sum(arr[_x_][y_+1:])
                    for _ in range(d1):
                        _x_, _y, y_ = _x_ + 1, _y + 1, y_ - 1
                        l[2] += sum(arr[_x_][:_y])
                        l[4] += sum(arr[_x_][_y:y_ + 1])
                        l[3] += sum(arr[_x_][y_+1:])
                elif d1 < d2:
                    for _ in range(d1-1):
                        _x_, _y, y_ = _x_ + 1, _y - 1, y_ + 1
                        l[0] += sum(arr[_x_][:_y])
                        l[4] += sum(arr[_x_][_y:y_ + 1])
                        l[1] += sum(arr[_x_][y_ + 1:])
                    _x_, _y, y_ = _x_ + 1, _y - 1, y_ + 1
                    l[2] += sum(arr[_x_][:_y])
                    l[4] += sum(arr[_x_][_y:y_ + 1])
                    l[1] += sum(arr[_x_][y_ + 1:])
                    for _ in range(d2-d1-1):
                        _x_, _y, y_ = _x_ + 1, _y + 1, y_ + 1
                        l[2] += sum(arr[_x_][:_y])
                        l[4] += sum(arr[_x_][_y:y_ + 1])
                        l[1] += sum(arr[_x_][y_ + 1:])
                    for _ in range(d1):
                        _x_, _y, y_ = _x_ + 1, _y + 1, y_ - 1
                        l[2] += sum(arr[_x_][:_y])
                        l[4] += sum(arr[_x_][_y:y_ + 1])
                        l[3] += sum(arr[_x_][y_ + 1:])
                else:
                    for _ in range(d2):
                        _x_, _y, y_ = _x_ + 1, _y - 1, y_ + 1
                        l[0] += sum(arr[_x_][:_y])
                        l[4] += sum(arr[_x_][_y:y_ + 1])
                        l[1] += sum(arr[_x_][y_ + 1:])
                    for _ in range(d1-d2-1):
                        _x_, _y, y_ = _x_ + 1, _y - 1, y_ - 1
                        l[0] += sum(arr[_x_][:_y])
                        l[4] += sum(arr[_x_][_y:y_ + 1])
                        l[3] += sum(arr[_x_][y_ + 1:])
                    _x_, _y, y_ = _x_ + 1, _y - 1, y_ - 1
                    l[2] += sum(arr[_x_][:_y])
                    l[4] += sum(arr[_x_][_y:y_ + 1])
                    l[3] += sum(arr[_x_][y_ + 1:])
                    for _ in range(d2):
                        _x_, _y, y_ = _x_ + 1, _y + 1, y_ - 1
                        l[2] += sum(arr[_x_][:_y])
                        l[4] += sum(arr[_x_][_y:y_ + 1])
                        l[3] += sum(arr[_x_][y_ + 1:])
                l[2] += sum([sum(arr[i][:_y]) for i in range(_x_ + 1, n)])
                l[3] += sum([sum(arr[i][y_:]) for i in range(_x_ + 1, n)])
                ans = min(ans, max(l) - min(l))
print(ans)

"""
6
1 2 3 4 1 6
7 8 9 1 4 2
2 3 4 1 1 3
6 6 6 6 9 4
9 1 9 1 9 5
1 1 1 1 9 9

6
6 1 4 3 2 1
2 4 1 9 8 7
3 1 1 4 3 2
4 9 6 6 6 6
5 9 1 9 1 9
9 9 1 1 1 1

8
1 2 3 4 5 6 7 8
2 3 4 5 6 7 8 9
3 4 5 6 7 8 9 1
4 5 6 7 8 9 1 2
5 6 7 8 9 1 2 3
6 7 8 9 1 2 3 4
7 8 9 1 2 3 4 5
8 9 1 2 3 4 5 6

8
8 7 6 5 4 3 2 1
9 8 7 6 5 4 3 2
1 9 8 7 6 5 4 3
2 1 9 8 7 6 5 4
3 2 1 9 8 7 6 5
4 3 2 1 9 8 7 6
5 4 3 2 1 9 8 7
6 5 4 3 2 1 9 8
"""
