# programmers - 2020 kakao blind 블록 이동하기
board = [[0, 0, 0, 1, 1, 0],
         [0, 0, 0, 1, 0, 0],
         [0, 1, 0, 1, 1, 0],
         [1, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 1, 0]]
def solution(board):
    ans = 0
    n = len(board)
    cache = [[[0] * n for _ in range(n)] for _ in range(2)]
    cache[0][0][1] = 1
    q = [(0, 0, 1)]
    d0 = ((-1, 0), (1, 0), (0, 1), (0, -2))
    d1 = ((-2, 0), (1, 0), (0, 1), (0, -1))
    while q:
        tmp = []
        for a, b, c in q:
            if (b, c) == (n-1, n-1):
                return ans
            if a == 0:
                for dx, dy in d0:
                    dy_ = max(-1, dy)
                    if (-1 < b + dx < n and -1 < c + dy < n
                            and cache[0][b+dx][c+dy_] < 1
                            and board[b+dx][c+dy_] + board[b+dx][c+dy_-1] < 1):
                        tmp.append((0, b+dx, c+dy_))
                        cache[0][b+dx][c+dy_] = 1
                if 0 < b and board[b-1][c] + board[b-1][c-1] < 1:
                    if cache[1][b][c] < 1:
                        tmp.append((1, b, c))
                        cache[1][b][c] = 1
                    if cache[1][b][c-1] < 1:
                        tmp.append((1, b, c-1))
                        cache[1][b][c-1] = 1
                if b < n-1 and board[b+1][c] + board[b+1][c-1] < 1:
                    if cache[1][b+1][c] < 1:
                        tmp.append((1, b+1, c))
                        cache[1][b+1][c] = 1
                    if cache[1][b+1][c-1] < 1:
                        tmp.append((1, b+1, c-1))
                        cache[1][b+1][c-1] = 1
            else:
                for dx, dy in d1:
                    dx_ = max(-1, dx)
                    if (-1 < b + dx < n and -1 < c + dy < n
                            and cache[1][b + dx_][c + dy] < 1
                            and board[b + dx_-1][c + dy] + board[b + dx_][c + dy] < 1):
                        tmp.append((1, b+dx_, c+dy))
                        cache[1][b+dx_][c+dy] = 1
                if c < n-1 and board[b][c+1] + board[b-1][c+1] < 1:
                    if cache[0][b][c+1] < 1:
                        tmp.append((0, b, c+1))
                        cache[0][b][c+1] = 1
                    if cache[0][b-1][c+1] < 1:
                        tmp.append((0, b-1, c+1))
                        cache[0][b-1][c+1] = 1
                if 0 < c and board[b][c-1] + board[b-1][c-1] < 1:
                    if cache[0][b][c] < 1:
                        tmp.append((0, b, c))
                        cache[0][b][c] = 1
                    if cache[0][b-1][c] < 1:
                        tmp.append((0, b-1, c))
                        cache[0][b-1][c] = 1
        ans += 1
        q = tmp
print(solution(board))