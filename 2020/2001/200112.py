# BOJ - 6593
def bfs(a, b, c):
    arr = []
    s, e = None, None
    for i in range(a):
        tmp = []
        for j in range(b):
            row = input()
            for k in range(c):
                if row[k] == 'S':
                    s = (i, j, k)
                elif row[k] == 'E':
                    e = (i, j, k)
            tmp.append(row)
        arr.append(tmp)
        input()
    visit = [[[0] * c for _ in range(b)] for _ in range(a)]
    visit[s[0]][s[1]][s[2]] = 1
    d = ((0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0))
    q = [s]
    ans = 0
    while q:
        tmp = []
        for x, y, z in q:
            for dx, dy, dz in d:
                if -1 < x + dx < a \
                        and -1 < y + dy < b \
                        and -1 < z + dz < c \
                        and visit[x + dx][y + dy][z + dz] < 1:
                    visit[x + dx][y + dy][z + dz] = 1
                    if arr[x + dx][y + dy][z + dz] == '.':
                        tmp.append((x + dx, y + dy, z + dz))
                    elif arr[x+dx][y+dy][z+dz] == 'E':
                        print('Escaped in %s minute(s).' % (ans + 1))
                        return
        q = tmp
        ans += 1
    print('Trapped!')
    return
while True:
    a, b, c = map(int, input().split())
    if (a, b, c) == (0, 0, 0): break
    bfs(a, b, c)
"""
3 4 5
S....
.###.
.##..
###.#

#####
#####
##.##
##...

#####
#####
#.###
####E

1 3 3
S##
#E#
###

0 0 0
"""
