# BOJ - 7344
import sys
read = sys.stdin.readline
for _ in range(int(read())):
    n = int(read())
    l = [*map(int, read().split())]
    arr = sorted((l[i], l[i+1]) for i in range(0, 2*n, 2))
    a = [-1]
    for _, i in arr:
        flag = True
        for j in range(len(a)):
            if a[j] <= i:
                a[j] = i
                flag = False
                break
        if flag:
            a.append(i)
    print(len(a))
"""
3
5
4 9 5 2 2 1 3 5 1 4
3
2 2 1 1 2 2
3
1 3 2 2 3 1
"""
exit()

# programmers - 2019 kakao winter 호텔 방 배정
# import sys
sys.setrecursionlimit(1000000)
k = 10
room_number = [1,3,4,1,3,1]
def solution(_, room_number):
    ans = []
    l = {}
    def func(a):
        nn = l[a]
        if nn not in l:
            return nn
        val = func(nn)
        l[a] = val
        return val
    for num in room_number:
        if num in l:
            num = func(num)
        ans.append(num)
        l[num] = num+1
    return ans
print(solution(k, room_number))

"""
good reference

def solution(k, room_number):
    room_dic = {}
    ret = []
    for i in room_number:
        n = i
        visit = [n]
        while n in room_dic:
            n = room_dic[n]
            visit.append(n)
        ret.append(n)
        for j in visit:
            room_dic[j] = n+1
    return ret
"""