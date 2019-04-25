# programmers - 2018 blind kakao - 오픈채팅방
record = ["Enter uid1234 Muzi",
          "Enter uid4567 Prodo",
          "Leave uid1234",
          "Enter uid1234 Prodo",
          "Change uid4567 Ryan"]
import collections
def solution(record):
    l = []
    uid = collections.defaultdict(str)
    for r in record:
        if r[0] == 'L':
            c, u = r.split()
            l.append((c, u))
        elif r[0] == 'E':
            c, u, n = r.split()
            l.append((c, u))
            uid[u] = n
        else:
            _, u, n = r.split()
            uid[u] = n
    answer = []
    for c, u in l:
        if c[0] == 'E':
            string = '%s님이 들어왔습니다.' % uid[u]
            answer.append(string)
        else:
            string = '%s님이 나갔습니다.' % uid[u]
            answer.append(string)
    return answer
print(solution(record))
exit()
# programmers - 2017 blind kakao - 셔틀버스
# n, t, m = 1, 1, 5
# timetable = ['08:00', '08:01', '08:02', '08:03']
n, t, m = 10, 60, 45
timetable = ['23:59'] * 16
# n, t, m = 2, 10, 2
# timetable = ["09:10", "09:09", "08:00"]
# n, t, m = 2, 1, 2
# timetable = ["00:01", "00:01", "09:00"]
def func(i, t):
    h, mm = divmod(i * t, 60)
    time = str(9 + h).zfill(2) + ':' + str(mm).zfill(2)
    return time
def substract_time(time: str, t: int):
    h, m = map(int, time.split(':'))
    hh, m = divmod(m-t, 60)
    h += hh
    return str(h).zfill(2) + ':' + str(m).zfill(2)
def solution(n, t, m, timetable):
    answer = '09:00'
    timetable.sort(reverse=True)
    mm = m
    idx = 0
    while timetable and idx < n:
        time = timetable.pop()
        if answer >= time:
            if idx + 1 < n:
                if mm > 0: mm -= 1
                else:
                    idx += 1
                    answer = func(idx, t)
                    mm = m - 1
            else:
                if mm > 1: mm -= 1
                else: return substract_time(time, 1)
        else:
            while True:
                if idx < n:
                    if func(idx, t) >= time:
                        mm = m - 1
                        answer = func(idx, t)
                        break
                    else: idx += 1
                else:
                    break
    if idx <= n: answer = func(n-1, t)
    return answer
print(solution(n, t, m, timetable))
exit()

# BOJ - 17130
import sys
sys.setrecursionlimit(10000000)
read = lambda: sys.stdin.readline().rstrip()
n, m = map(int, read().split())
arr = [read() for _ in range(n)]
dp = [[-1] * m for _ in range(n)]
d = ((1, 1), (0, 1), (-1, 1))
def func(x, y):
    t = -987654321
    for dx, dy in d:
        if -1 < x+dx < n and -1 < y+dy < m:
            if arr[x+dx][y+dy] == '#': continue
            if arr[x+dx][y+dy] == 'C':
                t = max(t, dp[x+dx][y+dy]+1 if dp[x+dx][y+dy] != -1 else func(x+dx, y+dy)+1)
            elif arr[x+dx][y+dy] == 'O':
                t = max(t, 0, dp[x+dx][y+dy] if dp[x+dx][y+dy] != -1 else func(x+dx, y+dy))
            else:
                t = max(t, dp[x+dx][y+dy] if dp[x+dx][y+dy] != -1 else func(x+dx, y+dy))
    dp[x][y] = t
    return dp[x][y]
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'R':
            func(i, j)
            if dp[i][j] < 0: print(-1)
            else: print(dp[i][j])
            exit()
"""
3 5
RC#OO
.#CCC
..O..

2 4
CC#O
RC##
"""