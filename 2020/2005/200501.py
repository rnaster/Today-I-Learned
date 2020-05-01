# programmers - 2019 winter 종이접기
def solution(n):
    ans = [0]
    for i in range(1, n):
        tmp = [0, 1] * 2 ** (i-1)
        for t, a in zip(tmp, ans):
            l.extend([t, a])
        l.append(1)
        ans = l
    return ans
print(solution(4))
exit()

# programmers - 2019 winter 멀쩡한 사각형
import math
def solution(w,h):
    if w == h:
        return w*(w - 1)
    a, b = max(w, h), min(w, h)
    c = math.gcd(a, b)
    a //= c
    b //= c
    return w*h - (math.ceil(a / b)*b + max((a % b) - 1, 0))*c
exit()

# programmers - 단속카메라
routes = [[-20, 15], [-14, -5], [-18, -13], [-5, -3]]
def solution(routes):
    answer = 1
    routes.sort()
    c = 987654321
    for a, b in routes:
        if a > c:
            c = b
            answer += 1
        else: c = min(c, b)
    return answer
print(solution(routes))
