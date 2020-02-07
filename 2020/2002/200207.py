# BOJ - 17825
from itertools import product
arr = [*map(int, input().split())]
road = [[0, 2, 4, 6, 8],
        [10, 12, 14, 16, 18],
        [20, 22, 24, 26, 28],
        [30, 32, 34, 36, 38, 40],
        [10, 13, 16, 19],
        [30, 28, 27, 26, 40],
        [25, 30, 35, 40],
        [20, 22, 24, 25, 30, 35, 40]]
red = {0:1, 1:2, 2:3, 4:6, 5:6, 6:-1, 7:-1, 3:-1}
blue = {0:4, 1:7, 2:5, 4:6, 5:6, 6:-1, 7:-1, 3:-1}
def func(order):
    score = 0
    state = [[0, 0] for _ in range(4)]
    for i, o in enumerate(order):
        a, b = state[o]
        if a < 0: return -1
        p, b = divmod(b+arr[i], len(road[a]))
        if p > 0 and b > 0:
            a = red[a]
        elif p > 0:
            a = blue[a]
        if a < 0:
            if b == 0: score += 40
        else:
            for j in range(4):
                if j == o: continue
                if [a, b] == state[j]:
                    return -1
            score += road[a][b]
        state[o] = [a, b]
    return score
ans = 0
for order in product(range(4), repeat=10):
    ans = max(ans, func(order))
print(ans)
"""
1 2 3 4 1 2 3 4 1 2
"""