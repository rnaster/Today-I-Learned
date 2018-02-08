# BOJ - 11070
from sys import stdin
read = lambda: stdin.readline().rstrip()
def fun(tp):
    if tp[0] == 0: return 0
    if tp[0] == 0 and tp[1] == 0: return 0
    return int(tp[0] ** 2 / (tp[0] ** 2 + tp[1] ** 2) * 1000)
for _ in range(int(read())):
    dic = {}
    n, m = map(int, read().split())
    for _ in range(m):
        a, b, p, q = map(int, read().split())
        if not a in dic.keys(): dic[a] = (0, 0)
        if not b in dic.keys(): dic[b] = (0, 0)
        dic[a] = (dic[a][0] + p, dic[a][1] + q)
        dic[b] = (dic[b][0] + q, dic[b][1] + p)
    Ma, Mi = 0, 1000
    for k in dic.keys():
        Ma = max(Ma, fun(dic[k]))
        Mi = min(Mi, fun(dic[k]))
    if len(dic.keys()) < n: Mi = 0
    print(Ma)
    print(Mi)
'''
2
3 5
1 2 3 5
1 3 10 1
1 2 0 7
2 3 9 3
3 2 4 5
4 6
1 2 0 11
1 3 17 13
1 4 17 1
2 3 7 12
2 4 19 17
3 4 17 0
'''