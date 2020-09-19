# programmers - 2018 kakao blind
str1 = "handshake"
str2 = "shake hands"
import re
from collections import Counter
def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    l1 = []
    pat = re.compile("[a-z]{2}")
    for i in range(len(str1)-1):
        s = str1[i:i+2]
        if pat.match(s):
            l1.append(s)
    l2 = []
    for i in range(len(str2)-1):
        s = str2[i:i+2]
        if pat.match(s):
            l2.append(s)
    if l1 == [] and l2 == []: return 65536
    l1 = Counter(l1)
    l2 = Counter(l2)
    s1, s2 = [], []
    for k, v in l1.items():
        if k in l2:
            s1.append(min(v, l2[k]))
        s2.append(v)
    for _, v in l2.items():
        s2.append(v)
    return int(sum(s1) / (sum(s2) - sum(s1)) * 65536)
print(solution(str1, str2))
exit()

# programmers - 2019 kakao blind
food_times = [3, 1, 2]
k = 5
food_times = [5, 5, 5, 5, 1, 7, 6]
k = 31
def solution(food_times, k):
    if sum(food_times) <= k: return -1
    n = len(food_times)
    arr = [[i for i in range(1, n + 1)], [i for i in range(-1, n - 1)]]
    arr[0][-1] = 0
    arr[1][0] = n - 1
    t = 0
    cnt = n
    for i, v in sorted(enumerate(food_times), key=lambda x: x[1]):
        v -= t
        if k >= v * cnt:
            k -= v * cnt
            t += v
            cnt -= 1
            arr[0][arr[1][i]] = arr[0][i]
            arr[1][arr[0][i]] = arr[1][i]
        else:
            k %= cnt
            l = [0] * cnt
            for j in range(cnt):
                l[j] = i
                i = arr[0][i]
            l.sort()
            return l[k] + 1
print(solution(food_times, k))
exit()
