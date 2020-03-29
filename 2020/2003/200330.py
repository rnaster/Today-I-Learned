# programmers - 2018 s/w coding 스티커(2)
sticker = [14, 6, 5, 11, 3, 9, 2, 10]
def solution(sticker):
    n = len(sticker)
    if n == 1: return sticker[0]
    a, b = 0, 0
    aa, bb = 0, 0
    for i in range(n-1):
        a, aa = max(aa + sticker[i], a), a
    for i in range(1, n):
        b, bb = max(bb + sticker[i], b), b
    return max(a, b)
print(solution(sticker))
exit()

# programmers - 2019 kakao blind 블록게임
board = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 4, 0, 0, 0],
         [0, 0, 0, 0, 0, 4, 4, 0, 0, 0],
         [0, 0, 0, 0, 3, 0, 4, 0, 0, 0],
         [0, 0, 0, 2, 3, 0, 0, 0, 5, 5],
         [1, 2, 2, 2, 3, 3, 0, 0, 0, 5],
         [1, 1, 1, 0, 0, 0, 0, 0, 0, 5]]
from collections import Counter
def solution(board):
    n = len(board)
    ans = 0
    def func():
        for j in range(n):
            for i in range(n):
                if board[i][j] < 1:
                    board[i][j] = -1
                else: break
        return
    def func1(i, j):
        s = Counter(
            [board[i][j], board[i][j + 1], board[i][j + 2],
             board[i + 1][j], board[i + 1][j + 1], board[i + 1][j + 2]]
        )
        if len(s) == 2 and 0 not in s and s[-1] == 2:
            board[i][j] = board[i][j + 1] = board[i][j + 2] = 0
            board[i + 1][j] = board[i + 1][j + 1] = board[i + 1][j + 2] = 0
            return True
        return False
    def func2(i, j):
        s = Counter(
            [board[i][j], board[i][j + 1],
             board[i + 1][j], board[i + 1][j + 1],
             board[i + 2][j], board[i + 2][j + 1]]
        )
        if len(s) == 2 and 0 not in s and s[-1] == 2:
            board[i][j] = board[i][j + 1] = 0
            board[i + 1][j] = board[i + 1][j + 1] = 0
            board[i + 2][j] = board[i + 2][j + 1] = 0
            return True
        return False
    while 1:
        tmp = 0
        func()
        for i in range(n-1):
            for j in range(n-2):
                tmp += func1(i, j)
        func()
        for i in range(n - 2):
            for j in range(n - 1):
                tmp += func2(i, j)
        if tmp == 0: break
        ans += tmp
    return ans
print(solution(board))
