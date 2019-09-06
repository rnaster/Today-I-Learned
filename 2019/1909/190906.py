# programmers - 2018 kakao blind 후보키
relation = [["100", "ryan", "music", "2"],
            ["200", "apeach", "math", "2"],
            ["300", "tube", "computer", "3"],
            ["400", "con", "computer", "4"],
            ["500", "muzi", "music", "3"],
            ["600", "apeach", "music", "2"]]
from itertools import combinations
def solution(relation):
    answer = 0
    m, n = len(relation), len(relation[0])
    power = []
    for i in range(n, 0, -1):
        power += list(combinations(range(n), i))
    while power:
        comb = power.pop()
        s = set()
        for i in range(m):
            s.update({tuple([relation[i][j] for j in comb])})
        if len(s) == m:
            answer += 1
            _power = []
            for _comb in power:
                if len(set(comb) - set(_comb)) > 0:
                    _power.append(_comb)
            power = _power
    return answer

# programmers - 2017 kakao blind 3차 자동완성
words = ['go', 'gone', 'guild']
words = ['abc', 'def', 'ghi', 'jklm']
words = ['word', 'war', 'warrior', 'world']
def solution(words):
    answer = 0
    w = {}
    for i, word in enumerate(words):
        if word[0] in w:
            w[word[0]].append(i)
        else:
            w[word[0]] = [i]
    l = w.values()
    i = 1
    while l:
        print(l)
        ll = []
        for _l in l:
            if len(_l) > 1:
                w = {}
                for j in _l:
                    if len(words[j]) > i:
                        if words[j][i] in w:
                            w[words[j][i]].append(j)
                        else:
                            w[words[j][i]] = [j]
                    else:
                        answer += i
                ll.extend(list(w.values()))
            else:
                answer += i
        l = ll
        i += 1
    return answer
