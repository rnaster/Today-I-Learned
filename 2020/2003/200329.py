# programmers - 2018 kakao blind 프렌즈4블록
m, n = 4, 5
board = ['CCBDE', 'AAADE', 'AAABF', 'CCBBF']
def solution(m, n, board):
    for i in range(m): board[i] = [*board[i]]
    ans = 0
    def func(i, j):
        return board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1]
    while 1:
        tmp = 0
        arr = [[False] * n for _ in range(m)]
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] and func(i, j):
                    tmp += 4 - arr[i][j] - arr[i+1][j] - arr[i][j+1] - arr[i+1][j+1]
                    arr[i][j] = arr[i+1][j] = arr[i][j+1] = arr[i+1][j+1] = True
        for j in range(n):
            row = [board[i][j] for i in range(m) if not arr[i][j]]
            row = [''] * (m-len(row)) + row
            for i in range(m):
                board[i][j] = row[i]
        if tmp == 0: break
        ans += tmp
    return ans
print(solution(m, n, board))