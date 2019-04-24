# programmers - 2017 kakao blind - 파일명 정렬
# files = ['img12.png', 'img10.png', 'img02.png', 'img1.png', 'IMG01.GIF', 'img2.JPG']
# files = ['F-5 Freedom Fighter', 'B-50 Superfortress', 'A-10 Thunderbolt II', 'F-14 Tomcat']
files = ['x10', 'a1', 'a2', 'aa1']
def solution(files):
    answer = []
    l = []
    for f in files:
        tmp = []
        i = 0
        while True:
            if '0' <= f[i] <= '9': break
            i += 1
        tmp.append(f[:i].lower())
        t = i
        while i < len(f):
            if '9' < f[i] or f[i] in (' ', '.', '-'): break
            i += 1
        tmp.append(f[t:i].zfill(5))
        l.append(tmp)
    for k, v in sorted(enumerate(l), key=lambda x: x[1]):
        answer.append(files[k])
    return answer
print(solution(files))
exit()

# programmers - 2017 kakao blind - 압축
msg = "TOBEORNOTTOBEORTOBEORNOT"
# msg = "KAKAO"
import string
d = {string.ascii_uppercase[i-1]:i for i in range(1, 27)}
def solution(msg):
    answer = []
    idx = 26
    i = 0
    while i < len(msg):
        k = 1
        while msg[i:i+k] in d and i+k <= len(msg):
            k += 1
        if not msg[i:i+k] in d:
            idx += 1
            d[msg[i:i+k]] = idx
        answer.append(d[msg[i:i+k-1]])
        i += k-1
    return answer
print(solution(msg))
exit()

# BOJ - 5430
import sys
read = lambda: sys.stdin.readline().rstrip()
for _ in range(int(read())):
    a, b = read(), int(read())
    c = list(read().strip('[]').split(','))
    if b == 0:
        if 'D' in a: print('error'); continue
        else: print('[]');continue
    p, q, r = 0, b, 1
    stop, is_error = False, False
    for aa in a:
        if aa == 'R':
            if r == 1: p, q, r = q-1, p-1, -1
            else: p, q, r = q+1, p+1, 1
        else:
            if b == 0: stop = True; is_error = True; break
            p += 1 * r
            b -= 1
    if stop:
        if is_error: print('error')
        else: print('[]')
    else:
        print('[', end='')
        for i in range(p, q-r, r): print(c[i], end=',')
        if b == 0:
            print(']')
        else:
            print('%s]' % c[q-r])

"""
4
RDD
4
[1,2,3,4]
DRRRDRR
1
[42]
RDRDD
6
[1,1,2,3,5,8]
RRRD
0
[]

1
DRRRRRR
1
[42]
"""