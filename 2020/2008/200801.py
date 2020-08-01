# programmers - 2020 kakao blind 가사 검색
words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
def solution(words, queries):
    forward = [[-1] * 27]
    backward = [[-1] * 27]
    forward[0][-1] = {}
    backward[0][-1] = {}
    cur = [1, 1]
    def func(arr, word, ptr):
        i = 0
        s = len(word)
        for w in word:
            j = ord(w) - 97
            arr[i][-1][s] = arr[i][-1].get(s, 0) + 1
            if arr[i][j] > -1:
                i = arr[i][j]
            else:
                arr[i][j] = cur[ptr]
                i = cur[ptr]
                cur[ptr] += 1
                arr.append([-1] * 27)
                arr[-1][-1] = {}
        arr[i][-1][s] = arr[i][-1].get(s, 0) + 1
        return
    ans = [0] * len(queries)
    for word in words:
        func(forward, word, 0)
        func(backward, word[::-1], 1)
    for i, query in enumerate(queries):
        s = len(query)
        if query[0] == "?":
            query = query[::-1]
            arr = backward
        else:
            arr = forward
        j = 0
        for q in query:
            if q == "?":
                ans[i] = arr[j][-1].get(s, 0)
            else:
                j = arr[j][ord(q) - 97]
                if j == -1: break
    return ans
print(solution(words, queries))
