# programmers - 2018 kakao blind - 실패율
N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
N = 2
stages = [1, 1, 2, 3]
import collections
def solution(N, stages):
    answer = []
    s = len(stages)
    l = collections.Counter(stages)
    for i in range(1, N+1):
        if s == 0:
            answer.append(0)
        else:
            answer.append(l[i] / s)
            s -= l[i]
    answer = sorted(enumerate(answer), key=lambda x: x[1], reverse=True)
    return [i+1 for i, _ in answer]
print(solution(N, stages))
exit()

# BOJ - 2138
n = int(input())
arr1, arr2 = input(), input()
dd = {'1':'0', '0':'1'}
a, b = dd[arr1[0]], dd[arr1[1]]
c, d = arr1[:2]
ans1, ans2 = 1, 0
for i in range(1, n-1):
    if a != arr2[i-1]:
        ans1 += 1
        a, b = dd[b], dd[arr1[i+1]]
    else:
        a, b = b, arr1[i+1]
    if c != arr2[i-1]:
        ans2 += 1
        c, d = dd[d], dd[arr1[i+1]]
    else:
        c, d = d, arr1[i+1]
if a != arr2[-2]:
    ans1 += 1
    b = dd[b]
if c != arr2[-2]:
    ans2 += 1
    d = dd[d]
if b == arr2[-1] and d == arr2[-1]:
    print(min(ans1, ans2))
elif b == arr2[-1]:
    print(ans1)
elif d == arr2[-1]:
    print(ans2)
else:
    print(-1)

"""
3
000
010

5
00000
01110

2
01
11
"""