# BOJ - 1089
from itertools import product
n = int(input())
l = [input() for _ in range(5)]
digits = [
    "###...#.###.###.#.#.###.###.###.###.###",
    "#.#...#...#...#.#.#.#...#.....#.#.#.#.#",
    "#.#...#.###.###.###.###.###...#.###.###",
    "#.#...#.#.....#...#...#.#.#...#.#.#...#",
    "###...#.###.###...#.###.###...#.###.###"
]
def parsing(l, n):
    arr = [[] for _ in range(n)]
    for j in range(5):
        k = 0
        for i in range(0, 4*n-1, 4):
            arr[k].append(l[j][i:i+3])
            k += 1
    return arr
def func(a, b):
    for i in range(5):
        for j in range(3):
            if a[i][j] == '#' and b[i][j] == '.':
                return False
    return True
arr = parsing(digits, 10)
l = parsing(l, n)
b = []
for ll in l:
    tmp = [str(i) for i, d in enumerate(arr) if func(ll, d)]
    if tmp: b.append(tmp)
    else: b.append([''])
ans = 0
cnt = 0
for prod in product(*b):
    ans += int(''.join(prod))
    cnt += 1
if cnt: print(ans / cnt)
else: print(-1)
print(ans, cnt)
print(*b, sep='\n')
"""
2
###.###
#.#.#.#
#.#.###
#.#...#
###.###

2
....###
....#.#
....###
....#.#
....###

9
...................................
...................................
...................................
...................................
...................................
"""
