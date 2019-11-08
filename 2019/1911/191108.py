# programmers - 2020 kakao blind 문자열 압축
s = 'abcabcabcabcdededededede'
def solution(s):
    n = len(s)
    ans = n
    for i in range(1, n//2+1):
        ans_ = 0
        tmp = s[:i]
        a = 1
        j = 0
        for j in range(i, n, i):
            if s[j:j+i] == tmp:
                a += 1
            else:
                ans_ += i + len(str(a)) if a > 1 else i
                tmp = s[j:j+i]
                a = 1
        ans_ += len(s[j+i:])
        ans_ += len(tmp) + len(str(a)) if a > 1 else len(tmp)
        ans = min(ans, ans_)
    return ans
print(solution(s))
exit()

# programmers - 2020 kakao blind 자물쇠와 열쇠
key = [[0, 0, 0],
       [1, 0, 1],
       [0, 0, 1]]
lock = [[1, 1, 1, 1],
        [0, 0, 0, 0],
        [1, 1, 1, 1],
        [0, 0, 1, 1]]
def rot(arr):
    n = len(arr)
    arr_ = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            arr_[j][n-1-i] = arr[i][j]
    return arr_
def func(arr1, arr2):
    n, m = len(arr1), len(arr1[0])
    val = 0
    for i in range(n):
        for j in range(m):
            if (arr1[i][j], arr2[i][j]) == (1, 1):
                return -1
            elif (arr1[i][j], arr2[i][j]) == (1, 0):
                val += 1
    return val
def solution(key, lock):
    n, m = len(key), len(lock)
    t = m * m - sum(sum(l) for l in lock)
    for _ in range(4):
        key = rot(key)
        for i in range(n+m-1):
            a1, a2 = max(0, n-1-i), min(n, n+m-1-i)
            b1, b2 = max(0, i-n+1), min(i + 1, m)
            for j in range(n+m-1):
                c1, c2 = max(0, n-1-j), min(n, n+m-1-j)
                d1, d2 = max(0, j-n+1), min(j + 1, m)
                if func([row[c1:c2] for row in key[a1:a2]],
                        [row[d1:d2] for row in lock[b1:b2]]) == t:
                    return True
    return False
print(solution(key, lock))
exit()

# programmers - 2020 kakao blind 괄호변환
p = '))((((())(())))('
def func(p):
    l = []
    for pp in p:
        if pp == '(':
            l.append(pp)
        elif len(l) > 0 and (l[-1], pp) == ('(', ')'):
            l.pop()
        else:
            return False
    return True
d = {'(': 1, ')': -1}
def rev(p):
    dd = {'(': ')', ')': '('}
    return ''.join(dd[pp] for pp in p)
def solution(p_):
    if p_ == '': return p_
    a = d[p_[0]]
    for i, pp in enumerate(p_[1:], 1):
        a += d[pp]
        if a == 0:
            if func(p_[:i+1]):
                return p_[:i+1] + solution(p_[i+1:])
            return '(' + solution(p_[i+1:]) + ')' + rev(p_[1:i])
print(solution(p))
