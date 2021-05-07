# programmers - 2019 kakao internship 튜플
s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
import re
def solution(s):
    l = re.findall("\{[\d,]+?\}", s)
    l.sort(key=len)
    # print(l, "#")
    ans = []
    for ll in l:
        ll = ll.strip("{}").split(',')
        for lll in ll:
            if lll not in ans:
                ans.append(lll)
                break
    return [*map(int, ans)]
print(solution(s))
exit()

# programmers - 2019 kakao internship 불량 사용자
user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "*rodo", "******", "******"]
user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "abc1**"]
import re
def solution(user_id, banned_id):
    banned_user_indices = []
    for b_id in banned_id:
        pat = re.compile(b_id.replace("*", "\w") + "$")
        tmp = []
        for idx, u_id in enumerate(user_id):
            if pat.match(u_id):
                tmp.append(idx)
        banned_user_indices.append(tmp)
    l = [0]
    for indices in banned_user_indices:
        tmp = []
        for i in l:
            for idx in indices:
                if not i & 1 << idx:
                    tmp.append(i | 1 << idx)
        l = tmp
    return len(set(l))
print(solution(user_id, banned_id))
exit()

# programmers - 2020 kakao internship 수식 최대화
expression = "100-200*300-500+20"
expression = "50*6-3*2"
import re
from itertools import permutations
def solution(expression):
    def func2(a, b, o):
        if o == "*":
            return a * b
        if o == "-":
            return a - b
        return a + b
    def func(digits:list, ops, o):
        idx = 0
        while idx < len(ops):
            if ops[idx] == o:
                ops.pop(idx)
                a = digits.pop(idx)
                b = digits.pop(idx)
                digits.insert(idx, func2(a, b, o))
            else:
                idx += 1
        return
    answer = 0
    operator = ["*", "-", "+"]
    for comb in permutations(range(3), 3):
        digits = [*map(int, re.findall('\d+', expression))]
        ops = re.findall("[-+*]", expression)
        for c in comb:
            func(digits, ops, operator[c])
        answer = max(answer, abs(digits[0]))
        # print(answer, digits, ops, "#")
    return answer
print(solution(expression))
exit()

# programmers - 2020 kakao internship 보석쇼핑
gems = ["AA", "AB", "AC", "AA", "AC"]
gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
def solution(gems):
    gem2id = {key: i for i, key in enumerate(set(gems))}
    l = [0] * len(gem2id)
    i, j = 0, 0
    ans = [-100_000, 100_000]
    cnt = 0
    n = len(gems)
    while j < n:
        # print(f"(i, j): {i, j}, cnt: {cnt}, l: {l}, ans: {ans}")
        t = gem2id[gems[j]]
        if l[t] == 0:
            cnt += 1
        l[t] += 1
        while i < j:
            t = gem2id[gems[i]]
            if l[t] > 1:
                l[t] -= 1
                i += 1
            else:
                break
        if cnt == len(gem2id) and ans[1] - ans[0] > j - i:
            ans = [i, j]
        j += 1
    j -= 1
    if ans[1] - ans[0] > j - i:
        ans = [i, j]
    return [ans[0] + 1, ans[1] + 1]
print(solution(gems))
