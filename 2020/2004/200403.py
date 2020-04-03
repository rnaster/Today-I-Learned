# programmers - 2019 kakao winter 징검다리 건너기
stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3
def solution(stones, k):
    a, c = 1, max(stones)
    b = c
    def func(bb):
        t = [s >= bb for s in stones]
        tt = sum(t[:k])
        if tt < 1: return False
        for i in range(k, len(stones)):
            tt += t[i] - t[i-k]
            if tt < 1: return False
        return True
    while a < b <= c:
        if func(b):
            a = b
        else:
            c = b
        b = (a+c) // 2
    return b
print(solution(stones, k))