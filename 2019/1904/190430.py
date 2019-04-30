# programmers - 2017 kakao blind - n진수 게임
n, t, m, p = 2, 4, 2, 1
# n, t, m, p = 16, 16, 2, 1
# n, t, m, p = 16, 16, 2, 2
# n, t, m, p = 4, 4, 7, 7
d = {0:0,1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,
    10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
def solution(n, t, m, p):
    answer = '%s' * t
    l, a = [], [-1]
    idx = p-1
    while len(l) < t:
        b = 1
        for i in range(len(a)):
            b, a[i] = divmod(a[i]+b, n)
        if b > 0: a.append(1)
        if idx - len(a) > 0:
            idx -= len(a)
        else:
            l.extend(a[::-1][idx:][::m])
            idx = (idx - len(a)) % m
    return answer % tuple([d[i] for i in l[:t]])
print(solution(n, t, m, p))