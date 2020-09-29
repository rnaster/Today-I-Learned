# BOJ - 13913
n, m = map(int, input().split())
visit = [True] * 100_003
l = [-1] * 100_003
visit[n] = False
q = [n]
cnt = 0
while q:
    tmp = []
    for a in q:
        if a == m:
            print(cnt)
            ll = []
            while l[m] > -1:
                ll.append(m)
                m = l[m]
            ll.append(n)
            for i in range(len(ll)-1, -1, -1):
                print(ll[i], end=" ")
            exit()
        if a - 1 > -1 and visit[a-1]:
            visit[a-1] = False
            tmp.append(a-1)
            l[a-1] = a
        if a+1 < 100_003 and visit[a+1]:
            visit[a+1] = False
            tmp.append(a+1)
            l[a+1] = a
        if 2*a < 100_003 and visit[2*a]:
            visit[2*a] = False
            tmp.append(2*a)
            l[2*a] = a
    q = tmp
    cnt += 1
"""
5 17
"""