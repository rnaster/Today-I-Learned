# BOJ - 1978
p = set()
arr = [*range(1001)]
for i in range(2, 1000):
    if arr[i] > 0:
        p.add(i)
        for j in range(2*i, 1000, i):
            arr[j] = 0
ans = 0; input()
for a in map(int, input().split()):
    if a in p: ans += 1
print(ans)
"""
4
1 3 5 7
"""
exit()

# BOJ - 13460
n, m = map(int, input().split())
arr = [[*input()] for _ in range(n)]
red, blue, hole = None, None, None
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'R':
            red = (i, j)
            arr[i][j] = '.'
        elif arr[i][j] == 'B':
            blue = (i, j)
            arr[i][j] = '.'
cache = {(red, blue)}
q = [(red, blue)]
for i in range(1, 11):
    _q = []
    for (r1, r2), (b1, b2) in q:
        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            _r1, _r2 = r1, r2
            _b1, _b2 = b1, b2
            red_in = False
            blue_in = False
            b = True
            while arr[_r1+dx][_r2+dy] != '#':
                if (_r1+dx, _r2+dy) == (_b1, _b2):
                    if b:
                        b = False
                        while arr[_b1+dx][_b2+dy] != '#':
                            if arr[_b1+dx][_b2+dy] == '.':
                                _b1 += dx; _b2 += dy
                            elif arr[_b1+dx][_b2+dy] == 'O':
                                blue_in = True
                                break
                        if blue_in: break
                    else:
                        break
                elif arr[_r1+dx][_r2+dy] == '.':
                    _r1 += dx; _r2 += dy
                elif arr[_r1+dx][_r2+dy] == 'O':
                    red_in = True
                    _r1, _r2 = 999, 999
                    break
                else:
                    break
            if b:
                while arr[_b1+dx][_b2+dy] != '#' and (_b1+dx, _b2+dy) != (_r1, _r2):
                    if arr[_b1+dx][_b2+dy] == '.':
                        _b1 += dx; _b2 += dy
                    elif arr[_b1+dx][_b2+dy] == 'O':
                        blue_in = True
                        break
            if red_in | blue_in:
                if red_in and not blue_in:
                    print(i); exit()
            elif ((_r1, _r2), (_b1, _b2)) not in cache:
                cache.add(((_r1, _r2), (_b1, _b2)))
                _q.append(((_r1, _r2), (_b1, _b2)))
    q = _q
print(-1)
"""
7 7
#######
#O#.BR#
#.#.#.#
#.#...#
#.....#
#..#..#
#######

5 7
#######
#.RB..#
#.#O..#
#..####
#######

4 4
####
#OB#
#R.#
####

10 9
#########
#.#.....#
#.##.B#.#
#.#.....#
#.....#.#
#R.#.#..#
#....##.#
#....##O#
#.#.#.#.#
#########

10 9
#########
#.#RB...#
#.##..#.#
#.#.....#
#.....#.#
#..#.#..#
#....##.#
#....##O#
#.#.#.#.#
#########
"""