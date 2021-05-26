# programmers - 괄호 회전하기
s = "[](){}"
# s = "}]()[{"
s = "{[]({)}}"
s = "{[](){}}"
from collections import deque
def solution(s):
    answer = 0
    l = deque(s)
    a = s.count("[") - s.count("]")
    b = s.count("{") - s.count("}")
    c = s.count("(") - s.count(")")
    if a != 0 or b != 0 or c != 0:
        return 0
    def func(l):
        print(' '.join(l))
        ll = []
        for i in l:
            print(ll, "#")
            if len(ll) == 0:
                if i == "}" or i == "]" or i == ")":
                    return 0
                ll.append(i)
            elif ll[-1] == "[":
                if i == "]":
                    ll.pop()
                elif i in ["[", "{", "("]:
                    ll.append(i)
                else:
                    return 0
            elif ll[-1] == "{":
                if i == "}":
                    ll.pop()
                elif i in ["[", "{", "("]:
                    ll.append(i)
                else:
                    return 0
            else:
                if i == ")":
                    ll.pop()
                elif i in ["[", "{", "("]:
                    ll.append(i)
                else:
                    return 0
        return 1
    for _ in range(len(s)):
        answer += func(l)
        print()
        l.append(l.popleft())
    return answer
print(solution(s))
