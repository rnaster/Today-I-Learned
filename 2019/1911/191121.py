# programmers - 2020 kakao blind 가사 검색
words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
cache = {}
def solution(words, queries):
    words = set(words)
    ans = [0] * len(queries)
    d = {}
    for i, q in enumerate(queries):
        if d.get(q, -1) < 0:
            n = 0
            if q[0] == '?':
                idx = q.rfind('?')
                _q = q[idx+1:]
                for w in words:
                    if len(q) == len(w) and _q == w[idx+1:]:
                        n += 1
            else:
                idx = q.find('?')
                _q = q[:idx]
                for w in words:
                    if len(q) == len(w) and _q == w[:idx]:
                        n += 1
            d[q] = n
        ans[i] = d[q]
    return ans
print(solution(words, queries))